from mongoengine import Document, StringField, DateTimeField, ObjectIdField


class EventModel(Document):
    id = ObjectIdField(primary_key=True)
    title = StringField(required=True)
    description = StringField(required=True)
    dt_init = DateTimeField(required=True)
    dt_end = DateTimeField(required=True)
    user = ObjectIdField()

    meta = {
        'collection': 'events'
    }