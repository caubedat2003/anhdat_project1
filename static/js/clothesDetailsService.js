document.addEventListener("DOMContentLoaded", function () {
    const clothesId = new URLSearchParams(window.location.search).get("id"); // Get ID from URL
    if (!clothesId) {
        alert("Clothes ID is missing!");
        return;
    }

    fetch(`http://127.0.0.1:8000/api/clothes/${clothesId}/`) // Fetch book details
        .then(response => response.json())
        .then(data => {
            document.getElementById("clothes-title").textContent = data.title;
            document.getElementById("clothes-brand").textContent = data.brand;
            document.getElementById("clothes-size").textContent = data.size;
            document.getElementById("clothes-color").textContent = data.size;
            document.getElementById("clothes-price").textContent = data.price;
            document.getElementById("clothes-description").textContent = data.description;
            document.getElementById("clothes-image").src = `/static/images/${data.image}`;

            // Set product ID in button
            const addToCartButton = document.getElementById("add-to-cart-btn");
            addToCartButton.setAttribute("data-product-id", clothesId);

            // Attach event listener AFTER setting product ID
            addToCartButton.addEventListener("click", function () {
                addToCart(clothesId);
            });

            loadComments(clothesId);
        })
        .catch(error => {
            console.error("Error fetching clothes details:", error);
            alert("Failed to load clothes details.");
        });

    function addToCart(clothesId) {
        const customerId = getCustomerId(); // Ensure this function exists
        if (!customerId) {
            alert("You must be logged in to add items to your cart!");
            return;
        }

        fetch("/api/cart/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken() // Ensure this function exists
            },
            body: JSON.stringify({
                customer_id: customerId,
                product_id: clothesId,
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

    function loadComments(clothesId) {
        fetch(`http://127.0.0.1:8000/api/comments/${clothesId}/`)  // Updated URL
            .then(response => response.json())
            .then(comments => {
                const commentsSection = document.getElementById("comment-list");
                commentsSection.innerHTML = "";  // Clear old comments
                comments.forEach(comment => {
                    const commentDiv = document.createElement("div");
                    commentDiv.classList.add("comment-box");
                    commentDiv.innerHTML = `<strong>User ${comment.customer_id}:</strong> ${comment.content}`;
                    commentsSection.appendChild(commentDiv);
                });
            })
            .catch(error => console.error("Error loading comments:", error));
    }

    document.getElementById("submit-comment").addEventListener("click", function () {
        const content = document.getElementById("comment-input").value;
        const customerId = getCustomerId();

        if (!customerId) {
            alert("You must be logged in to comment!");
            return;
        }
        if (!content.trim()) {
            alert("Comment cannot be empty!");
            return;
        }

        fetch(`http://127.0.0.1:8000/api/comments/add/`, {  // Updated URL
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken()
            },
            body: JSON.stringify({
                "product": clothesId,
                "customer_id": customerId,
                "content": content
            })
        })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert("✅ Comment added!");
                    document.getElementById("comment-input").value = "";
                    loadComments(bookId);
                } else {
                    alert("❌ Failed to add comment. Please try again.");
                }
            })
            .catch(error => console.error("Error adding comment:", error));
    });
});
