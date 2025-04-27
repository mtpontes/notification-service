############################### S3 output vars #################################

variable "notification_service_source_bucket_id" {
  description = "Nome do bucket onde o zip do código fonte será armazenado"
  type        = string
}

################################ Pipeline vars #################################

variable "lambda_file_zip_name" { # Pipeline env TF_VAR_LAMBDA_FILE_ZIP_NAME
  description = "Nome do arquivo ZIP da Lambda"
  type        = string
}

variable "whatsapp_api_token" { # TF_VAR_WHATSAPP_API_TOKEN
  type        = string
}

variable "db_username" { # TF_VAR_DB_USERNAME
  type        = string
}
variable "db_password" { # TF_VAR_DB_PASSWORD
  type        = string
}
variable "db_name" { # TF_VAR_DB_NAME
  type        = string
}
variable "db_port" { # TF_VAR_DB_PORT
  type        = string
}
variable "db_uri" { # TF_VAR_DB_URI
  type        = string
}
variable "db_uri_args" { # TF_VAR_DB_URI_ARGS
  type        = string
}