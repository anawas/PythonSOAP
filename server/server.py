"""
http://spyne.io/docs/2.10/manual/02_helloworld.html

"""
from spyne.application import Application
from spyne.decorator import srpc
from spyne.service import ServiceBase, ServiceBaseBase
from spyne.model.complex import Iterable
from spyne.model.primitive import UnsignedInteger
from spyne.model.primitive import String
from spyne.server.wsgi import WsgiApplication
from spyne.protocol.soap import Soap11, Soap12
from wsgiref.simple_server import make_server

class GoodbyeWorldService(ServiceBase):
    @srpc(String, _returns=String)
    def say_goodbye(name):
        return 'Goodbye, %s' % name

class HelloWorldService(ServiceBase):
    @srpc(String, UnsignedInteger, _returns=Iterable(String))
    def say_hello(name, times):
        for i in range(times):
            yield 'Hello, %s' % name

if __name__ == '__main__':
    import logging

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    app = Application([HelloWorldService, GoodbyeWorldService], 
        'spyne.examples.hello.http',
        in_protocol=Soap12(validator='lxml'),
        out_protocol=Soap12())

    wsgi_app = WsgiApplication(app)
    server = make_server('127.0.0.1', 7789, wsgi_app)
    print("Listening to 127.0.0.1:7789")
    print("wsdl is at: http://localhost:7789/?wsdl")
    server.serve_forever()

    


