import random

from core.data import MessageData
from core.types import EventType

class EventHandler():
    __slots__ = ('api', 'db')

    def start(self, api, db):
        self.api = api
        self.db = db

    def initiate(self):
        '''This method will be called every time the bot is launched'''
        pass
    
    def check_event(self, event):
        '''This method checks whether the event can be processed in handler'''
        return True

    def handle_event(self, event):
        '''The method processes the event'''
        pass


class MessageHandler(EventHandler):
    __slots__ = ('permissions')

    def initiate(self):
        self.permissions = []

    def check_event(self, event):
        if event.type == EventType.MESSAGE_NEW:
            message = MessageData.from_raw(event.data)
            return self.check_message(message) and \
                    self._check_permissions(message)
        return False
    
    def handle_event(self, event):
        message = MessageData.from_raw(event.data)
        return self.handle_message(message)

    def check_message(self, message):
        '''This method checks whether the message can be processed in handler'''
        return True

    def handle_message(self, message):
        '''The method processes the message'''
        pass

    def _check_permissions(self, message):
        for permission in self._get_permissions():
            if not permission.check(message):
                return False
        return True
    
    def _get_permissions(self):
        return [permission() for permission in self.permissions]
    
    def send_message(self, to_id, **data_message):
        data = {}
        
        data['random_id'] = random.randint(-10^5, 10^5)
        data['peer_id'] = to_id

        if 'attachments' in data_message.keys():
            for attachment in data_message['attachments']:
                data['attachments'].append(attachment.get_str())
        
        if 'forwards' in data_message.keys():
            for forward_message in data_message['forwards']:
                data['forwards'].append(forward_message.id)
        
        if 'message' in data_message.keys():
            data['message'] = data_message['message']

        if 'message' in data.keys() or 'attachments' in data.keys():
            return self.api.method('messages.send', data)
        else:
            raise ValueError


class CommandHandler(MessageHandler):
    __slots__ = ('prefix', 'command', 'args_count')

    def start(self, api, db):
        super().start(api, db)
        self.prefix = ''
        self.command = ''
        self.args_count = 0
        
    def check_message(self, message):
        command, args = self._parse_command(text)
        if command == self.prefix + self.command and \
            len(args) == self.args_count:
            return True
        return False

    def handle_message(self, message):
        '''The method processes the message'''
        pass

    def _parse_command(self, text):
        command = text.split()

        if len(command) > 1:
            return (command[0], command[1:])
        else:
            return (command[0], [])