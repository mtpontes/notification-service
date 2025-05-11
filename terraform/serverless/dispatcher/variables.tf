############################### S3 output vars #################################

variable "notification_service_source_bucket_id" {
  description = "Name of the bucket where the source code zip will be stored"
  type        = string
}

############################### Message output vars #################################

variable "sqs_publisher_queue_arn" {
  type = string
}

################################ Pipeline vars #################################

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
