
function changeImage() {
	document.getElementById("img1").src= "../img/" + document.getElementById("fl").files[0].name;	
   	document.getElementById("slik").innerHTML = "Uspešno ste zamenjali sliko."
}

function izpisiObvestilo(a, b) {
	if (document.getElementById(a).value == "") {
		document.getElementById(b).style.color = "red";
		document.getElementById(b).innerHTML = "Vpisite obvestilo.";
		document.getElementById(a).style.borderColor = "red";
		return false;
	}
	else {
		document.getElementById(b).style.color = "black";
		document.getElementById(a).style.borderColor = "black";
		document.getElementById(b).innerHTML = "Dodali ste obvestilo.";
		console.log(document.getElementById(a).value);
		document.getElementById(a).value = "";
		return false;
	}
}