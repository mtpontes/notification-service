############################### S3 output vars #################################

variable "notification_service_source_bucket_id" {
  description = "Name of the bucket where the source code zip will be stored"
  type        = string
}

############################### Message output vars #################################

variable "sns_topic_arn" {
  type = string
}

variable "sqs_publisher_queue_arn" {
  type = string
}

################################ Pipeline vars #################################

variable "publisher_source_code_lambda_s3_zip_name" { # TF_VAR_PUBLISHER_SERVICE_LAMBDA_FILE_ZIP_NAME
  type    = string
  default = "publisher_service"
}
variable "publisher_source_code_zip" { # workflows -> build -> build-artifacts -> strategy -> matrix -> service
  type = string
}

variable "dispatcher_source_code_lambda_s3_zip_name" { # TF_VAR_DISPATCHER_SERVICE_LAMBDA_FILE_ZIP_NAME
  type    = string
  default = "dispatcher_service"
}
variable "dispatcher_source_code_zip" { # workflows -> build -> build-artifacts -> strategy -> matrix -> service
  type = string
}

variable "whatsapp_api_token" { # TF_VAR_WHATSAPP_API_TOKEN
  type = string
}

variable "db_username" { # TF_VAR_DB_USERNAME
  type = string
}
variable "db_password" { # TF_VAR_DB_PASSWORD
  type = string
}
variable "db_name" { # TF_VAR_DB_NAME
  type = string
}
variable "db_port" { # TF_VAR_DB_PORT
  type = string
}
variable "db_uri" { # TF_VAR_DB_URI
  type = string
}
variable "db_uri_args" { # TF_VAR_DB_URI_ARGS
  type = string
}