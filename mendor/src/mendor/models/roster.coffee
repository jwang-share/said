###
*the collection name is roster, in the db which is special for a site, like sina weibo
*the id is disabled, and use uid directly
###


class rosterOne
	constructor: (name) ->
		@roster_schema = @init_schema()

	insert: (users) ->
		return

	find_user_by_id: (uid) ->
		return

	find_users: (start,num) ->
		return

	update_users:(uids,items) ->
		return

	get_model:() ->
		return

	init_schema: () ->
		theschema = new Schema({
			uid: {type:String}
			fansnum: {type:Number},
			followersnum: {type:Number},
			blogsnum: {type:Number},
			userphoto: {type:String},
			usertype: {type:String},
			info: {type:String},
			usernick: {type:String},
			userhref: {type:String},
			updatetime: {type:Date, default:Date.now},
			stamptime: {type:Date},
			createtime:{type:Date},
			maxmid: {type:String},
			bloghistory:[Number]
			})
		return theschema





module.exports = rosters