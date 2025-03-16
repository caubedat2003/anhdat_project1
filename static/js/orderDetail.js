document.addEventListener("DOMContentLoaded", async function () {
    const userId = localStorage.getItem("user_id");
    let orderId = localStorage.getItem("order_id");
    while (!orderId) {
        console.log("Waiting for order_id...");
        await new Promise(resolve => setTimeout(resolve, 500)); // Wait 0.5 seconds
        orderId = localStorage.getItem("order_id");
    }

    console.log("Order ID found:", orderId);

    try {
        // Fetch customer details
        const customerResponse = await fetch(`http://127.0.0.1:8000/api/customer/customers/${userId}`);
        if (!customerResponse.ok) throw new Error("Failed to fetch customer details");
        const customer = await customerResponse.json();

        document.getElementById("customerName").textContent = `${customer.first_name} ${customer.last_name}`;
        document.getElementById("customerPhone").textContent = customer.phone_number;
        document.getElementById("customerEmail").textContent = customer.email;

        // Fetch customer address
        const addressResponse = await fetch(`http://127.0.0.1:8000/api/customer/customers/${userId}/address/`);
        if (!addressResponse.ok) throw new Error("Failed to fetch customer address");
        const address = await addressResponse.json();
        document.getElementById("customerAddress").textContent =
            `${address.house_number}, ${address.street}, ${address.district}, ${address.city}`;

        // Fetch order details
        const orderResponse = await fetch(`http://127.0.0.1:8000/api/order/${orderId}`);
        if (!orderResponse.ok) throw new Error("Failed to fetch order details");
        const order = await orderResponse.json();
        document.getElementById("orderDate").textContent = order.order_date;
        document.getElementById("totalPrice").textContent = `$${order.total_price}`;

        // Fetch shipping method
        const shippingResponse = await fetch(`http://127.0.0.1:8000/api/shipping/get/${orderId}`);
        if (!shippingResponse.ok) throw new Error("Failed to fetch shipping method");
        const shipping = await shippingResponse.json();
        document.getElementById("shipMethod").textContent = shipping.method;

        // Fetch order items
        const itemsResponse = await fetch(`http://127.0.0.1:8000/api/order/items/${orderId}/`);
        if (!itemsResponse.ok) throw new Error("Failed to fetch order items");
        const orderItems = await itemsResponse.json();

        const orderItemsContainer = document.getElementById("orderItems");
        orderItemsContainer.innerHTML = "";

        orderItems.forEach(item => {
            const title = item.product_details?.title || "Unknown Product";
            const price = item.product_details?.price || "N/A";
            const image = item.product_details?.image || "default.jpg";

            const listItem = document.createElement("div");
            listItem.classList.add("ship-item");
            listItem.innerHTML = `
                <img src="/static/images/${image}" alt="Product Image" class="ship-image">
                <h3 class="ship-title">${title}</h3>
                <p class="ship-price">${item.quantity} x $${price} = $${item.total_price}</p>
            `;
            orderItemsContainer.appendChild(listItem);
        });
    } catch (error) {
        console.error("Error loading order details:", error);
        alert("Failed to load order details.");
    }
});
