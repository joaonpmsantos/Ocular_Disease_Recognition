FROM python:3.8.12-buster

# First, pip install dependencies
COPY api/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Then only, install taxifare!
COPY api api
#not sure if needed:
#RUN pip install .

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT


#Locally
#docker build --tag=odr:dev .
#docker run -it -e PORT=8000 -p 8000:8000 odr:dev

#GCP
#docker build -t eu.gcr.io/civic-cedar-378816/odr:prod .
#docker push eu.gcr.io/civic-cedar-378816/odr:prod
#gcloud run deploy --image eu.gcr.io/civic-cedar-378816/odr:prod --memory 4Gi --region europe-west1
