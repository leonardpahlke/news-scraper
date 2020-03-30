FROM python:3

# create src folder in container
RUN mkdir /zeitonline
COPY zeitonline /zeitonline

# copy requirements to docker
COPY requirements.txt ./

# install pip requirements
RUN pip install -r requirements.txt

# copy api.py and LICENSE to docker container
COPY api.py /

EXPOSE 8080
# execute api.py file

# TODO error handling
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "80"]

# TODO Docker compose