let chart;

async function predict() {
    const symbol = document.getElementById("symbol").value.trim();

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ symbol })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        `${symbol.toUpperCase()} — 30-Day Forecast Loaded`;

    drawChart(data.historical_prices, data.predicted_prices);
}

function drawChart(historical, predicted) {
    const ctx = document.getElementById("chartCanvas");

    if (chart) chart.destroy();

    const totalLabels = [
        ...Array(historical.length).fill("Past"),
        ...Array(predicted.length).fill("Future")
    ];

    chart = new Chart(ctx, {
        type: "line",
        data: {
            labels: totalLabels,
            datasets: [
                {
                    label: "Historical (Last 60 Days)",
                    data: [...historical],
                    borderColor: "#4e54c8",
                    pointRadius: 0,
                    borderWidth: 3,
                    tension: 0.35
                },
                {
                    label: "Predicted (Next 30 Days)",
                    data: [...Array(historical.length).fill(null), ...predicted],
                    borderColor: "#ff6ec7",
                    pointRadius: 0,
                    borderWidth: 3,
                    borderDash: [5, 5],
                    tension: 0.35
                }
            ]
        },
        options: {
            plugins: {
                legend: {
                    labels: { color: "#fff" }
                }
            },
            scales: {
                x: { ticks: { color: "#fff" } },
                y: { ticks: { color: "#fff" } }
            }
        }
    });
}
