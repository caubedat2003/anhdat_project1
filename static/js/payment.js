document.addEventListener("DOMContentLoaded", function () {
    const totalPrice = localStorage.getItem("totalPrice") || "0.00"; // Get total price from local storage

    paypal.Buttons({
        createOrder: function (data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: totalPrice // Use the stored total price
                    }
                }]
            });
        },
        onApprove: function (data, actions) {
            return actions.order.capture().then(function (details) {
                const transactionId = details.purchase_units[0].payments.captures[0].id;
                localStorage.setItem("paypalTransactionId", transactionId);
                alert("Transaction completed by " + details.payer.name.given_name);
                window.location.href = "/order/"; // Redirect to success page
            });
        },
        onError: function (err) {
            console.error(err);
            alert("An error occurred during the transaction.");
        }
    }).render("#paypal-button-container");
});
