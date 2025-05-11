resource "aws_lambda_event_source_mapping" "sqs_trigger" {
  event_source_arn = var.sqs_publisher_queue_arn
  function_name    = aws_lambda_function.notification_dispatcher.function_name
}