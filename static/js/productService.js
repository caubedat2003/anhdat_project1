document.addEventListener("DOMContentLoaded", function () {
    const categories = ["books", "mobiles", "clothes", "shoes"];

    categories.forEach(category => {
        fetchProducts(category);
    });

    function fetchProducts(category) {
        fetch(`/api/${category}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Failed to fetch ${category}`);
                }
                return response.json();
            })
            .then(data => displayProducts(category, data))
            .catch(error => console.error(`Error fetching ${category}:`, error));
    }

    function displayProducts(category, products) {
        const container = document.querySelector(`#${category}-section`);
        if (!container) return;
        container.innerHTML = "";

        products.forEach(product => {
            const productCard = document.createElement("div");
            productCard.classList.add("product-card");

            // Construct static image URLs
            const staticImagePath = `/static/images/${product.image}`;

            productCard.innerHTML = `
                <img src="${staticImagePath}" alt="Product Image">
                <h3>
                    <a class="a-text" href="http://127.0.0.1:8000/${category}/details/?id=${product.id}">
                    ${product.title}
                </a>
                </h3>
                <p>Price: $${product.price}</p>
                <button class="add-to-cart-btn" data-product-id="${product.id}">Add to Cart</button>
            `;

            container.appendChild(productCard);
        });

        // Attach event listeners after rendering
        attachAddToCartListeners();
    }

    function attachAddToCartListeners() {
        document.querySelectorAll(".add-to-cart-btn").forEach(button => {
            button.removeEventListener("click", handleAddToCart); // Avoid duplicate event listeners
            button.addEventListener("click", handleAddToCart);
        });
    }

    function handleAddToCart(event) {
        const productId = event.target.getAttribute("data-product-id");
        addToCart(productId);
    }

    function addToCart(productId) {
        const customerId = getCustomerId();
        if (!customerId) {
            alert("You must be logged in to add items to your cart!");
            return;
        }

        fetch("/api/cart/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            body: JSON.stringify({
                customer_id: customerId,
                product_id: productId,
                quantity: 1
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert("✅ Item added to cart!");
                } else {
                    alert("❌ Failed to add item. Please try again.");
                }
            })
            .catch(error => console.error("Error adding to cart:", error));
    }

    function getCustomerId() {
        return localStorage.getItem("user_id");  // Fetch from localStorage instead of session
    }

    function getCSRFToken() {
        return document.cookie.split('; ')
            .find(row => row.startsWith('csrftoken='))
            ?.split('=')[1];
    }
});

// Scroll functions
function scrollLeft(sectionId) {
    document.getElementById(sectionId).scrollBy({ left: -300, behavior: 'smooth' });
}

function scrollRight(sectionId) {
    document.getElementById(sectionId).scrollBy({ left: 300, behavior: 'smooth' });
}
