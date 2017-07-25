from pony import orm
def createMessageClass(database):
    class Message(database.Entity):

        def __init__(self, text=None, message=None, sender=None):
            if text is None and message is None:
                raise ValueError("Neither text or message were passed")
            # passed only message
            # passed only text

    return Message


def createMessageClass(database):
    class Message(database.Entity):
        text=orm.Required(text)
    return Message
