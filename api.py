import json
import os
from typing import Optional, Awaitable

import tornado.ioloop
import tornado.web
import jieba.analyse as analyse


class TextRankHandler(tornado.web.RequestHandler):
    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def post(self):
        try:
            content = json.loads(self.request.body.decode('utf-8'))
            keywords = analyse.textrank(content['content'], topK=30, withWeight=True, allowPOS='n')
            output = []
            for keyword in keywords:
                output.append({"name": keyword[0], "score": keyword[1]})
            self.write(json.dumps(output))
        except json.decoder.JSONDecodeError:
            self.set_status(400)
            self.write(json.dumps({"msg": "传入格式错误"}))
            pass


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/textrank", TextRankHandler),
    ])
    port = os.environ.get('LISTEN_PORT', 8888)
    application.listen(port)
    tornado.ioloop.IOLoop.current().start()
