function calculate() {
    let num1 = document.getElementById("num1").value;
    let num2 = document.getElementById("num2").value;
    let operation = document.getElementById("operation").value;

    fetch(`/calculate?operation=${operation}&num1=${num1}&num2=${num2}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("result").innerText = "Error: " + data.error;
            } else {
                document.getElementById("result").innerText = data.result;
            }
        })
        .catch(error => console.log(error));
}