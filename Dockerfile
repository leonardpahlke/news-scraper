FROM python:3

# create src folder in container
RUN mkdir /zeitonline
COPY zeitonline /zeitonline

# copy requirements to docker
COPY requirements.txt ./

# install pip requirements
RUN pip install -r requirements.txt

# copy api.py to docker container
COPY api.py /

EXPOSE 8080

# execute app in api.py file
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8080"]

# uvicorn api:app --host 0.0.0.0 --port 8080