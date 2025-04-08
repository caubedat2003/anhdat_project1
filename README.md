1. Install needed library
- python 3.12
- REST framework
- mongoengine (pip install mongoengine) - library to make connect with mongodb (version 0.29.1)
- dnspython (pip install dnspython) - library to make connect with mongodb (version 2.7.0)
- pip install wheel - library to make connect with mysql (version 0.45.1)
- mysqlclient (pip install mysqlclient) - library to make connect with mysql (version 2.2.7)
- psycopg2 (pip install psycopg2-binary) - library to make connect with postgres (version 2.9.10)

2. Setup docker
- Run MongoDB in Docker use : docker run -d -p 27017:27017 --name mongodb-container mongo 
- Check if MongoDB is Running: docker exec -it mongodb-container mongosh
- List Databases : show dbs
- Switch to the ecommerce Database: use ecommerce
- List Collections (Tables) use : show collections

3. How to run the website
- run python manage.py runserver
- enter http://127.0.0.1:8000/login/ to login or http://127.0.0.1:8000/register/ to create account
- after login, enter 127.0.0.1:8000/products/ and add products to cart
- enter 127.0.0.1:8000/cart/ to view cart and adjust quantity of item
- choose shipping method in 127.0.0.1:8000/shipping/
- choose PayPal to make payment 127.0.0.1:8000/payment/ (use email: son1@gmail.com password:sonson123 to login to paypal sandbox, or modify the bussiness and personal paypal account)

4. How to modify Paypal account
- Login to PayPal
- access https://developer.paypal.com/dashboard/accounts to create bussiness and personal account
- access https://developer.paypal.com/dashboard/applications/sandbox to create new app (connect with your bussiness account)
- take client id and replace it in script in payment.html (<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=USD"></script>)
- access https://www.sandbox.paypal.com/ to see all transactions
- detail instruction: https://www.youtube.com/watch?v=UX_F3maOWDo

5. DATA Folder
- Create new folder in C:/DATA
- Cut and paste all files in DATA folder into new folder
- Delete DATA folder in project
