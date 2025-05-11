resource "aws_scheduler_schedule" "notification_service_scheduler" {
  name       = "notification_service_scheduler"
  group_name = "default"

  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "cron(32 0,12 * * ? *)"

  target {
    arn      = var.lambda_function_publisher_arn
    role_arn = aws_iam_role.scheduler_lambda_role.arn
  }
}
