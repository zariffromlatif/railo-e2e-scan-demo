import psycopg2


def orders_for(conn, customer_id, status):
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders WHERE customer_id = %s AND status = %s", (customer_id, status))
    return cur.fetchall()
