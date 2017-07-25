from peewee import Model, CharField, DateTimeField

class ChatRecord(Model):
    text = CharField()
    timestamp = DateTimeField()

    @classmethod
    def bind(cls, database):
        class Meta:
            database = database
        cls.Meta = Meta


class Message(ChatRecord)
