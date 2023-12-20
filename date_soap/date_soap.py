from spyne import Application, rpc, ServiceBase, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from datetime import date

class DateService(ServiceBase):
    @rpc(_returns=String)
    def get_date(ctx):
        return date.today().strftime("%Y-%m-%d")

application = Application([DateService],
    tns='my.date.service',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('127.0.0.1', 8000, WsgiApplication(application))
    server.serve_forever()
