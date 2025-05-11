# Serverless Notification Service

This is a notification system, however, each registered user can specify which (supported) providers they want to notify them.

The system is completely open to the creation of new notification providers; by respecting the required data structure and implementing only one interface, it is possible to increase/decrease notification providers without the need to make major adjustments to the base code.

## System overview

![application-schema](/assets/application.svg)

## Tecnologies

### Tools
- Python 3.13
- MongoDB
- AWS S3
- AWS Lambda
- AWS Event Bridge

### Optional tools
- AWS Secret Manager: Used for provider Google Calendar, what a need for user credentials. The tool is optional as all provider is optional.

### Infra & CI/CD
- AWS
- Terraform
- Github Actions

<details>
    <summary><h2>Details</h2></summary>

### Data Structures (models e MongoDB collections)

#### User:
``` python
full_name: str
email: str
phone: str
providers: list[str]
```

#### Event:
``` python
title: str
description: str
dt_init: datetime
dt_end: datetime
user: User
```

</details>

<details>
  <summary><h2>How to run</h2></summary>

### Prerequisites
- AWS access key (third party service)
- AWS CLI
- Terraform

### AWS Roles/Policies

Roles used:
- AmazonEventBridgeFullAccess
- AmazonS3FullAccess
- AmazonSNSFullAccess
- AmazonSQSFullAccess
- AWSLambda_FullAccess
- CloudWatchLogsFullAccess
- iam:*

<details>
    <summary><h3>Envs</h3></summary>

#### Lambda - Publisher:
```.env
# Database
DB_USERNAME
DB_PASSWORD
DB_NAME
DB_PORT
DB_URI
DB_URI_ARGS # Opcional

# AWS
SNS_PATH
```

#### Lambda - Dispatcher:
```.env
# API token
WHATSAPP_API_TOKEN
```

#### Pipeline vars/secrets:
```
# Vars
REGION
TFSTATE_BUCKET_NAME

# Secrets
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY

DB_NAME
DB_PASSWORD
DB_PORT
DB_URI
DB_URI_ARGS
DB_USERNAME

WHATSAPP_API_TOKEN
```

#### Terraform envs:
``` .env
TF_LOG
TF_VAR_publisher_source_code_zip
TF_VAR_dispatcher_source_code_zip
TF_VAR_publisher_source_code_lambda_s3_zip_name
TF_VAR_dispatcher_source_code_lambda_s3_zip_name
TF_VAR_region
TF_VAR_tfstate_bucket_name
TF_VAR_whatsapp_api_token
TF_VAR_db_username
TF_VAR_db_password
TF_VAR_db_name
TF_VAR_db_port
TF_VAR_db_uri
TF_VAR_db_uri_args
```
</details>


<details>
  <summary><h3>Implementation step by step</h3></summary>

> **IMPORTANT** \
> Configure all necessary envs (Terraform envs)

#### Build
Generate an application zip along with all dependencies at the same level as the `` src`` directory.
```bash
python -m pip install --upgrade pip
mkdir package
pip install -r requirements.txt -t package/
cp -r src package/
cp lambda_function.py package/

cd package
zip -r "../source_code.zip" . # Remember to assign the same name in the environment variable TF_VAR_code_result_zip
cd ..
```
#### Terraform
1. Create a bucket for the Terraform state file and set its name to the ``TF_VAR_tfstate_bucket_name`` environment variable

2. Configure all environment variables

3. Init
    ```bash
    terraform init \
        -backend-config="bucket=$TF_VAR_tfstate_bucket_name" \
        -backend-config="key=terraform.state" \
        -backend-config="region=$TF_VAR_region"
    ```

4. Valide
    ```terraform
    terraform validate
    ```

5. Plan
    ```terraform
    terraform plan
    ```

6. Apply
    ```terraform
    terraform apply
    ```
</details>

</details>