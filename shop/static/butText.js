document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('action-button');
    const currentURL = window.location.href;

    if (currentURL.includes('/edit')) {
        button.textContent = 'Edit car';
    }
    else {
        button.textContent = 'Add new car';
    }
});
