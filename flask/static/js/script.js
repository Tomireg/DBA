document.addEventListener("DOMContentLoaded", init);
function init() {
    let darkModeStore = localStorage.getItem('dark-mode');

    if (darkModeStore === null) {
        localStorage.setItem("dark-mode", false);
    }
    if (darkModeStore === "true") {
        setDarkMode();
    } else {
        ;
    }

    let myButton = document.getElementById("mybtn");
    myButton.addEventListener("click", clickedDarkMode);

    let checkBox = document.getElementById("checkbox");
    checkBox.addEventListener("click", showPasswordBox);
}

function clickedDarkMode() {
    toggleDarkMode();
    setDarkMode();
}

function toggleDarkMode() {
    if (localStorage.getItem("dark-mode") === "true") {
        localStorage.setItem("dark-mode", false);

    } else {
        localStorage.setItem("dark-mode", true);
    }
}

function setDarkMode() {
    styleBody();
    styleBtn();
    styleNav();
}

function styleBody() {
    let element = document.body;
    element.classList.toggle("dark-mode");
}

function styleBtn() {
    let dmBtn = document.getElementById("mybtn");
    dmBtn.classList.toggle("dmbtn");
}

function styleNav() {
    let allButtons = document.getElementsByClassName("nav-item");
    for (let i = 0; i < allButtons.length; i++) {
        let button = allButtons[i];

        button.classList.toggle("nav-item-dark");
    }
}

function showPasswordBox(e) {
    let passwordBox = document.getElementById("password");
    if (e.target.checked) {
        passwordBox.type = "text";
    } else {
        passwordBox.type = "password";
    }
}