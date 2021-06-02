# SAMANA-BACKEND

## Introduction
This is a backend services repository for SAMANA-ADMIN and SAMANA-USER apps.

## Guide to Deploy
This guide informs how to deploy all of the resources in this repository to Google Cloud Platform. All of the resources under the services directory are a REST API service to perform several tasks from mobile apps. This API is created on purpose for App Engine GCP. Each service contains 3 file:
- main.py
- service-name-app.yaml
- requirement.txt

The 'main.py' is the main code of the service which is written in Python with Flask web framework while the 'requirement.txt' file is the list of libraries required to run the service. Note that all of the API use 'firebase-admin' library to perform data read and write to the Firestore database. To set up firebase-admin inside code, a private file 'key.json' must be generated from the firebase console.
1. In the Firebase console, open **Settings > [Service Accounts](https://console.firebase.google.com/u/0/project/_/settings/serviceaccounts/adminsdk)**.
2. Click **Generate New Private Key**, then confirm by clicking **Generate Key**.
3. Securely store the JSON file containing the key.

Copy the 'key.json' to your service directory and change `cred = credentials.Certificate("path/to/serviceAccountKey.json")` inside 'main.py' with the path your generated 'key.json' stored similar to this `cred = credentials.Certificate("key.json")`.To Deploy the service, move to the service directory and use the following command on cloud shell:
```
gcloud app deploy {service-name}-app.yaml
```
Replace the `{service-name}` with the service name you want to deploy. Please refer to the [Google Cloud documentation](https://cloud.google.com/sdk/gcloud/reference/app/deploy) for more information about deployment.

## Reference
- [Set up firebase-admin](https://firebase.google.com/docs/admin/setup#python_4)
- [Deploy App Engine on Google Cloud Platform](https://cloud.google.com/sdk/gcloud/reference/app/deploy)
