
document.querySelectorAll('.animal')[0].innerHTML = "dog";

const animals = document.getElementById("animals");

animals.innerHTML+="<li class = 'animal'>Cat</li>";

document.querySelectorAll(".box")[0].classList.add("Purple");

document.querySelectorAll(".box")[0].classList.remove("Purple");

document.querySelectorAll(".box")[0].classList.toggle("Yellow");
