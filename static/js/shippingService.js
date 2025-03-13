const API_BASE_URL = "http://127.0.0.1:8000/api"; // Change to your API endpoint

// Fetch Order Details (Including Items)
async function fetchOrderDetails(orderId) {
    try {
        const response = await fetch(`${API_BASE_URL}/order/${orderId}/`);
        if (!response.ok) throw new Error("Failed to fetch order details");
        return await response.json();
    } catch (error) {
        console.error("Error:", error);
        return null;
    }
}

async function loadOrderDetails() {
    const orderDate = localStorage.getItem("orderDate");
    const totalPrice = localStorage.getItem("totalPrice");
    const userId = localStorage.getItem("user_id");

    if (!orderDate || !totalPrice || !userId) {
        alert("No order details found. Redirecting to cart.");
        window.location.href = "http://127.0.0.1:8000/cart/";
        return;
    }

    document.getElementById("orderDate").textContent = orderDate;
    document.getElementById("totalPrice").textContent = `$${totalPrice}`;

    try {
        const response = await fetch(`${API_BASE_URL}/cart/${userId}/`);
        if (!response.ok) throw new Error("Failed to fetch cart items");
        const cartItems = await response.json();

        const orderItemsContainer = document.getElementById("orderItems");
        orderItemsContainer.innerHTML = "";

        cartItems.forEach(item => {
            const listItem = document.createElement("div");
            listItem.classList.add("ship-item");
            listItem.innerHTML = `
                <img src="/static/images/${item.image}" alt="Product Image" class="ship-image">
                <h3 class="ship-title">${item.title}</h3>
                <p class="ship-price">${item.quantity} x $${item.price} = $${item.total_price}</p>
            `;
            orderItemsContainer.appendChild(listItem);
        });
        const addressResponse = await fetch(`${API_BASE_URL}/customer/customers/${userId}/address/`);
        if (!addressResponse.ok) throw new Error("Failed to fetch customer address");
        const address = await addressResponse.json();

        document.getElementById("customerAddress").textContent =
            `${address.house_number}, ${address.street}, ${address.district}, ${address.city}`;

        const customerResponse = await fetch(`${API_BASE_URL}/customer/customers/${userId}/`);
        if (!customerResponse.ok) throw new Error("Failed to fetch customer details");
        const customer = await customerResponse.json();
        document.getElementById("customerName").textContent = `${customer.first_name} ${customer.last_name}`;
        document.getElementById("customerPhone").textContent = customer.phone_number;
        document.getElementById("customerEmail").textContent = customer.email;
    } catch (error) {
        console.error("Error:", error);
        alert("Failed to load order items.");
    }
}

// Call function on page load
document.addEventListener("DOMContentLoaded", loadOrderDetails);


// Submit Selected Shipping Method
async function submitShipping(customerId, addressId, method) {
    try {
        const response = await fetch(`${API_BASE_URL}/shipping/select/`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                customer_id: customerId,
                address_id: addressId,
                method: method
            })
        });

        if (!response.ok) throw new Error("Failed to submit shipping method");
        alert("Shipping method selected successfully!");
        window.location.href = "/paying.html"; // Redirect to payment page
    } catch (error) {
        console.error("Error:", error);
        alert("Error submitting shipping method.");
    }
}

function getCustomerId() {
    return localStorage.getItem("user_id");
}

function updateUserUI() {
    const storedUsername = localStorage.getItem("username");
    const usernameDisplay = document.getElementById("username-display");

    if (storedUsername && usernameDisplay) {
        usernameDisplay.textContent = `Hello, ${storedUsername}`;
    }
}