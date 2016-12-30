document.bes;

function validateForm(a, b, c, d) {
	var x = document.getElementById(a).value;
	var y = document.getElementById(b).value;
	var tr = true;
	if (x == "") {
        document.getElementById(c).innerHTML = "Vnesite uporabnišo ime!";
        document.getElementById(a).style.borderColor = "red";
        tr = false;
    }
    else {
        document.getElementById(c).innerHTML = "";
        document.getElementById(a).style.border= '1px solid black';
    }
    if (y == "") {
        document.getElementById(d).innerHTML = "Vnesite geslo!";
        document.getElementById(b).style.borderColor = "red";
        tr = false;
    }
    else {
        document.getElementById(d).innerHTML = "";
        document.getElementById(b).style.border= '1px solid black';
    }
    if (x != "trener" && x != "") {
        document.getElementById(c).innerHTML = "Uporabnišo ime ne obstaja!";
        document.getElementById(a).style.borderColor = "red";
        tr = false;   
    }
    else if (y != "123" && y != "" && x == "trenerjaS") {
         document.getElementById(d).innerHTML = "Geslo ni pravilno!";
        document.getElementById(b).style.borderColor = "red";
        tr = false;   
    }
    return tr;
}

function validateForm1() {
	var x1 = document.getElementById("uname3").value
	var tr = true
	if (x1 == "") {
        document.getElementById("n6").innerHTML = "Vnesite elektronski naslov!";
        document.getElementById("uname3").style.borderColor = "red";
        tr = false;
    }
    return tr;
}

function izpis() {
    var parameterName="username"
    var result = null,
        tmp = [];
    location.search
    .substr(1)
        .split("&")
        .forEach(function (item) {
        tmp = item.split("=");
        if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
    });
	document.getElementById("iz").innerHTML = result;
}

function pass() {
    var a = "uname";
    var b = "psw";
    var b1 = "psw2";
    var c = "t1";
    var d = "t2";
    var d1 = "t3";

    var x = document.getElementById(a).value;
    var y = document.getElementById(b).value;
    var z = document.getElementById(b1).value;
    var tr = true;
    if (x == "") {
        document.getElementById(c).innerHTML = "Vnesite uporabnišo ime!";
        document.getElementById(a).style.borderColor = "red";
        tr = false;
    }
    else {
        document.getElementById(c).innerHTML = "";
        document.getElementById(b1).style.border= '1px solid black';
    }
    if (y == "") {
        document.getElementById(d).innerHTML = "Vnesite geslo!";
        document.getElementById(b).style.borderColor = "red";
        tr = false;
    }
    else {
        document.getElementById(d).innerHTML = "";
        document.getElementById(b1).style.border= '1px solid black';
    }
    if (z == "") {
        document.getElementById(d1).innerHTML = "Vnesite geslo!";
        document.getElementById(b1).style.borderColor = "red";
        tr = false;
    }
    else {
        document.getElementById(d1).innerHTML = "";
        document.getElementById(b1).style.border= '1px solid black';
    }
    if (z != "" && y != "" && y != z) {
        document.getElementById(d1).innerHTML = "Gesli se ne ujema";
        document.getElementById(b1).style.borderColor = "red";
        tr = false;   
    }
    console.log(y.length)
    if(tr) {
        document.getElementById("t5").innerHTML = "Dodali ste trenerja.";
        document.getElementById(a).value = "";
        document.getElementById(b).value = "";
        document.getElementById(b1).value = "";
        tr = false;
    }
    else document.getElementById("t5").innerHTML = "";
    document.bes = x;
    return tr;
}
