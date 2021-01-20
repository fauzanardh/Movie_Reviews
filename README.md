## How to Run
1. Apply the migrations to the sql database
   ```sh
   python manage.py migrate
    ```
2. Collect static files
   ```sh
   python manage.py collectstatic
   ```
3. Create an administrator account
   ```sh
   python manage.py createsuperuser
   ```
4. Run the Server
   ```sh
   python manage.py runserver
    ```
