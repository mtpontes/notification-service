from mongoengine import Document, StringField, EmailField, ListField, ObjectIdField


class UserModel(Document):
    id = ObjectIdField(primary_key=True)
    full_name = StringField(required=True, unique=True)
    email = EmailField(required=False, unique=True)
    phone = StringField(required=False, unique=True)
    providers = ListField(StringField(), required=False)


    meta = {
        'collection': 'users',
        'indexes': [
            {
                'fields': ['email'],
                'unique': True
            },
            {
                'fields': ['phone'],
                'unique': True
            }
        ]
    }