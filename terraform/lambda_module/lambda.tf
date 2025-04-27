resource "aws_lambda_function" "notification_service_lambda" {
  function_name = "notification_service_lambda"
  handler       = "lambda_function.lambda_handler"

  role          = aws_iam_role.notification_service_lambda_role.arn

  s3_bucket     = var.notification_service_source_bucket_id
  s3_key        = "${var.lambda_file_zip_name}.zip"

  source_code_hash = filebase64sha256(var.code_result_zip)

  runtime       = "python3.13"
  timeout       = 60

  environment {
    variables = {
      WHATSAPP_API_TOKEN  = var.whatsapp_api_token
      DB_USERNAME         = var.db_username
      DB_PASSWORD         = var.db_password
      DB_NAME             = var.db_name
      DB_PORT             = var.db_port
      DB_URI              = var.db_uri
      DB_URI_ARGS         = var.db_uri_args
    }
  }
}


# Assume role
resource "aws_iam_role" "notification_service_lambda_role" {
  name = "notification_service_lambda_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = ["lambda.amazonaws.com"]
        }
      },
    ]
  })

  tags = {
    tag-key = "tag-value"
  }
}

# Create Role with policies
resource "aws_iam_role_policy" "notification_service_lambda_policies" {
  name = "notification_service_lambda_policies"
  role = aws_iam_role.notification_service_lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        "Effect" = "Allow",
        "Action" = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        "Resource" = "*"
      },
      {
        "Effect" = "Allow",
        "Action" = [
          "secretsmanager:GetSecretValue",
          "secretsmanager:PutSecretValue",
        ],
        "Resource" = "*"
      },
      {
        "Effect" = "Allow",
        "Action" = [
          "kms:Decrypt",
          "kms:DescribeKey"
        ],
        "Resource" = "arn:aws:kms:us-east-1:314146297418:key/40725092-7ef8-4ccb-a1b9-afd3aa4f79c3"
      }
    ]
  })
}