document.addEventListener("DOMContentLoaded", () => {
    const queryForm = document.getElementById("query-form");
    const queryInput = document.getElementById("query-input");

    queryForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const query = queryInput.value;

        // Redirect to Loading Screen with query as a URL parameter
        window.location.href = `/loading_screen?query=${encodeURIComponent(query)}`;
    });
});

document.addEventListener('DOMContentLoaded', function() {
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

    slider.addEventListener('input', function() {
        updateOutput(slider.value);
    });

    // Initialize with the default value
    updateOutput(slider.value);
});

document.addEventListener('DOMContentLoaded', function() {
    // Listen for events from the Flask backend
    const eventSource = new EventSource('/stream');

    eventSource.onmessage = function(event) {
        const data = event.data;
        const outputDiv = document.getElementById('output');

        // Display the data in the outputDiv
        const newParagraph = document.createElement('p');
        newParagraph.textContent = data;
        outputDiv.appendChild(newParagraph);

        // Redirect to info screen if processing is complete
        if (data.includes('Processing complete')) {
            const query = new URLSearchParams(window.location.search).get('query');
            const sliderValue = document.getElementById('myRange').value;
            window.location.href = `/info_screen?query=${encodeURIComponent(query)}&slider=${encodeURIComponent(sliderValue)}`;
        }
    };

    eventSource.onerror = function() {
        console.error('EventSource failed.');
        eventSource.close();
    };
});
