FROM tomoncle/python27:alpine.latest
MAINTAINER Tom.Lee <1123431949@qq.com>

WORKDIR /workspace
ADD ./ /workspace/app

RUN pip install -r /workspace/app/requirements.txt

EXPOSE 5000
CMD ["python", "/workspace/app/bootstrap_app.py"]