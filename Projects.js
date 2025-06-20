fetch("Projects.json")
	.then(response => {
		if (!response.ok) {
			throw new Error('Network response was not ok');
		}
		return response.json();
	})
	.then(Projects => {
		CreateCards(Projects);
	})
	.catch(error => {
		console.error('There was a problem with the fetch operation:', error);
	});

function CreateCards(Data) {
	const ProjDiv = document.querySelector("main");
	Data.forEach(function (item, i) {
		const NewCard = document.createElement("Project");

		const NewTitle = document.createElement("h3");
		TitleRU = document.createElement("ru");
		TitleRU.innerHTML = item.NameRU;
		TitleEN = document.createElement("en");
		TitleEN.innerHTML = item.NameEN;
		NewTitle.appendChild(TitleRU);
		NewTitle.appendChild(TitleEN);

		const NewDescription = document.createElement("p");
		DescriptionRU = document.createElement("ru");
		DescriptionRU.innerHTML = item.DescriptionRU;
		DescriptionEN = document.createElement("en");
		DescriptionEN.innerHTML = item.DescriptionEN;
		NewDescription.appendChild(DescriptionRU);
		NewDescription.appendChild(DescriptionEN);

		const NewLink = document.createElement("a");
		NewLink.href = item.Dir;
		NewLink.innerHTML = "<b><ru>Подробнее</ru><en>Read more</en></b>";

		const NewInfo = document.createElement("Info");
		NewInfo.appendChild(NewTitle);
		NewInfo.appendChild(NewDescription);
		NewInfo.appendChild(NewLink);

		const NewImage = document.createElement("img");
		NewImage.src = item.Image;

		NewCard.appendChild(NewInfo);
		NewCard.appendChild(NewImage);

		ProjDiv.appendChild(NewCard);
	});
}
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