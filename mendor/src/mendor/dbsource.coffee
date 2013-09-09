
dbConn = require './models/dbconn'

class dbsource
	instance = undefined

	@initialize: ()->
		instance ?= new Internal()

	@uninitialize: () ->
		return

	class Internal
		constructor: () ->
			Async.series(
				(->
					dbconn.get(dbConfig.WEIBO_ROSTER_URI)
				),
				(->
					dbconn.get(dbConfig.WEIBO_MINIBLOG_URI)
				)
			)
			







module.exports = dbsource