# gunicorn_config.py
bind = "0.0.0.0:5000"
workers = 3  # Adjust the number of workers based on your app's needs
MYSQL = {
    'user': 'admin',
    'password': '54322016',
    'host': 'database-prod.c92a0wmu8szj.eu-north-1.rds.amazonaws.com',
    'database': 'sms_system'
}
