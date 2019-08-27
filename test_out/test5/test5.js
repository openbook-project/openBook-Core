function toggle(element){
	let obj =  document.getElementById(element);
	obj.style.display = obj.style.display === 'none' ? 'block' : 'none';
}

let x_offset = 0;
let y_offset = 0;

function beginDrag(e){
	x_offset = e.clientX
	y_offset = e.clientY
}
function endDrag(e){
	let obj = e.target.parentNode;
	let x = x_offset - e.clientX;
	let y = y_offset - e.clientY;
	obj.style.left = (obj.offsetLeft - x) + "px";
	obj.style.top = (obj.offsetTop - y) + "px";
}


function dragstart_handler(e) {
	e.dataTransfer.setData("text/plain", e.target.innerText);
}
function moveToPosition(e, element){
	let obj = document.getElementById(element);
	obj.style.left = e.pageX + 'px';
	obj.style.top = e.pageY + 'px';
}
document.addEventListener('DOMContentLoaded', function() {
	menuLeft = document.getElementById( 'navbar' );
	body = document.body;
	showLeft = document.getElementById( 'showLeft' );
	menuLeft.style.left = "-500px";
	var dropdown = document.getElementsByClassName("dropdown-btn");
	var i;
	for (i = 0; i < dropdown.length; i++) {
		dropdown[i].addEventListener("click", function() {
		this.classList.toggle("active");
		var dropdownContent = this.nextElementSibling;
		dropdownContent.style.display = dropdownContent.style.display === "none" ? "block" : "none";		});
	}
});

function toggleNavBar(){
	menuLeft.style.left = menuLeft.style.left == "0px" ? "-500px" : "0px";
}
