resource "aws_sqs_queue" "sqs_queue_serverless_notification_service" {
  name                       = "sqs_queue_serverless_notification_service"
  visibility_timeout_seconds = 60
}
