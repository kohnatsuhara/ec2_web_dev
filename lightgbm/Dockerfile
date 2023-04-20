FROM python:3.8
RUN pip install pandas scikit-learn lightgbm mecab-python3 jupyterlab
RUN apt update
RUN apt install mecab -y
RUN apt install libmecab-dev -y
RUN apt install mecab-ipadic-utf8 -y