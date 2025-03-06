document.addEventListener("DOMContentLoaded", function () {
    fetchCartItems();
    updateUserUI();
});

function fetchCartItems() {
    const customerId = getCustomerId();
    if (!customerId) {
        alert("You need to log in to view your cart!");
        return;
    }

    fetch(`/api/cart/${customerId}/`)
        .then(response => response.json())
        .then(data => displayCartItems(data))
        .catch(error => console.error("Error fetching cart:", error));
}

function displayCartItems(cartItems) {
    const cartContainer = document.getElementById("cart-items");
    cartContainer.innerHTML = "";

    let totalPrice = 0;

    cartItems.forEach(item => {
        totalPrice += item.total_price;

        const cartItem = document.createElement("div");
        cartItem.classList.add("cart-item");

        cartItem.innerHTML = `
            <img src="/static/images/${item.image}" alt="Product Image" class="cart-image">
            <h3 class="cart-title">${item.title}</h3>
            <div class="cart-quantity">
                <button class="decrease-qty" data-cart-id="${item.id}">-</button>
                <span>${item.quantity}</span>
                <button class="increase-qty" data-cart-id="${item.id}">+</button>
            </div>
            <p class="cart-price">$${item.price}</p>
            <button class="remove-from-cart-btn" data-cart-id="${item.id}">Remove</button>
        `;

        cartContainer.appendChild(cartItem);
    });

    // Total Price Section
    const totalPriceElement = document.createElement("div");
    totalPriceElement.classList.add("cart-total");
    totalPriceElement.innerHTML = `<h3>Total Price: $${totalPrice.toFixed(2)}</h3>`;
    cartContainer.appendChild(totalPriceElement);

    // Proceed to Paying Button
    const proceedButton = document.createElement("button");
    proceedButton.classList.add("proceed-to-paying");
    proceedButton.textContent = "Proceed to Paying";
    proceedButton.addEventListener("click", function () {
        alert("Proceeding to payment...");
    });

    cartContainer.appendChild(proceedButton);

    attachRemoveListeners();
    attachQuantityListeners();
}

function attachQuantityListeners() {
    document.querySelectorAll(".increase-qty").forEach(button => {
        button.addEventListener("click", function () {
            const cartId = this.getAttribute("data-cart-id");
            updateQuantity(cartId, 1);
        });
    });

    document.querySelectorAll(".decrease-qty").forEach(button => {
        button.addEventListener("click", function () {
            const cartId = this.getAttribute("data-cart-id");
            updateQuantity(cartId, -1);
        });
    });
}

function updateQuantity(cartId, change) {
    fetch(`/api/cart/update/${cartId}/`, {
        method: "PATCH",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ change: change })
    })
        .then(response => response.json())
        .then(() => fetchCartItems()) // Refresh cart
        .catch(error => console.error("Error updating quantity:", error));
}

function attachRemoveListeners() {
    document.querySelectorAll(".remove-from-cart-btn").forEach(button => {
        button.addEventListener("click", function () {
            const cartId = this.getAttribute("data-cart-id");
            removeFromCart(cartId);
        });
    });
}

function removeFromCart(cartId) {
    fetch(`/api/cart/delete/${cartId}/`, { method: "DELETE" })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert("Error: " + data.error);
            } else {
                alert("Item removed!");
                fetchCartItems(); // Refresh cart after deletion
            }
        })
        .catch(error => console.error("Error removing item:", error));
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