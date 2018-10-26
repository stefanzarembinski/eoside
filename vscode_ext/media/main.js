// This script will be run within the webview itself
// It cannot access the main VS Code APIs directly.

const vscode = acquireVsCodeApi();

function main() {
    // Initialization work goes here.    
}

function clickHandler(e) {
    vscode.postMessage({
        title: e.target.title,
        text: e.target.textContent,
        id: e.target.id
        });
}

document.addEventListener(
    'DOMContentLoaded', 
    function () {
        var clickables = document.querySelectorAll('.clickable')
        for (var i = 0; i < clickables.length; i++) {
            clickables[i].addEventListener('click', clickHandler);
        }
    main();
  });