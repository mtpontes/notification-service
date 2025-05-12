output "sqs_publisher_queue_arn" {
  value = aws_sqs_queue.sqs_queue_serverless_notification_service.arn
}
