// Event listener remove messages
document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        document
            .querySelectorAll(".alert")
            .forEach((alert) => {
                bootstrap.Alert
                    .getOrCreateInstance(alert)
                    .close();
            });
    }, 3000);
});