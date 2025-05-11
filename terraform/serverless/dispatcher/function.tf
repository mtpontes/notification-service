resource "aws_lambda_function" "notification_dispatcher" {
  function_name = "notification_dispatcher"
  handler       = "lambda_function.lambda_handler"

  role = aws_iam_role.lambda_dispatcher_role.arn

  s3_bucket = var.notification_service_source_bucket_id
  s3_key    = "${var.dispatcher_source_code_lambda_s3_zip_name}.zip"

  source_code_hash = filebase64sha256(var.dispatcher_source_code_zip)

  runtime = "python3.13"
  timeout = 60

  environment {
    variables = {
      WHATSAPP_API_TOKEN = var.whatsapp_api_token
    }
  }
}

resource "aws_cloudwatch_log_group" "dispatcher-service-lambda" {
  name              = "/aws/lambda/dispatcher-service-lambda"
  retention_in_days = 30
}