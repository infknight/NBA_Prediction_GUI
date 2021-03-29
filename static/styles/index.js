// document.getElementsByClassName("teamBbtn")[0]; 


function getname(ID_NAME){
    var x = document.getElementById(ID_NAME).value; 
    var i;
    if (ID_NAME === "teamApic"){
        i = 0;
    } else{
        i = 1; 
    }
    console.log(x)

    var picpath = "/static/images/teamlogo/" + x +".png"
    document.querySelectorAll(".teampic")[i].src = picpath;


    // if(x === "Philadelphia 76ers"){
    //     document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/philadelphia_76ers.png"
    //     console.log("76er"); 
    // }
    // if(x === "Brooklyn Nets"){

    //     console.log("nets");
    // }
}


