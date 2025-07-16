# this file is used for connection with mysql workbench and performing some functions
import mysql.connector

# making connection with mysql workbench
DB_CONFIG = {  
    "host": "localhost",
    "user": "root",
    "password": "*******",
    "database": "pandeyji_eatery"
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# function for placing an order
def insert_order_item(food_item, quantity, order_id):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        cursor.callproc('insert_order_item', (food_item, quantity, order_id))
        cnx.commit()
        cursor.close()
        cnx.close()
        return 1
    except mysql.connector.Error as err:
        print(f"MySQL error: {err}")
        return -1
    except Exception as e:
        print(f"General error: {e}")
        return -1

# function for tracking user order
def insert_order_tracking(order_id, status):
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)", (order_id, status))
    cnx.commit()
    cursor.close()
    cnx.close()

# function to calculate total price of order
def get_total_order_price(order_id):
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute(f"SELECT get_total_order_price({order_id})")
    result = cursor.fetchone()[0]
    cursor.close()
    cnx.close()
    return result

# function to get next order id
def get_next_order_id():
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute("SELECT MAX(order_id) FROM orders")
    result = cursor.fetchone()[0]
    cursor.close()
    cnx.close()
    return 1 if result is None else result + 1

# function to check status of order(delievered/ in transit)
def get_order_status(order_id):
    try:
        cnx = get_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT status FROM order_tracking WHERE order_id = %s", (order_id,))
        result = cursor.fetchone()
        cursor.close()
        cnx.close()
        return result[0] if result else None
    except Exception as e:
        print(f"Error fetching order status: {e}")
        return None
