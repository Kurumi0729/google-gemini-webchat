FROM python:3.10


RUN python3 -m pip install  Flask==2.3.2
RUN python3 -m pip install google-cloud-aiplatform==1.39.0
RUN python3 -m pip install  google-api-core==2.11.0
RUN python3 -m pip install  Flask-Cors==3.0.10
RUN python3 -m pip install  google-auth==2.19.1
RUN python3 -m pip install  googleapis-common-protos==1.59.0
RUN python3 -m pip install  grpcio==1.54.2
RUN python3 -m pip install  grpcio-status==1.54.2
RUN python3 -m pip install  google-api-python-client==2.84.0 
RUN python3 -m pip install  pytz==2021.3

WORKDIR /app
COPY app.py /app

EXPOSE 8080
CMD ["python3", "app.py"]