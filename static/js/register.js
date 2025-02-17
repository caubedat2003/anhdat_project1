document.getElementById("register-form").addEventListener("submit", async function (event) {
    event.preventDefault();  // Prevent form from refreshing the page

    const first_name = document.getElementById("first_name").value;
    const last_name = document.getElementById("last_name").value;
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const phone_number = document.getElementById("phone_number").value;
    const password = document.getElementById("password").value;

    const response = await fetch("/api/customer/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ first_name, last_name, username, email, phone_number, password })
    });

    const data = await response.json();
    const messageEl = document.getElementById("message");

    if (response.ok) {
        messageEl.style.color = "green";
        messageEl.textContent = "User registered successfully!";
        setTimeout(() => {
            window.location.href = "/login/";
        }, 1500);
    } else {
        messageEl.style.color = "red";
        messageEl.textContent = data.error || "Registration failed!";
    }
});
