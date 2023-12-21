const canvas = document.getElementById("canvas_entry") // snag the canvas object/element
console.log(canvas) // <canvas id='canvas_entry" ...


let c = canvas.getContext("2d")
c.font = "30px Arial"
c.fillStyle = ("black") 
c. textAlign = "center" // like translate(-50%,-50%)
c.fillText("Hello world", canvas.width / 2, canvas.height / 2) // text, x, y, max-width

// if everything ran correctly, done will be printed to the console.
console.log("done")