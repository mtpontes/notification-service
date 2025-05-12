resource "aws_lambda_permission" "publisher_allow_scheduler" {
  statement_id  = "AllowExecutionFromEventBridge"
  action        = "lambda:InvokeFunction"
  principal     = "scheduler.amazonaws.com"
  function_name = aws_lambda_function.notification_publisher.function_name
}