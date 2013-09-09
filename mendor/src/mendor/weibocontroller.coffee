
#involve long polling to make monitot much easier
sessionmanager = require './sessionmanager'
http = require 'http'

class WeiboController
	constructor: () ->
		@route = [
			{"/weibo/:id/start",                http_method: "put",      method: "start_work"},
			{"/weibo/:id/stop",                 http_method: "put",      method: "stop_work"},
			{"/weibo/followers/results/:id",    http_method: "post",     method: "handle_fl_results"},
			{"/weibo/miniblogs/results/:id",    http_method: "post",     method: "handle_mb_results"},
			{"/weibo/followers/failure/:id",    http_method: "post",     method: "handle_fl_failure"},
			{"/weibo/miniblogs/failure/:id",    http_method: "post",     method: "handle_mb_failure"},
			{"/weibo/followers/error/:id",      http_method: "get",     method: "handle_fl_error"},
			{"/weibo/miniblogs/error/:id",      http_method: "get",     method: "handle_mb_error"}

		]
		@ssmgr = new sessionmanager()
		return

     #front-end should check the parameters to lighten the work of back-end
	start_work: (req, res) ->
		id = req.param.id
		ipaddr = (req.body.ipaddr) || 0
		task = (req.body.task) || 0
		


		return

	stop_work: (req, res) ->
		return

	handle_fl_results: (req, res) ->
		return

	handle_mb_results: (req, res) ->
		return

	handle_fl_failure: (req, res) ->
		return

	handle_mb_failure: (req, res) ->
		return

	handle_fl_error: (req, res) ->
		return

	handle_mb_error: (req, res) ->
		return


