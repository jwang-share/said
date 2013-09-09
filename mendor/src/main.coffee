require './mendor/config'

console.log "main...."
console.log "mendor"

#connect to database before starting server
datasource = './mendor/dbsource'
datasource.initialize()

#start server
Server = require './mendor/server'
new Server().start()