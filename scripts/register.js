function redirectToLoginPage() {
    window.location.href = "/OpenChat/login";
}

function submitForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirmPassword").value;

    if (password !== confirmPassword) {
        document.getElementById("error-message").innerText = "Passwords do not match";
        return;
    }

    var data = {
        username: username,
        password: password
    };

    fetch('/OpenChat/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        console.log('Status:', response.status);

        if (!response.ok) {
            return response.text().then(text => {
                throw new Error(text);
            });
        }

        return response.json();
    })
    .then(data => {
        window.location.href = "/OpenChat/chat";
    })
    .catch(error => {
        console.error('There has
