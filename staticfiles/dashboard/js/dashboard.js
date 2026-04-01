let table = null;


function dataTableAtendimentos() {
    fetch('/dashboard/dados-broadcasts/')
        .then(response => response.json())
        .then(data => {
            // Preenche o tbody manualmente
            const tbody = document.querySelector("#tabela-broadcasts tbody");
            const tabelaBroadcasts = document.querySelector("#tabela-broadcasts");

            // Limpa o tbody antes de adicionar novos dados
            tbody.innerHTML = "";
            
            // Destroi instância anterior se existir
            if (table) {
                table.destroy();
                table = null;
            }

            // Preenche a tabela
            data.forEach(broadcast => {
                const row = document.createElement("tr");
                row.innerHTML = `
                    <td>${broadcast.id}</td>
                    <td>${broadcast.nome}</td>
                    <td>${broadcast.numero_destinatario}</td>
                    <td>${broadcast.status_envio}</td>
                    <td>${broadcast.criado_em}</td>
                    <td>
                        <a onclick=''><i class='bx bxs-detail icon-green icon-size-20 disabled'></i></a>
                        <a onclick=''><i class='bx bxs-edit-alt icon-yellow icon-size-20 disabled'></i></a>
                        <i onclick='' class='bx bxs-trash icon-red icon-size-20 disabled' data-bs-toggle="modal" data-bs-target="#confirmDeleteModal"></i>
                    </td>
                `;
                tbody.appendChild(row);
            });

            // Recria DataTable
            if (tabelaBroadcasts) {
                // Só depois de preencher, inicializa o Simple-DataTables
                table = new simpleDatatables.DataTable("#tabela-broadcast", {
                    perPage: 25,
                    scrollY: "400px", // Scroll vertical funciona com wrapper CSS
                     perPageSelect: [10, 25, 50, 100] // opções disponíveis no select
                });
            }
        }
    );
}

function baixarExcel() {
    console.log("oi")
    // Pega os valores das datas dos inputs
    var dataInicial = document.getElementById('data-inicial').value;
    var dataFinal = document.getElementById('data-final').value;

    console.log(dataInicial)
    console.log(dataFinal)
    console.log("...")

    // Verifica se as datas foram preenchidas, se não, define como 'null'
    if (!dataInicial) {
        dataInicial = 'none';
    }
    if (!dataFinal) {
        dataFinal = 'none';
    }

    // Monta a URL manualmente
    var url = `/dashboard/baixar-excel-tabela-broadcast/${dataInicial}/${dataFinal}/`;

    // Redireciona para a URL com as datas
    window.location.href = url;
}

// Evento de clique no botão
document.addEventListener("DOMContentLoaded", () => {
    dataTableAtendimentos(); // carrega ao iniciar

    document.getElementById("baixar-excel").addEventListener("click", () => {
        baixarExcel(); // recarrega quando clicar
    });
});

new Chart(document.getElementById("bar-chart-grouped"), {
    type: 'bar',
    data: {
      labels: [""],
      datasets: [
        {
          label: "Novo Registro",
          backgroundColor: "#90ee90",
          data: [133]
        }, {
          label: "Enviado",
          backgroundColor: "#0d6efd",
          data: [408,]
        }, {
          label: "Confirmado",
          backgroundColor: "#008000",
          data: [408,]
        }, {
          label: "Não Respondeu",
          backgroundColor: "#ffc107",
          data: [734]
        }, {
          label: "Cancelado",
          backgroundColor: "#dc3545",
          data: [734]
        }, {
          label: "Erro ao Enviar",
          backgroundColor: "#f8d7da",
          data: [734]
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
