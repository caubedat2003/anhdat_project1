document.addEventListener("DOMContentLoaded", async function () {
    const customerId = localStorage.getItem("user_id");
    const orderDate = localStorage.getItem("orderDate");
    const totalPrice = localStorage.getItem("totalPrice");
    let addressId = localStorage.getItem("address_id"); // Fetch from local storage
    const shippingMethod = localStorage.getItem("shippingMethod");
    const transactionId = localStorage.getItem("paypalTransactionId");

    if (!customerId || !totalPrice || !shippingMethod || !transactionId) {
        alert("Error: Missing order details.");
        return;
    }

    try {
        // If address_id is missing in localStorage, fetch it from the backend
        if (!addressId) {
            const addressResponse = await fetch(`http://127.0.0.1:8000/api/customer/customers/${customerId}/address/`);
            if (!addressResponse.ok) throw new Error("Failed to fetch customer address");
            const address = await addressResponse.json();
            addressId = address.id;  // Extract address ID

            // Store address_id in localStorage for future use
            localStorage.setItem("address_id", addressId);
        }

        // Now create the order with the fetched address_id
        const response = await fetch("http://127.0.0.1:8000/api/order/create/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()  // Include CSRF token here
            },
            body: JSON.stringify({
                customer_id: customerId,
                order_date: orderDate,
                total_price: totalPrice,
                address_id: addressId,
                shipping_method: shippingMethod,
                transaction_id: transactionId,
                status: "delivering",  // Default order status
            })
        });

        const data = await response.json();
        if (response.ok) {
            localStorage.setItem("order_id", data.id);
            alert("Order placed successfully! Order ID: " + data.id);

            // Clear cart & local storage after successful order
            localStorage.removeItem("cart");
            localStorage.removeItem("paypalTransactionId");
            localStorage.removeItem("address_id");
            localStorage.removeItem("shipping_method");

        } else {
            alert("Failed to place order: " + data.error);
        }
    } catch (error) {
        console.error("Error creating order:", error);
        alert("An error occurred while placing the order.");
    }
    function getCSRFToken() {
        const cookieValue = document.cookie
            .split("; ")
            .find(row => row.startsWith("csrftoken="))
            ?.split("=")[1];
        return cookieValue;
    }
});
