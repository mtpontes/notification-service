import os

import boto3

from src.main.infra.utils.log_utils import log
from src.main.application.mapper import Mapper
from src.main.domain.models.user_model import UserModel
from src.main.domain.models.event_model import EventModel
from src.main.business.publisher.publisher_i import PublisherI
from src.main.infra.utils.publisher_utils import PublisherUtils
from src.main.application.dto import EventDispatcherDTO, UserDispatcherDTO
from src.main.infra.providers.notificarion_provider_enum import NotificationProviderEnum


class SNSPublisherImpl(PublisherI):
    def __init__(self):
        self.sns_client = boto3.client('sns', region_name='us-east-1')
        self.sns_arn = os.getenv('SNS_PATH')
        self.mapper = Mapper()

    def publish(self, events: list[EventModel], user: UserModel, provider: NotificationProviderEnum) -> None:
        log.info('%s - [publish] - Start', self.__class__.__name__)
        
        message: str = self._prepare_message(events, user, provider)
        response = self.sns_client.publish(TopicArn=self.sns_arn, Message=message) 
        
        log.info('SNS response: %s', str(response))
        log.info('%s - [publish] - End', self.__class__.__name__)

    def _prepare_message(self, events: list[EventModel], user: UserModel, provider: NotificationProviderEnum) -> str:
        user_dict: UserDispatcherDTO = self.mapper.to_UserDispatcherDTO(user)
        event_dict_list: list[EventDispatcherDTO] = self.mapper.to_EventOutputDTO_list(events)
        message: str = PublisherUtils.create_message(provider, event_dict_list, user_dict)
        
        log.info('%s - [_prepare_message] - Prepared message: %s', self.__class__.__name__, message)
        return message
