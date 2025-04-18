document.addEventListener("DOMContentLoaded", function() {
    // Your code here
    enable_translate();
});

function enable_translate() {
	document.getElementById("switch-language").addEventListener("click", function(e) {
		document.querySelectorAll("[t]").forEach(node => {
			var original_text = node.innerText;
			node.innerText = node.getAttribute("t");
			node.setAttribute("t", original_text);
		});
	});
}