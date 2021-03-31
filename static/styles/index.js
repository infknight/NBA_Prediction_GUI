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


    if(x === "Philadelphia 76ers"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/Philadelphia 76ers.png";
    }
    if(x === "Brooklyn Nets"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/brooklyn_nets.png";
    }
    if(x === "Milwaukee Bucks"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/milwaukee_bucks.png";
    }
    if(x === "Charlotte Hornets"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/charlotte__hornets.png";
    }
    if(x === "New York Knicks"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/new_york_knicks.gif";
    }
    if(x === "Atlanta Hawks"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/atlanta_hawks.png";
    }
    if(x === "Boston Celtics"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/boston_celtics.png";
    }
    if(x === "Miami Heat"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/miami_heat.gif";
    }
    if(x === "Indiana Pacers"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/indiana_pacers.png";
    }
    if(x === "Chicago Bulls"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/chicago_bulls.png";
    }
    if(x === "Toronto Raptors"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/toronto_raptors.png";
    }
    if(x === "Washington Wizards"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/washington_wizards.png";
    }
    if(x === "Cleveland Cavaliers"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/cleveland_cavaliers.png";
    }
    if(x === "Orlando Magic"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/orlando_magics.gif";
    }
    if(x === "Detroit Pistons"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/detroit_pistons.png";
    }
    if(x === "Utah Jazz"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/utah_jazz.png";
    }
    if(x === "Phoenix Suns"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/phoenix_suns.png";
    }
    if(x === "LA Clippers"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/los_angeles_clippers.png";
    }
    if(x === "Los Angeles Lakers"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/lakers.png";
    }
    if(x === "Denver Nuggets"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/denver_nuggets.png";
    }
    if(x === "Portland Trail Blazers"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/portland_trail_blazers.png";
    }
    if(x === "Dallas Mavericks"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/dallas_mavericks.png";
    }
    if(x === "San Antonio Spurs"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/san_antonio_spurs.png";
    }
    if(x === "Memphis Grizzlies"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/memphis_grizzlies.png";
    }
    if(x === "Golden State Warriors"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/golden_state_warriors.png";
    }
    if(x === "Sacramento Kings"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/sacramento_kings.png";
    }
    if(x === "New Orleans Pelicans"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/new_orleans_pelicans.png";
    }
    if(x === "Oklahoma City Thunder"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/okc_thunder.png";
    }
    if(x === "Houston Rockets"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/houston_rockets.png";
    }
    if(x === "Minnesota Timberwolves"){
        document.querySelectorAll(".teampic")[i].src = "/static/images/teamlogo/minnesota_timberwolves.png";

    }
}




