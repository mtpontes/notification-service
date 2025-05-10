############################### Terraform Config ###############################
provider "aws" {
  region = var.region
}

# Backend is configured with arguments via pipeline
terraform {
  backend "s3" {}
}

################################### Modules ####################################

# S3
module "s3" {
  source                                  = "./s3_module"
  publisher_service_lambda_file_zip_name  = var.publisher_service_lambda_file_zip_name
  dispatcher_service_lambda_file_zip_name = var.dispatcher_service_lambda_file_zip_name
}

# SNS & SQS
module "message_services" {
  source                                = "./message_module"
}

# Lambda
module "lambda" {
  source                                  = "./lambda_module"
  depends_on                              = [ module.s3, module.message_services ]
  notification_service_source_bucket_id   = module.s3.notification_service_source_bucket_id
  sns_topic_arn                           = module.message_services.sns_topic_arn
  publisher_service_lambda_file_zip_name  = var.publisher_service_lambda_file_zip_name
  dispatcher_service_lambda_file_zip_name = var.dispatcher_service_lambda_file_zip_name
  whatsapp_api_token                      = var.whatsapp_api_token
  db_username                             = var.db_username
  db_password                             = var.db_password
  db_name                                 = var.db_name
  db_port                                 = var.db_port
  db_uri                                  = var.db_uri
  db_uri_args                             = var.db_uri_args
}

# Event Bridge
module "event_bridge" {
  source                                = "./event_bridge"
  depends_on                            = [ module.lambda.notification_service_lambda_arn ]
  notification_service_lambda_arn       = module.lambda.notification_service_lambda_arn
}