module "publisher" {
  source                                   = "./publisher"
  notification_service_source_bucket_id    = var.notification_service_source_bucket_id
  publisher_source_code_lambda_s3_zip_name = var.publisher_source_code_lambda_s3_zip_name
  publisher_source_code_zip                = var.publisher_source_code_zip
  sns_topic_arn                            = var.sns_topic_arn
  sqs_publisher_queue_arn                  = var.sqs_publisher_queue_arn
  db_username                              = var.db_username
  db_password                              = var.db_password
  db_name                                  = var.db_name
  db_port                                  = var.db_port
  db_uri                                   = var.db_uri
  db_uri_args                              = var.db_uri_args
}

module "dispatcher" {
  source                                    = "./dispatcher"
  notification_service_source_bucket_id     = var.notification_service_source_bucket_id
  dispatcher_source_code_lambda_s3_zip_name = var.dispatcher_source_code_lambda_s3_zip_name
  dispatcher_source_code_zip                = var.dispatcher_source_code_zip
  sqs_publisher_queue_arn                   = var.sqs_publisher_queue_arn
  whatsapp_api_token                        = var.whatsapp_api_token
}