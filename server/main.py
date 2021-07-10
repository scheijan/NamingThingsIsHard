import os

import cherrypy


class NaminThingsIsHard(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"


cherrypy.tree.mount(NaminThingsIsHard(), '/', config={
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.abspath(os.path.dirname(__file__)),
        'tools.staticdir.index': 'index.html',
    },
})

cherrypy.engine.start()
