###
* use uid as the collection name
* the collection is in the db which special for a site, like sina weibo
* I don't want to make the db too complicated, so all miniblogs should follow the 
*    the same schema
###

class blogOne
	constructor: (name) ->
		@miniblog_schema = @init_schema()
		@name = name

	find_blog_by_id: (uid,id,fields,callback) ->
		themodel = @get_model(uid)
		callback ?= null
		themodel.find()
		.sort('-timestamp')
		.select(fields)
		.exec(callback)

	find_blogs_by_uid1: (uid,start,num,callback) ->
		themodel = @get_model(uid)
		callback ?= null
		themodel.find()
		.sort('-timestamp')
		.skip(start)
		.limit(num)
		.exec(callback)
		return

	find_blogs_by_uid2: (uid,mid,gt,callback) ->
		themodel = @get_model(uid)
		callback ?= null
		themodel.find()
		.sort('-mid')
		.gt(mid)
		.exec(callback)

	find_blogs_by_uid3: (uid,mid1,mid2,callback) ->
		#
		return

	insert_blogs:(uid,blogs) ->
		themodel = @get_model(uid)
		themodel.create(blogs,(err)->
			if err?
				logger.info "insert_blogs: " + err
			)

	delete_blog_by_id:(uid,id) ->
		return

	delete_blog_by_uid:(uid) ->
		return

    #must be overwrite by its subclass
	get_model:(uid) ->
		collectobj = mongoose.model(uid,@miniblog_schema)
		return collectobj

    #ow by needs
	init_schema: () ->
		theschema = new Schema({
			mid: {type:String},
			timestamp: {type:Date},
			imgs: [String],
			medias: [String]
			})
		return theschema










module.exports = miniBlogs