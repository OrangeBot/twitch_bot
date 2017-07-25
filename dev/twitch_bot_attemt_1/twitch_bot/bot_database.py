from peewee import Database
from .viewer import Viewer
from .utils import fixPath


class BotDatabase(Database):
    def __init__(self, path='./'):
        path = fixPath(path)
        import os
        if os.path.isdir(path):
            path = os.path.join(path, 'bot_database.sqlite')
        # super(BotDatabase, self).__init__("sqlite", path, create_db=True)


                    createMessageClass(self)
                    # self._Message = createMessageClass(self)

                # @property
                # def Message(self):
                #     return self._Message

    @property
    def messages(self):
        pass
        # todo
        # return orm.select(self.Message)

    @property
    def viewers(self):
        pass
        # todo
        # return