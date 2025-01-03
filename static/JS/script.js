let testValue = true

function test(){
    if (testValue){
        document.getElementById("test").innerText = "Hello World!"
        testValue = false
    } else{
        document.getElementById("test").innerText = "test"
        testValue = true
    }

}