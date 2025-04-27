output "notification_service_source_bucket_id" {
  value = aws_s3_bucket.notification_service_source_bucket.id
}

output "lambda_zip_object_id" {
  value = aws_s3_object.lambda_zip_object.id
}