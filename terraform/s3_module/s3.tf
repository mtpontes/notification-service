resource "aws_s3_bucket" "notification_service_source_bucket" {
  bucket = "notification-service-lambda-code-2"

  tags = {
    Name = "notification-service"
  }
}

resource "aws_s3_object" "lambda_zip_object" {
  bucket = aws_s3_bucket.notification_service_source_bucket.id
  key    = "${var.lambda_file_zip_name}.zip"
  source = var.code_result_zip
  etag = filemd5(var.code_result_zip)
  content_type = "application/zip"
}
