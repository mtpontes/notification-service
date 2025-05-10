resource "aws_s3_bucket" "notification_service_source_bucket" {
  bucket = "notification-service-lambda-code-2"

  tags = {
    Name = "notification-service"
  }
}

resource "aws_s3_object" "publisher_lambda_zip_object" {
  bucket = aws_s3_bucket.notification_service_source_bucket.id
  key    = "${var.publisher_service_lambda_file_zip_name}.zip"
  source = "${var.publisher_service_lambda_file_zip_name}.zip"
  etag = filemd5("${var.publisher_service_lambda_file_zip_name}.zip")
  content_type = "application/zip"
}

resource "aws_s3_object" "dispatcher_lambda_zip_object" {
  bucket = aws_s3_bucket.notification_service_source_bucket.id
  key    = "${var.dispatcher_service_lambda_file_zip_name}.zip"
  source = "${var.dispatcher_service_lambda_file_zip_name}.zip"
  etag = filemd5("${var.dispatcher_service_lambda_file_zip_name}.zip")
  content_type = "application/zip"
}
