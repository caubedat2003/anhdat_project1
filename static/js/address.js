document.getElementById('address-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        house_number: document.getElementById('house_number').value,
        street: document.getElementById('street').value,
        district: document.getElementById('district').value,
        city: document.getElementById('city').value,
        customer_idS: localStorage.getItem('user_id')  // Replace with actual customer ID from session/auth
    };

    try {
        const response = await fetch('/api/customer/addresses/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();
        const messageDiv = document.getElementById('message');

        if (response.ok) {
            messageDiv.style.color = 'green';
            messageDiv.textContent = 'Address added successfully!';
            document.getElementById('address-form').reset();
        } else {
            messageDiv.style.color = 'red';
            messageDiv.textContent = `Error: ${result.detail || 'Failed to add address'}`;
        }
    } catch (error) {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').textContent = 'Error: Network issue';
    }
});