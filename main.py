import os.path
import pymongo
import motor
import jwt


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


import profile


from tornado.options import define,options
define("port",default=8000,help="port addr",type=int)


MONGODB_URI = "mongodb://four:four@ds045882.mongolab.com:45882/pyjwt"

#handles the main class for configuration settings
class Application(tornado.web.Application):
	def __init__(self):
		handlers=[
		(r'/',profile.IndexHandler),
		(r'/register',profile.RegisterHandler),
		(r'/login',profile.LoginHandler),
		
		(r'/logout',profile.LogoutHandler)
				]
		settings=dict(
			template_path=os.path.join(os.path.dirname(__file__),"templates"),
			static_path=os.path.join(os.path.dirname(__file__),"static"),
			assets_path=os.path.join(os.path.dirname(__file__),"assets"),
			cookie_secret="Djsjdjikzxmnlkjuf&4nlDIOFSJ943qqjkj09",
			xsrf_cookies=True,
			debug=True,
			login_url='/login'
			)
		client1=pymongo.MongoClient(MONGODB_URI)
		client=motor.MotorClient(MONGODB_URI)
		self.db1=client1.pyjwt
		self.db=client.pyjwt
		tornado.web.Application.__init__(self,handlers,**settings)

if __name__=="__main__":
	tornado.options.parse_command_line()
	http_server=tornado.httpserver.HTTPServer(Application(),xheaders=True)
	http_server.listen(options.port  )
	tornado.ioloop.IOLoop.instance().start()
