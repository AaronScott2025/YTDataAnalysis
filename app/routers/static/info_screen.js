document.addEventListener("DOMContentLoaded", async () => {
    const urlParams = new URLSearchParams(window.location.search);
    const query = urlParams.get("query");

    const graphContainer = document.getElementById("graph");
    const dataList = document.getElementById("data-list");

    if (query) {
        // Fetch data from Flask backend
        const response = await fetch(`/api/query?query=${encodeURIComponent(query)}`);
        const data = await response.json();

        // Render graph and data
        renderGraph(data.graphData);
        renderDataList(data.details);
    } else {
        dataList.innerHTML = `<li>Error: No query provided!</li>`;
    }

    // Render the graph using Chart.js
    function renderGraph(graphData) {
        new Chart(graphContainer, {
            type: "bar",
            data: {
                labels: graphData.labels,
                datasets: [{
                    label: graphData.label,
                    data: graphData.values,
                    backgroundColor: "rgba(0, 123, 255, 0.5)",
                    borderColor: "rgba(0, 123, 255, 1)",
                    borderWidth: 1,
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { display: true },
                }
            }
        });
    }

    // Render the data list
    function renderDataList(details) {
        dataList.innerHTML = details.map(item => `<li>${item}</li>`).join("");
    }
});
