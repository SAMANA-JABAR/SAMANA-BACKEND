# SAMANA-BACKEND

## Introduction
This is a backend services repository for SAMANA-ADMIN and SAMANA-USER apps.

## Guide to Deploy
This guide informs how to deploy all of the resources in this repository to Google Cloud Platform. All of the resources under the services directory are a REST API service to perform several tasks from mobile apps. This API is created on purpose for App Engine GCP. Each service contains 3 file:
- main.py
- service-name-app.yaml
- requirement.txt \
The main.py is the main code of the service which is written in Python with Flask web framework. requirement.txt file is the list of libraries required to run the service. To Deploy the service, move to the service directory and use the following command on cloud shell:
```
gcloud app deploy {service-name}-app.yaml
```
replace the {service-name} with the service name you want to deploy. Please refer to the [Google Cloud documentation](https://cloud.google.com/sdk/gcloud/reference/app/deploy) for more information about deployment.
