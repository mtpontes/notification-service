resource "aws_iam_role" "scheduler_lambda_role" {
  name = "scheduler_lambda_role"
  
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "scheduler.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "scheduler_lambda_policy" {
  name = "scheduler_lambda_policy"
  role = aws_iam_role.scheduler_lambda_role.id
  
  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = [
          "lambda:InvokeFunction"
        ],
        Resource = var.notification_service_lambda_arn
      }
    ]
  })
}

resource "aws_scheduler_schedule" "notification_service_scheduler" {
  name       = "notification_service_scheduler"
  group_name = "default"

  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "rate(12 hours)"

  target {
    arn      = var.notification_service_lambda_arn
    role_arn = aws_iam_role.scheduler_lambda_role.arn
  }
}