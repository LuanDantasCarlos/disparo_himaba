const isDev = true; // true em hmg e false em prd


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Manipula o sideBar
function sidebarExpand(){
    const hambuguer = document.querySelector(".toggle-btn");
    const toggler = document.querySelector("#icon");

    hambuguer.addEventListener("click", function() {
        document.querySelector("#sidebar").classList.toggle("expand");
        toggler.classList.toggle("bxs-chevrons-right");
        toggler.classList.toggle("bxs-chevrons-left");
    });
}

function verificarScroll() {
    const margemTolerancia = 10; // margem para barra de tarefas e bordas

    const estaMaximizada = (
        window.innerWidth >= screen.width - margemTolerancia &&
        window.innerHeight >= screen.height - margemTolerancia
    );

    if (estaMaximizada) {
        document.body.style.overflow = 'hidden';
    } else {
        document.body.style.overflow = 'auto';
    }
}

function querySelectorCleanInput(chave) {
    const object = document.querySelector(chave);
    object.value = "";
}

function setInputValue(chave, valor) {
    const object = document.querySelector(chave);
    object.value = valor;
}

function querySelectorValueInput(chave) {
    if (querySelectorTag(".form-container")) {
        const object = document.querySelector(chave).value.trim();
        return object;
    }
}

function querySelectorTag(chave) {
    const object = document.querySelector(chave)
    return object;
}

function ternarioValue(valor) {
    return valor ? valor : null;
}

function getQueryParamUrl(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}
