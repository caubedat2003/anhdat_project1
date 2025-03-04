document.addEventListener("DOMContentLoaded", function () {
    const categories = ["books", "mobiles", "clothes", "shoes"];

    categories.forEach(category => {
        fetchProducts(category);
    });

    function fetchProducts(category) {
        fetch(`/api/${category}/`)
            .then(response => response.json())
            .then(data => displayProducts(category, data))
            .catch(error => console.error(`Error fetching ${category}:`, error));
    }

    function displayProducts(category, products) {
        const container = document.querySelector(`#${category}-section`);
        container.innerHTML = "";

        products.forEach(product => {
            const productCard = document.createElement("div");
            productCard.classList.add("product-card");

            // Correct way to construct static image URLs
            const staticImagePath = `/static/images/${product.image}`;

            productCard.innerHTML = `
                <img src="${staticImagePath}" alt="Product Image">
                <h3>${product.title}</h3>
                <p>Price: $${product.price}</p>
                <button class="add-to-cart-btn">Add to Cart</button>
            `;

            container.appendChild(productCard);
        });
    }

});
function scrollLeft(sectionId) {
    document.getElementById(sectionId).scrollBy({ left: -300, behavior: 'smooth' });
}

function scrollRight(sectionId) {
    document.getElementById(sectionId).scrollBy({ left: 300, behavior: 'smooth' });
}