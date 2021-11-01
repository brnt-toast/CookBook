const express = require('express');


const app = express()
const port = 3000;

app.set('view engine', 'pug')


app.get('/', (req,res) =>{
    res.render('index',{title: "Home"}) // index = index.pug 
})


app.listen(port, () => {
    console.log(`Example app listening on ${port}`)
})