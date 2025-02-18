document.getElementById("loginForm").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent page reload

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
        const messageElement = document.getElementById("responseMessage");

        if (response.ok) {
            messageElement.style.color = "green";
            messageElement.textContent = "Login successful!";

            setTimeout(() => {
                window.location.href = "";
            }, 1500);
        } else {
            messageElement.style.color = "red";
            messageElement.textContent = data.error || "Login failed!";
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("responseMessage").textContent = "An error occurred!";
    }
});