let text = 'I love you !!!';
function save(text) {
    var link = document.createElement('a');
    link.href = 'data:text/plain;charset=UTF-8,' + escape(text);
    link.download = 'output.txt';
    link.click();
}