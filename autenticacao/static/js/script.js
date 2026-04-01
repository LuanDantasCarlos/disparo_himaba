const container = document.getElementById('container');
const overlayCon = document.getElementById('overlayCon');
const BtnSingUp = document.getElementById('btn-sing-up');
const BtnSingIn = document.getElementById('btn-sing-in');


BtnSingUp.addEventListener('click', () => {
    container.classList.toggle('right-panel-active');
});

BtnSingIn.addEventListener('click', () => {
    container.classList.toggle('right-panel-active');
});