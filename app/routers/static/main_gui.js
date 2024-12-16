document.addEventListener("DOMContentLoaded", () => {
    const queryForm = document.getElementById("query-form");
    const queryInput = document.getElementById("query-input");

    queryForm.addEventListener("submit", (e) => {
        e.preventDefault();
        const query = queryInput.value;

        // Redirect to info screen with query as a URL parameter
        window.location.href = `/info_screen?query=${encodeURIComponent(query)}`;
    });
});
