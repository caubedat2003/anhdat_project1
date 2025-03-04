document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    if (loginForm) {
        loginForm.addEventListener("submit", async function (event) {
            event.preventDefault();

            const formData = {
                username: document.getElementById("username").value,
                password: document.getElementById("password").value
            };

            try {
                const response = await fetch("/api/customer/login/", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(formData),
                });

                const data = await response.json();

                if (response.ok) {
                    // Update username display
                    const usernameDisplay = document.getElementById("username-display");
                    if (usernameDisplay) {
                        usernameDisplay.textContent = data.username;
                    }

                    // Redirect to homepage
                    setTimeout(() => {
                        window.location.href = "/";
                    }, 1500);
                } else {
                    document.getElementById("responseMessage").textContent = data.error || "Login failed!";
                }
            } catch (error) {
                console.error("Error:", error);
                document.getElementById("responseMessage").textContent = "An error occurred!";
            }
        });
    }
});
