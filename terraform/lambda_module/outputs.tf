output "publisher_lambda_arn" {
  value = aws_lambda_function.notification_publisher.arn
}

output "dispatcher_lambda_arn" {
  value = aws_lambda_function.notification_dispatcher.arn
}