from mongoengine import Document, StringField, EmailField, ListField


class UserModel(Document):
    complete_name = StringField(required=True, unique=True)
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
    
    def __str__(self):
        return (
            f"UserModel(complete_name='{self.complete_name}', "
            f"email='{self.email}', telefone='{self.phone}', "
            f"providers={self.providers})"
        )