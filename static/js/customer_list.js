function fetchCustomers() {
    fetch("/api/customer/customers/")
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("customer-table-body");
            tableBody.innerHTML = "";

            data.forEach(customer => {
                let row = `<tr>
                            <td>${customer.first_name} ${customer.last_name}</td>
                            <td>${customer.username}</td>
                            <td>${customer.email}</td>
                            <td>${customer.phone_number}</td>
                        </tr>`;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error("Error fetching customers:", error));
}

document.addEventListener("DOMContentLoaded", fetchCustomers);
