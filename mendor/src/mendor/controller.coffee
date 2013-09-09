workermanager = require './workermanager'


class Controller
	constructor: () ->
		@routes = [
			{"/workers/keepalive/:id"      http_method: "put",         method: "keep_alive"},
			{"/worker/register",           http_method: "post",        method: "register_worker"},  
			{"/employee",                  http_method: "get",         method: "employ_worker"},
			{"/workers",                   http_method: "get",         method: "get_workers"}
		]
		@wmgr = workermanager.get()
		return

	get_workers: (req,res) ->
		
		return

	keep_alive: (req, res) ->
		return

	employ_worker: (req, res) ->
		ipaddr = (req.param.ipaddr) || -1
		if ipaddr isnt -1
			options = {
				"host": ipaddr,
				"path": "/employee"
			
			}


		else
			res.send 500, {"info","bad request"}


	register_worker: (req, res) ->
		ipaddr = req.headers['x-forwarded-for'] || req.connection.remoteAddress
		skillset = req.body.skillset || -1
		workername = req.body.workername || -1
		if skillset isnt -1 and workername isnt -1
			ret = @wmgr.register(ipaddr, skillset)
			if ret is True
				res.send 200, {"info":"success", "uid":Uuid.v4()}
			else
				res.send 300, {"info":"failed to register"}
		else
			res.send 500, {"info":"bad request"}
    
 


module.exports = Controller
