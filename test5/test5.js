function toggle(element){
	let obj =  document.getElementById(element);
	obj.style.display = obj.style.display === 'none' ? 'block' : 'none';
}

let x_offset = 0;
let y_offset = 0;

function beginDrag(e){
	let init = e.target;
	x_offset = e.clientX - init.style.left.substr(0, init.style.left.length - 2);
	y_offset = e.clientY - init.style.top.substr(0, init.style.top.length - 2);
}
function endDrag(e){
	let obj = e.target.parentNode;
	obj.style.left = String(e.clientX - x_offset) + "px";
	obj.style.top = String(e.clientY - y_offset) + "px";
}

function dragstart_handler(e) {
	e.dataTransfer.setData("text/plain", e.target.innerText);
}
