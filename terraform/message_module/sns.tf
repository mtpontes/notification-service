resource "aws_sns_topic" "sns_topic_serverless_notification_service" {
  name = "sns_topic_serverless_notification_service"
}

resource "aws_sqs_queue" "sqs_queue_serverless_notification_service" {
  name   = "sqs_queue_serverless_notification_service"
  policy = data.aws_iam_policy_document.sqs_queue_policy.json
}

resource "aws_sns_topic_subscription" "user_updates_sqs_target" {
  topic_arn = aws_sns_topic.sns_topic_serverless_notification_service.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.sqs_queue_serverless_notification_service.arn
}

data "aws_iam_policy_document" "sqs_queue_policy" {
  policy_id = "arn:aws:sqs:us-west-2:123456789012:user_updates_queue/SQSDefaultPolicy"

  statement {
    sid    = "UserUpdatesSQSTarget"
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["sns.amazonaws.com"]
    }

    actions = [
      "SQS:SendMessage",
    ]

    resources = [
      "arn:aws:sqs:us-west-2:123456789012:user-updates-queue",
    ]

    condition {
      test     = "ArnEquals"
      variable = "aws:SourceArn"

      values = [
        aws_sns_topic.sns_topic_serverless_notification_service.arn,
      ]
    }
  }
}