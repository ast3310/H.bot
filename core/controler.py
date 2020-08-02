class EventControler():
    __slots__ = ('handlers', 'api', 'db', 'logger')

    def __init__(self, handlers, api, db, logger):
        self.handlers = handlers
        self.api = api
        self.db = db
        self.logger = logger

        self._starting_handlers()
        self._initaite_handlers()
        
    def recognition(self, event):
        for handler in self.handlers:
            if handler.check_event(event) is True:
                self.logger.info('Handling: {}'.format(handler.name))
                return handler.handle_event(event)
    
    def _initaite_handlers(self):
        self.logger.info('Initaite handlers')

        for handler in self.handlers:
            handler.initiate()
    
    def _starting_handlers(self):
        self.logger.info('Starting handlers')

        for handler in self.handlers:
            handler.start(self.api, self.db, self.logger)
