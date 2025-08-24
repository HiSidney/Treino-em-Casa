// // Dados vindos do Django (convertidos em JSON)
// const pesos = JSON.parse('{{ pesos|escapejs }}');
// const datas = JSON.parse('{{ datas|escapejs }}');
// console.log(pesos, datas); // só para testar

// const ctx = document.getElementById('graficoPeso');
// new Chart(ctx, {
// type: 'line',
// data: {
//     labels: datas,
//     datasets: [{
//     label: 'Peso corporal (kg)',
//     data: pesos,
//     borderWidth: 2,
//     borderColor: 'blue',
//     fill: false
//     }]
// }
// });


document.addEventListener('DOMContentLoaded', function() {
    const canvasPeso = document.getElementById('graficoPeso').getContext('2d');
    const canvasReps = document.getElementById('graficoReps').getContext('2d');

    new Chart(canvasPeso, {
        type: 'line',
        data: { labels: datas, datasets: [{ label: 'Peso', data: pesos, borderColor: 'blue', backgroundColor: 'rgba(0,0,255,0.1)' }] },
        options: { responsive: true, maintainAspectRatio: false, plugins: {
            title: {
                display: true,
                text: 'Evolução do Peso Corporal',
                font: {
                    size: 18
                }
            }
        } }
    });

    new Chart(canvasReps, {
        type: 'bar',
        data: { labels: semanas, datasets: [{ label: 'Reps/Séries', data: reps, backgroundColor: 'green' }] },
        options: { responsive: true, maintainAspectRatio: false, plugins: {
            title: {
                display: true,
                text: 'Repetições por Semana',
                font: {
                    size: 18
                }
            }
        } }
    });
});
