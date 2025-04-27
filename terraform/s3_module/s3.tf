resource "aws_s3_bucket" "notification_service_source_bucket" {
  bucket = "notification_service_source_bucket"

  tags = {
    Name = "notification-service"
  }
}
