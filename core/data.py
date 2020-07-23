import json
import datetime


class Data():
    @classmethod
    def from_raw(cls, data):
        pass

    
class EventData(Data):
    __slots__ = ('type', 'data', 'date')

    @classmethod
    def from_raw(cls, data):
        event = cls()
        event.data = data['object']
        event.type = data['type']
        event.date = datetime.datetime.now()
        
        return event


class MessageData(Data):
    __slots__ = ('data', 'id', 'date', 'text', 'chat_id', 'user_id',
                'forwards', 'attachments')
    
    @classmethod
    def from_raw(cls, data):
        message = cls()
        message.data = data['message']
        message.id = message.data['id']
        message.date = message.data['date']
        message.text = message.data['text']
        message.chat_id = message.data['peer_id']
        message.user_id = message.data['from_id']
        
        return message
    
    @property
    def is_chat(self):
        return self.chat_id == self.user_id
    
    @property
    def has_payload(self):
        return 'payload' in self.data
    
    def get_payload(self):
        return json.loads(self.data['payload']) if self.has_payload else None

