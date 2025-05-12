module "sns" {
  source = "./sns"
}

module "sqs" {
  source        = "./sqs"
  depends_on    = [module.sns]
  sns_topic_arn = module.sns.sns_topic_arn
}

# SQS registration in SNS topic
module "subscription" {
  source                  = "./subscription"
  depends_on              = [module.sqs, module.sns]
  sns_topic_arn           = module.sns.sns_topic_arn
  sqs_publisher_queue_arn = module.sqs.sqs_publisher_queue_arn
}
