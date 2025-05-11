resource "aws_sns_topic_subscription" "user_updates_sqs_target" {
  topic_arn = var.sns_topic_arn
  protocol  = "sqs"
  endpoint  = var.sqs_publisher_queue_arn
}
