function strip_ending_pre_whitespace(pre) {
	var i = pre.innerText.length-1;
	while (pre.innerText[i] == "\t" || pre.innerText[i] == " " || pre.innerText[i] == "\n") {
		pre.innerText = pre.innerText.substring(0, i);
		i--;
	}
}

function count_newlines(pre) {
	var count = 0;
	for (var i = 0; i < pre.innerText.length; i++)
		if (pre.innerText[i] == "\n") count++;
	return count;
}

function fill_line_numbers(pre, n) {
	for (var i = 0; i < n; i++)
		pre.innerText += i + "\n";
}

function number_code_blocks(code_blocks) {
	for (var i = 0; i < code_blocks.length; i++) {
		var lines = code_blocks[i].children[0];
		var code = code_blocks[i].children[1];
		var no_lines = 0;
		for (var j = 0; j < code.innerText.length; j++) {
			if (code.innerText[j] == "\n") {
				lines.innerText += no_lines + "\n";
				no_lines++;
			}
		}
		lines.innerText += no_lines + "\n";
	}

}

document.addEventListener("DOMContentLoaded",  function() {
		var codeblocks = document.querySelectorAll(".code-block");
		for (var i = 0; i < codeblocks.length; i++)
			strip_ending_pre_whitespace(codeblocks[i].querySelectorAll("pre")[1]);
		number_code_blocks(codeblocks);
});
