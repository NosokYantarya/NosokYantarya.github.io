function Lang(lang) {
	let RU = document.getElementById("RU");
	let EN = document.getElementById("EN");

	RU.style = "";
	EN.style = "";

	if (lang == "ru") {
		RU.style = "background-color: white; color: black;";
	}
	if (lang == "en") {
		EN.style = "background-color: white; color: black;";
	}

	document.querySelector("html").lang = lang;
}