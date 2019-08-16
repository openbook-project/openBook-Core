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
