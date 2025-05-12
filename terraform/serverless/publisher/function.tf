resource "aws_lambda_function" "notification_publisher" {
  function_name = "notification_publisher"
  handler       = "lambda_function.lambda_handler"

  role = aws_iam_role.lambda_publisher_role.arn

  s3_bucket = var.notification_service_source_bucket_id
  s3_key    = "${var.publisher_source_code_lambda_s3_zip_name}.zip"

  source_code_hash = filebase64sha256(var.publisher_source_code_zip)

  runtime = "python3.13"
  timeout = 60

  environment {
    variables = {
      DB_USERNAME = var.db_username
      DB_PASSWORD = var.db_password
      DB_NAME     = var.db_name
      DB_PORT     = var.db_port
      DB_URI      = var.db_uri
      DB_URI_ARGS = var.db_uri_args
      SNS_PATH    = var.sns_topic_arn
    }
  }
}

resource "aws_cloudwatch_log_group" "publisher-service-lambda" {
  name              = "/aws/lambda/publisher-service-lambda"
  retention_in_days = 30
}
