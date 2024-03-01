import sqlite3
from datetime import datetime

# Connect to a SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Use executescript() to execute multiple SQL statements at once
cursor.executescript('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT,
        total_amount REAL
    );

    CREATE TRIGGER IF NOT EXISTS update_total_purchases
    AFTER INSERT ON orders
    BEGIN
        UPDATE customers
        SET total_purchases = total_purchases + NEW.total_amount
        WHERE id = NEW.customer_id;
    END;
''')

# Insert data into the orders table with the current date
order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cursor.execute("INSERT INTO orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)", (1, order_date, 75.50))
cursor.execute("INSERT INTO orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)", (2, order_date, 120.75))
conn.commit()

# Query orders and associated customer data
cursor.execute('''
    SELECT orders.id, orders.order_date, orders.total_amount,
    customers.name, customers.total_purchases
    FROM orders
    JOIN customers ON orders.customer_id = customers.id
''')
order_customer_data = cursor.fetchall()
print("\nOrders and Associated Customer Data:")
for row in order_customer_data:
    print(row)

# Demonstrate using date functions in queries
cursor.execute("SELECT * FROM orders WHERE DATE(order_date) = DATE(?)", (order_date,))
orders_today = cursor.fetchall()
print("\nOrders placed today:")
for row in orders_today:
    print(row)

# Demonstrate using LIMIT and OFFSET in queries
cursor.execute("SELECT * FROM customers ORDER BY total_purchases DESC LIMIT 2 OFFSET 1")
limited_customers = cursor.fetchall()
print("\nTop 2 Customers with OFFSET:")
for row in limited_customers:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
