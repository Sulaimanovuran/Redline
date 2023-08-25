import cherrypy
from main import app as flask_app

class Gateway(object):
    @cherrypy.expose
    def default(self, *args, **kwargs):
        # Передаем все входящие запросы в Flask-приложение
        return flask_app(*args, **kwargs)

if __name__ == '__main__':
    cherrypy.quickstart(Gateway(), '/', {
        'global': {
            'server.socket_host': '0.0.0.0',  # Чтобы ваше приложение было доступно извне
            'server.socket_port': 5000  # Порт, на котором будет работать CherryPy
        }
    })
