FROM registry.access.redhat.com/ubi9/python-312:latest
WORKDIR /app
ADD requirements.txt requirements.txt
ADD server.py server.py
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["python", "server.py", "--port", "8000"]
