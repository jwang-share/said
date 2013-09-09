require "./weibominiblogs"
require "./weiboroster"


class modelfactory
	instance = undefined
	obj_arr = new Array()
	@get: () ->
		instance ?= new Internal()

	@clear: () ->
		obj_arr = null
		instance = null	

	class Internal
		custructor: () ->
			return

		create: (uri) ->
			if uri in obj_arr
				return obj_arr[uri]
			switch uri
				when 'weibo/miniblogs'
					theobj = new weibominiblogs()
					obj_arr[uri] = theobj
					return theobj				
				when 'weibo/roster'
					theobj = new weiboroster()
				else
					logger.info "type: " + uri + "is not supported"
					return null

