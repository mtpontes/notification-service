resource "aws_sqs_queue_policy" "allow_sns" {
  queue_url = aws_sqs_queue.sqs_queue_serverless_notification_service.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Sid    = "Allow-SNS-SendMessage",
        Effect = "Allow",
        Principal = {
          Service = "sns.amazonaws.com"
        },
        Action   = "sqs:SendMessage",
        Resource = aws_sqs_queue.sqs_queue_serverless_notification_service.arn,
        Condition = {
          ArnEquals = {
            "aws:SourceArn" = var.sns_topic_arn
          }
        }
      }
    ]
  })
}
