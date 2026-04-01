const hambuguer = document.querySelector(".toggle-btn");
const toggler = document.querySelector("#icon");

hambuguer.addEventListener("click", function() {
    document.querySelector("#sidebar").classList.toggle("expand");
    toggler.classList.toggle("bxs-chevrons-right");
    toggler.classList.toggle("bxs-chevrons-left");
})

new Chart(document.getElementById("bar-chart-grouped"), {
    type: 'bar',
    data: {
      labels: ["1900", "1950", "1999", "2050"],
      datasets: [
        {
          label: "Africa",
          backgroundColor: "#3e95cd",
          data: [133,221,783,2478]
        }, {
          label: "Europe",
          backgroundColor: "#8e5ea2",
          data: [408,547,675,734]
        }
      ]
    },
    options: {
      title: {
        display: true,
        text: 'Population growth (millions)'
      }
    }
});


// document.addEventListener("DOMContentLoaded", function() {
//     // Controla o menu lateral
//     const toggleButton = document.getElementById("toggleButton");
//     const sidebar = document.getElementById("sidebar");

//     toggleButton.addEventListener("click", function() {
//         sidebar.classList.toggle("hidden");
//     });

//     // Controla os submenu's
//     const componentsToggle = document.getElementById("componentsToggle");
//     const submenu = document.getElementById("submenu");
//     const submenuIconDown = submenuIcon.querySelector(".bi-chevron-compact-down");
//     const submenuIconUp = submenuIcon.querySelector(".bi-chevron-compact-up");

//     componentsToggle.addEventListener("click", function(event) {
//         event.preventDefault();

//         // Verifica se o submenu está oculto
//         const isHidden = submenu.classList.contains("max-h-0");

//         if (isHidden) {
//             // Mostra submenu
//             submenu.classList.remove("max-h-0");
//             submenu.style.maxHeight = submenu.scrollHeight + 'px'; // Define max-height
//             submenu.style.opacity = '1'; // Define a opacidade para 1
//             submenuIconDown.classList.add("hidden"); // Oculta o ícone down
//             submenuIconUp.classList.remove("hidden"); // Mostra o ícone up
//         } else {
//             // Oculta submenu
//             submenu.style.maxHeight = '0'; // Define max-height para 0
//             submenu.style.opacity = '0'; // Define a opacidade para 0

//             // Usa um timeout para adicionar a classe max-h-0 após a animação
//             setTimeout(() => {
//                 submenu.classList.add("max-h-0");
//                 submenuIconDown.classList.remove("hidden"); // Mostra o ícone down
//                 submenuIconUp.classList.add("hidden"); // Oculta o ícone up
//             }, 300); // Tempo da animação
//         }
//     });

//     $(document).ready(function () {
//         // Clona a linha do cabeçalho para adicionar os filtros
//         $('#table thead tr')
//           .clone(true)
//           .addClass('filters')
//           .appendTo('#table thead')
//           .find('th')
//           .each(function () {
//             $(this).html(''); // Limpa o conteúdo dos cabeçalhos clonados
//           });
  
//         // Inicializa a tabela com DataTables
//         const table = $('#table').DataTable({
//           paging: true,
//           searching: false,
//           ordering: true,
//           lengthChange: true,
//           orderCellsTop: true, // Mantém a ordenação no cabeçalho original
//           language: {
//             lengthMenu: "Mostrar _MENU_ registros por página",
//             zeroRecords: "Nenhum registro encontrado",
//             info: "Mostrando _START_ a _END_ de _TOTAL_ registros",
//             infoEmpty: "Mostrando 0 a 0 de 0 registros",
//             infoFiltered: "(filtrado de _MAX_ registros no total)",
//             search: "Buscar:",
//             paginate: {
//               first: "Primeiro",
//               last: "Último",
//               next: "Próximo",
//               previous: "Anterior",
//             },
//           },
//           initComplete: function () {
//             // Adiciona inputs de pesquisa para cada coluna no cabeçalho clonado
//             this.api()
//               .columns()
//               .every(function () {
//                 const column = this;
//                 const input = $(
//                   '<input type="text" placeholder="Buscar..." style="width: 100%;" />'
//                 )
//                   .appendTo($('.filters th').eq(column.index()))
//                   .on('keyup change clear', function () {
//                     if (column.search() !== this.value) {
//                       column.search(this.value).draw();
//                     }
//                   });
//               });
//           },
//         });
        
//         // Remove a funcionalidade de ordenação na linha dos inputs
//         $('.filters th').off('click.DT');
//     });
// });
