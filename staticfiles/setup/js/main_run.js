document.addEventListener("DOMContentLoaded", () => {
    sidebarExpand();
    // Verifica ao carregar
    window.addEventListener('load', verificarScroll);

    // Verifica quando redimensionar a janela
    window.addEventListener('resize', verificarScroll);
});
