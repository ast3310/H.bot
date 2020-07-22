from core.handlers import MessageHandler

class ExampleHandler(MessageHandler):
    def initiate(self):
        self.permissions = []

    def check_message(self, message):
        if message.text == 'Test':
            return True
    
    def handle_message(self, message):
        self.send_message(message.user_id, message='Test message')