document.getElementsByClassName("teamBbtn")[0]; 


var selectElement = document.getElementsByClassName("dropdown-item").addEventListener("click", handleClick);

function handleClick(){
    alert("Clicked"); 
}
console.log(selectElement)
