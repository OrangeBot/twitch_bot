from pony import orm

def fixPath(path):
    import os
    return os.path.abspath(os.path.expanduser(path))

class BotDatabase(orm.Database):
    def __init__(self, path):
        path = fixPath(path)
        import os
        if os.path.isdir(path):
            path = os.path.join(path, 'bot_database.sqlite')
        super(BotDatabase, self).__init__("sqlite", path, create_db=True)

        from message import createMessageClass
        createMessageClass(self)
        # self._Message = createMessageClass(self)

    # @property
    # def Message(self):
    #     return self._Message

    @property
    def messages(self):
        return orm.select(self.Message)
