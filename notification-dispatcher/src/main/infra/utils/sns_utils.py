import json

from src.main.infra.utils.log_utils import log
from src.main.infra.constants.constants import NumberConstants, SQSConstants


class SNSUtils:
    
    @staticmethod
    def resolve_message(sns_input: dict) -> dict:
        sns_message_str: str = json.loads(sns_input[SQSConstants.RECORDS][NumberConstants.ZERO][SQSConstants.BODY])['Message']
        log.info('%s - [resolve_message] - sns message str: %s', SNSUtils.__name__, sns_message_str)

        sns_message_dict: dict = json.loads(sns_message_str)
        log.info('%s - [resolve_message] - sns message dict: %s', SNSUtils.__name__, sns_message_dict)
        return sns_message_dict