const submitBtn = document.getElementById('submit-btn');
const dateInput = document.getElementById('date');
const bodyWeightInput = document.getElementById('body-weight');
const pushUpsInput = document.getElementById('push-ups');
const pullUpsInput = document.getElementById('pull-ups');
const squatsInput = document.getElementById('squats');

let workoutData = [];

submitBtn.addEventListener('click', () => {
    const workout = {
        date: dateInput.value,
        bodyWeight: parseFloat(bodyWeightInput.value),
        pushUps: parseInt(pushUpsInput.value),
        pullUps: parseInt(pullUpsInput.value),
        squats: parseInt(squatsInput.value),
    };

    if (workout.date && workout.bodyWeight && workout.pushUps && workout.pullUps && workout.squats) {
        workoutData.push(workout);
        saveDataToLocalStorage(workoutData);
        updateChart(workoutData);
        resetForm();
    } else {
        alert("Please fill in all fields!");
    }
});

function saveDataToLocalStorage(data) {
    localStorage.setItem('workoutData', JSON.stringify(data));
}

function loadDataFromLocalStorage() {
    const savedData = localStorage.getItem('workoutData');
    if (savedData) {
        workoutData = JSON.parse(savedData);
        updateChart(workoutData);
    }
}

function resetForm() {
    dateInput.value = '';
    bodyWeightInput.value = '';
    pushUpsInput.value = '';
    pullUpsInput.value = '';
    squatsInput.value = '';
}

function updateChart(data) {
    const labels = data.map(item => item.date);
    const bodyWeights = data.map(item => item.bodyWeight);
    const pushUps = data.map(item => item.pushUps);
    const pullUps = data.map(item => item.pullUps);
    const squats = data.map(item => item.squats);

    const ctx = document.getElementById('progress-chart').getContext('2d');
    const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Body Weight (kg)',
                    data: bodyWeights,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    fill: false,
                },
                {
                    label: 'Push-ups (reps)',
                    data: pushUps,
                    borderColor: 'rgba(54, 162, 235, 1)',
                    fill: false,
                },
                {
                    label: 'Pull-ups (reps)',
                    data: pullUps,
                    borderColor: 'rgba(75, 192, 192, 1)',
                    fill: false,
                },
                {
                    label: 'Squats (reps)',
                    data: squats,
                    borderColor: 'rgba(153, 102, 255, 1)',
                    fill: false,
                }
            ]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

// Load previous data if available
loadDataFromLocalStorage();
