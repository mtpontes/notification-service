################################ Pipeline vars #################################

# variable "publisher_service_lambda_file_zip_name" { # TF_VAR_PUBLISHER_SERVICE_LAMBDA_FILE_ZIP_NAME
variable "publisher_source_code_lambda_s3_zip_name" { # TF_VAR_PUBLISHER_SERVICE_LAMBDA_FILE_ZIP_NAME
  type = string
  default = "publisher_service"
}
variable "publisher_source_code_zip" { # workflows -> build -> build-artifacts -> strategy -> matrix -> service
  type = string
  default = "notification-publisher"
}

# variable "dispatcher_service_lambda_file_zip_name" { # TF_VAR_DISPATCHER_SERVICE_LAMBDA_FILE_ZIP_NAME
variable "dispatcher_source_code_lambda_s3_zip_name" { # TF_VAR_DISPATCHER_SERVICE_LAMBDA_FILE_ZIP_NAME
  type = string
  default = "dispatcher_service"
}
variable "dispatcher_source_code_zip" { # workflows -> build -> build-artifacts -> strategy -> matrix -> service
  type = string
  default = "notification-dispatcher"
}