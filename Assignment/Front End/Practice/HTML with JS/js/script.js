console.log(" JS loaded ")  

let originalContent = "JavaScript can change HTML content."; // Store the original content
let changedContent = "HELLO THERE CONTENT CHANGED!!"; // Changed content
let isChanged = false;

function changeData(){
    if (isChanged){
        document.getElementById('p1').innerHTML = originalContent
        document.getElementById('p1').style.textDecoration = 'none'

    }
    else{
        document.getElementById('p1').innerHTML = changedContent
        document.getElementById('p1').style.textDecoration = 'underline'
    }
    isChanged = !isChanged
}


function trigggerDocumentWriteln(){
    document.writeln("<br><br><br><h1> Using document.writeln() after an HTML document is loaded, will delete all existing HTML, <br><br><br> The document.writeln() method should only be used for testing. <br><br><br>written from script tag with doc.writeln </h1>")
}
