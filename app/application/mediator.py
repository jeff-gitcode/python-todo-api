class Mediator:
    def __init__(self):
        self._handlers = {}

    def register(self, request_type, handler):
        self._handlers[request_type] = handler

    def send(self, request):
        handler = self._handlers.get(type(request))
        if not handler:
            raise ValueError(f'No handler registered for {type(request)}')
        return handler.handle(request)