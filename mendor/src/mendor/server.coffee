express         = require 'express'
querystring     = require 'querystring'
Controllers  = require('./controllerrepo')


class Server
	constructor: () ->
		@app = express()
		@ctrlers = new Controllers.get_all_controllers()
		@configure(@app)

	configure: (app) ->
		app.configure () ->
			app.use(express.cookieParser())
			app.use(express.bodyParser())
			app.use(express.methodOverride())
			app.use(app.router)
			app.use(express.static(__dirname + '/../../public'))
			app.use(express.errorHandler({ dumpExceptions: true, showStack: true }))
			app.set('views',__dirname + '/../../views')
			app.set('view engine', 'ejs')
			return

	self = this

	for ctrler in @ctrlers
		for api in ctrler.routes
			do (api) ->
				fn_handler = (req, res) ->
					try
						self.ctrler[api.method](req, res)
					catch e
						res.json(error)
				app[api.http_method](api.path, fn_handler)
				logger.info("route: #{api.http_method.toUpperCase()} #{api.path} => #{api.method}")
				

	start: (port=config.LISTEN_PORT) ->
		@app.listen(port)
		logger.info "Server is listening to #{port}"


module.exports = Server
