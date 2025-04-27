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
  source                = "./s3_module"
  lambda_file_zip_name  = var.lambda_file_zip_name
  code_result_zip       = var.code_result_zip
}

# Lambda
module "lambda" {
  source                                = "./lambda_module"
  depends_on                            = [ module.s3.lambda_zip_object_id ]
  notification_service_source_bucket_id = module.s3.notification_service_source_bucket_id
  code_result_zip                       = var.code_result_zip
  lambda_file_zip_name                  = var.lambda_file_zip_name
  whatsapp_api_token                    = var.whatsapp_api_token
  db_username                           = var.db_username
  db_password                           = var.db_password
  db_name                               = var.db_name
  db_port                               = var.db_port
  db_uri                                = var.db_uri
  db_uri_args                           = var.db_uri_args
}

module "event_bridge" {
  source                          = "./event_bridge"
  depends_on                      = [ module.lambda.notification_service_lambda_arn ]
  notification_service_lambda_arn = module.lambda.notification_service_lambda_arn
}