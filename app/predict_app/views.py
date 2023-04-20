from django.shortcuts import render
from django.utils import timezone
from django.views.generic import CreateView, UpdateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, FileResponse

from .forms import PostForm, UploadFileForm
from .models import Post

import sys
import os
# import paramiko
# import socket
import subprocess
from subprocess import PIPE
import traceback

@login_required
def index(request):
    """
    ホーム画面
    """
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'predict_app/index.html')


class PostCreateView(LoginRequiredMixin,CreateView):
    """
    試作
    使ってない
    """
    model = Post
    form_class = PostForm
    template_name = 'predict_app/postform.html'
    success_url = "predict_app/"  # 成功時にリダイレクトするURL

@login_required
def file_upload(request):
    """
    ファイルアップロード画面を構成する
    アップロードされたファイルを機械学習をする関数に投げる
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            create_time = timezone.now().strftime('%Y%m%d%H%M%S')
            context = {}
            sys.stderr.write("*** file_upload *** aaa ***\n")
            file_path, dir_path = handle_uploaded_file(request.FILES['file'],create_time)
            file_obj = request.FILES['file']
            sys.stderr.write(file_obj.name + "\n")
            post = Post.objects.create(
                author = request.user,
                title=request.POST["title"],
                text=request.POST["title"],
                file_path=file_path ,
                result_path = "",
                )
            context['post'] = post
            predict(post,dir_path)
            return render(request, 'predict_app/upload_success.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'predict_app/upload.html', {'form': form})

def handle_uploaded_file(file_obj,create_time):
    """
    ウェブページからサーバーにファイルをアップロード
    """
    sys.stderr.write("*** handle_uploaded_file *** aaa ***\n")
    sys.stderr.write(file_obj.name + "\n")
    dir_path = f'media/documents/{create_time}/' 
    os.makedirs(dir_path, exist_ok=True)
    file_path = dir_path + "data.csv" 
    sys.stderr.write(file_path + "\n")
    with open(file_path, 'wb+') as destination:
        for chunk in file_obj.chunks():
            sys.stderr.write("*** handle_uploaded_file *** ccc ***\n")
            destination.write(chunk)
            sys.stderr.write("*** handle_uploaded_file *** eee ***\n")
    return file_path, dir_path

def predict(post,dir_path):
    """
    機械学習
    予測結果をcsvファイルとして保存する
    """
    try:
        # raise
        
        sys.stderr.write("exec_command command\n")
        cmd = f"bash /code/lightgbm/test.sh {dir_path} {post.pk} "
        proc = subprocess.run(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
        sys.stderr.write(cmd)
    except Exception as e:
        print(e)
        traceback.print_exc()
        post.result_path = "error"
        post.save()


class PostListView(LoginRequiredMixin, ListView):
    """
    登録されたアイテムリストを表示する画面
    """
    template_name = 'predict_app/postlist.html'
    model = Post
    ordering = '-created_date' 

@login_required
def result_download_view(request, pk):
    post = Post.objects.get(pk=pk)
    print(post)
    filename = os.path.basename(post.result_path)
    filepath = post.result_path
    print(filepath)
    return FileResponse(open(filepath, "rb"), as_attachment=True, filename=filename)

@login_required
def input_download_view(request, pk):
    post = Post.objects.get(pk=pk)
    print(post)
    filename = os.path.basename(post.file_path)
    filepath = post.file_path
    print(filepath)
    return FileResponse(open(filepath, "rb"), as_attachment=True, filename=filename)