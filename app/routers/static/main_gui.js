document.addEventListener("DOMContentLoaded", () => {
    const queryForm = document.getElementById("query-form");
    const queryInput = document.getElementById("query-input");
    const loadingScreen = document.getElementById("loading-screen");
    const queryScreen = document.getElementById("query-screen");
    const slider = document.getElementById('myRange');
    const output = document.getElementById('demo');

    function updateOutput(value) {
        if (value < 34) {
            output.textContent = 'Broad';
        } else if (value < 67) {
            output.textContent = 'Moderate';
        } else {
            output.textContent = 'Precise';
        }
    }

    slider.addEventListener('input', function () {
        updateOutput(slider.value);
    });

    // Initialize with the default value
    updateOutput(slider.value);

    queryForm.addEventListener("submit", (e) => {
        e.preventDefault(); // Prevent the form's default behavior
        const query = queryInput.value.trim();
        const sliderValue = output.textContent;

        if (!query) {
            alert("Please enter a query.");
            return;
        }

        queryScreen.classList.remove("active");
        loadingScreen.classList.add("active");

        fetch(`/querydata?query=${encodeURIComponent(query)}&slider=${encodeURIComponent(sliderValue)}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.error) {
                    alert(data.error);
                    loadingScreen.classList.remove("active");
                    queryScreen.classList.add("active");
                } else {
                    window.location.href = `/info_screen?query=${encodeURIComponent(query)}`;
                }
            })
            .catch(error => {
                alert('An error occurred: ' + error.message);
                loadingScreen.classList.remove("active");
                queryScreen.classList.add("active");
            });
    });
});
