################################### Modules ####################################

# S3
module "bucket" {
  source = "./bucket"

  # Source code
  publisher_source_code_lambda_s3_zip_name  = var.publisher_source_code_lambda_s3_zip_name
  dispatcher_source_code_lambda_s3_zip_name = var.dispatcher_source_code_lambda_s3_zip_name
  publisher_source_code_zip                 = var.publisher_source_code_zip
  dispatcher_source_code_zip                = var.dispatcher_source_code_zip
}

# SNS & SQS
module "message" {
  source = "./message"
}

# Lambdas
module "serverless" {
  source     = "./serverless"
  depends_on = [module.bucket, module.message]

  # Dependencies
  notification_service_source_bucket_id = module.bucket.notification_service_source_bucket_id
  sns_topic_arn                         = module.message.sns_topic_arn
  sqs_publisher_queue_arn               = module.message.sqs_publisher_queue_arn

  # Source code
  publisher_source_code_lambda_s3_zip_name  = var.publisher_source_code_lambda_s3_zip_name
  dispatcher_source_code_lambda_s3_zip_name = var.dispatcher_source_code_lambda_s3_zip_name
  publisher_source_code_zip                 = var.publisher_source_code_zip
  dispatcher_source_code_zip                = var.dispatcher_source_code_zip

  # Database
  db_username = var.db_username
  db_password = var.db_password
  db_name     = var.db_name
  db_port     = var.db_port
  db_uri      = var.db_uri
  db_uri_args = var.db_uri_args

  # Integration
  whatsapp_api_token = var.whatsapp_api_token
}

# Event Bridge
module "event_bridge" {
  source     = "./scheduler"
  depends_on = [module.serverless.lambda_function_publisher_arn]

  # Dependencies
  lambda_function_publisher_arn = module.serverless.lambda_function_publisher_arn
}
