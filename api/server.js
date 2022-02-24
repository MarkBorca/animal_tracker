const express = require('express')
const cors = require('cors')
const app = express()
const port = 8000

const mongoClient = require('mongodb').MongoClient
var db = null
const url = "mongodb+srv://admin:iRBafvoVODyIbRwv@cluster0.ht8ng.mongodb.net/test"
const dbName = "AnimalTracker_db"

app.listen(port, () => {
    console.log(`Listening on port ${port}`)
})

app.use(cors())

mongoClient.connect(url, (err,client) => {
    if(err != null) {
        throw err
    }
    db = client.db(dbName)
    console.log(`Connected to ${dbName}`)
})

app.get('/env', (req, res) => {
    db.collection("environment").find().toArray((err,environmentData) => {
        if(err != null) {
            throw err
        }
        res.json(environmentData)
    })
})

app.get('/gps', (req, res) => {
    db.collection("gps").find().toArray((err,gpsData) => {
        if(err != null) {
            throw err
        }
        res.json(gpsData)
    })
})