function validateUsername(theInput) {
    var val = theInput.value;
    if (/Carshop/i.test(val)) {
        alert("Name: CarShop is not available");
        return false;
    } else {
        return true;
    }
}

function setValidation() {
    var form = document.getElementById('signup_form');
    var usernameInput = document.getElementById('id_username');

    form.addEventListener('submit', function (event) {
        if (!validateUsername(usernameInput)) {
            event.preventDefault();
        }
    });

    usernameInput.addEventListener('input', function () {
        validateUsername(usernameInput);
    });
}
document.addEventListener('DOMContentLoaded', setValidation);