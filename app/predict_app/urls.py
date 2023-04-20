from django.urls import path

from . import views




urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.LoginView.as_view(), name="login"),
    
    path('postcreate', views.PostCreateView.as_view(), name="postcreate"),
    path('fileupload', views.file_upload, name='file_upload'),
    path('postlist', views.PostListView.as_view(), name='postlist'),
    path('result_download/<int:pk>', views.result_download_view, name='result_download'),
    path('input_download/<int:pk>', views.input_download_view, name='input_download'),
]