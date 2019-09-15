
var test = document.getElementById("test")
var apiButton = document.getElementById("apiButton")
apiButton.addEventListener('click', function () {
    test.innerHTML = "Loading..."
    runPyScript("abcdefg")
})



function runPyScript(input) {
    var jqXHR = $.ajax({
        type: "GET",
        url: "http://127.0.0.1:8080/http://127.0.0.1:5000/runScript"
    });

    return jqXHR.responseText;
}