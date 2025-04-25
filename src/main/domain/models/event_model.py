from datetime import datetime, timedelta

from mongoengine import Document, StringField, DateTimeField, ReferenceField

from src.main.domain.models.user_model import UserModel


class EventModel(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    dt_init = DateTimeField(required=True)
    dt_end = DateTimeField(required=True)
    user = ReferenceField(UserModel, required=True)

    meta = {
        'collection': 'events'
    }
    
    def get_remaining_time(self) -> timedelta:
        return self.dt_end - datetime.now()
    
    def __str__(self):
        return (
            f"EventModel(title='{self.title}', description='{self.description}', "
            f"dt_init='{self.dt_init}', dt_end='{self.dt_end}', "
            f"user='{self.user.full_name}')"
        )
