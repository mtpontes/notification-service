resource "aws_s3_object" "publisher_service_object" {
  bucket        = aws_s3_bucket.notification_service_source_bucket.id
  key           = "${var.publisher_source_code_lambda_s3_zip_name}.zip"
  source        = var.publisher_source_code_zip
  etag          = filemd5(var.publisher_source_code_zip)
  content_type  = "application/zip"
}

resource "aws_s3_object" "dispatcher_service_object" {
  bucket        = aws_s3_bucket.notification_service_source_bucket.id
  key           = "${var.dispatcher_source_code_lambda_s3_zip_name}.zip"
  source        = var.dispatcher_source_code_zip
  etag          = filemd5(var.dispatcher_source_code_zip)
  content_type  = "application/zip"
}