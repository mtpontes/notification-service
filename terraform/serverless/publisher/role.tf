# Assume role
resource "aws_iam_role" "lambda_publisher_role" {
  name = "lambda_publisher_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
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
resource "aws_iam_role_policy" "lambda_publisher_policies" {
  name = "lambda_publisher_policies"
  role = aws_iam_role.lambda_publisher_role.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        "Sid"    = "CloudWatchIntegration"
        "Effect" = "Allow",
        "Action" = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        "Resource" = "*"
      },
      {
        "Sid"    = "SecretManagerIntegration"
        "Effect" = "Allow",
        "Action" = [
          "secretsmanager:GetSecretValue",
          "secretsmanager:PutSecretValue",
        ],
        "Resource" = "*"
      },
      {
        "Sid"    = "KMSPolicies"
        "Effect" = "Allow",
        "Action" = [
          "kms:Decrypt",
          "kms:DescribeKey"
        ],
        "Resource" = "*"
      },
      {
        "Sid"    = "SQSIntegration"
        "Effect" = "Allow",
        "Action" = [
          "sqs:ReceiveMessage",
          "sqs:DeleteMessage",
          "sqs:GetQueueAttributes"
        ],
        "Resource" = "*"
      },
      {
        "Sid" : "SNSPublishAccess",
        "Effect" : "Allow",
        "Action" : [
          "sns:Publish"
        ],
        "Resource" : "${var.sns_topic_arn}"
      }
    ]
  })
}
