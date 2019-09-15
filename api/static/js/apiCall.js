
var test = document.getElementById("test")
var apiButton = document.getElementById("apiButton")
var cors = "http://127.0.0.1:8080/"
var url = "http://127.0.0.1:5000/runScript"
apiButton.addEventListener('click', function () {
    test.innerHTML = "Loading..."
    var input = document.getElementById('input').value
    runPyScript(input)
})



function runPyScript(input) {
    var jqXHR = $.ajax({
        type: "GET",
        url: url + input,
        data: '{"data":' + input + '}',
        success: function(data){
            console.log("Running this from api")
            test.innerHTML = data
        },
        error: function (){
            $.ajax({
                type: 'GET',
                url: cors+url+input,
                success: function(data){
                    console.log("Running this from local" )
                    test.innerHTML = data
                }
            })
        }
    });

    return jqXHR.responseText;
}