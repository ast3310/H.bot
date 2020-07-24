class EventControler():
    def __init__(self, handlers, api, db):
        self.handlers = handlers
        self.api = api
        self.db = db

        self._starting_handlers()
        self._initaite_handlers()
        
    def recognition(self, event):
        for handler in self.handlers:
            if handler.check_event(event) is True:
                return handler.handle_event(event)
    
    def _initaite_handlers(self):
        for handler in self.handlers:
            handler.initiate()
    
    def _starting_handlers(self):
        for handler in self.handlers:
            handler.start(self.api, self.db)
