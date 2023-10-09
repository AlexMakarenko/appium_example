from jsonobject import JsonObject, IntegerProperty, StringProperty


class User(JsonObject):
    id = IntegerProperty()
    name = StringProperty()
    email = StringProperty()
    gender = StringProperty()
    status = StringProperty()

    def __eq__(self, user):
        return (
            self.name == user.name
            and self.email == user.email
            and self.gender == user.gender
            and self.status == user.status
        )
