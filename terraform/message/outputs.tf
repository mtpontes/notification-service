output "sns_topic_arn" {
  value = module.sns.sns_topic_arn
}

output "sqs_publisher_queue_arn" {
  value = module.sqs.sqs_publisher_queue_arn
}