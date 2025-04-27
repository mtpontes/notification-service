############################### Terraform Config ###############################
provider "aws" {
  region = var.region
}

terraform {
  backend "s3" {
    bucket = var.tfstate_bucket_name
    key    = "terraform.state"
    region = var.region
  }
}

################################### Modules ####################################

# S3
module "s3" {
  source = "./s3_module"
}

# Lambda
module "lambda" {
  source                                = "./lambda_module"
  notification_service_source_bucket_id = module.s3.notification_service_source_bucket_id
  lambda_file_zip_name                  = var.lambda_file_zip_name
  whatsapp_api_token                    = var.whatsapp_api_token
  db_username                           = var.db_username
  db_password                           = var.db_password
  db_name                               = var.db_name
  db_port                               = var.db_port
  db_uri                                = var.db_uri
  db_uri_args                           = var.db_uri_args
}