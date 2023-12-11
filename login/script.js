// This script is optional, but it shows how to validate the username and password before submitting the form.

const form = document.querySelector('form');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    const
 
username = document.getElementById('username').value;

    
const password = document.getElementById('password').value;

    if (username !== 'admin' || password !== 'Pass') {
        alert('Invalid username or password.');
        return;
    }

    // Submit the form if the username and password are valid
    form.submit();
});