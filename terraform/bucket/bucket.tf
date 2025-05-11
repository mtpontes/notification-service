resource "aws_s3_bucket" "notification_service_source_bucket" {
  bucket = "notification-service-lambda-code"

  tags = {
    Name = "notification-service"
  }
}
