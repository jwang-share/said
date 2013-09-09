
controller = require './controller'
weibocontroller = require './weibocontroller'



class controllerrepo
	instance = undefined
	
	@get_all_controllers: () ->
		instance ?= new Internal()
		ctrlers = instance.get_all_controllers()
		return ctrlers

	class Internal
		constructor: ()->
			@basic_controller = new controller()
			@weibo_controller = new weibocontroller()

		get_all_controllers: () ->
			return [
				@basic_controller,
				@weibo_controller
			]
