from Middleware.Auguma import TopicRouter

handlers = {}


def topic_handler(s):
    def _topic_handler(f):
        handlers.setdefault(s, f)
        return f
    return _topic_handler


def register_handler(router: TopicRouter):
    router.register_handler_all(handlers)