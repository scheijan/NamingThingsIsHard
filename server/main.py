import cherrypy


class NaminThingsIsHard(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"


cherrypy.quickstart(NaminThingsIsHard())
