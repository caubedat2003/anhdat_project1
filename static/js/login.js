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
                    // Store user info in localStorage
                    localStorage.setItem("user_id", data.user_id);
                    localStorage.setItem("username", data.username);

                    // Update UI dynamically
                    updateUserUI(data.username, data.user_id);

                    // Redirect to products page
                    setTimeout(() => {
                        window.location.href = "/products";
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
    function updateUserUI(username, userId) {
        const usernameDisplay = document.getElementById("username-display");
        if (usernameDisplay) {
            usernameDisplay.textContent = username;
            usernameDisplay.setAttribute("data-customer-id", userId);
        }
    }

    // Check localStorage on page load and update UI
    function checkUserSession() {
        const storedUsername = localStorage.getItem("username");
        const storedUserId = localStorage.getItem("user_id");

        if (storedUsername && storedUserId) {
            updateUserUI(storedUsername, storedUserId);
        }
    }

    checkUserSession(); // Run on page load
});
