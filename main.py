import psycopg2
import pandas as pd
from sshtunnel import SSHTunnelForwarder
import os

SSH_KEY = os.environ('SSH_KEY_PINKET')
SSH_USERNAME =  os.environ('SSH_USERNAME-PINKET')

try:
    # Create an SSH tunnel
    tunnel = SSHTunnelForwarder(
        ('91.98.99.106', 12091),
        ssh_username=SSH_USERNAME,
        ssh_password=SSH_KEY,
        remote_bind_address=('localhost', 5432),
        local_bind_address=('localhost', 5433),  # could be any available port
    )
    # Start the tunnel
    tunnel.start()

except:
    print("SSH Tunnel Failed")
    # os._exit(0)

try:
    # Create a database connection
    conn = psycopg2.connect(
        database='VShop',
        user=SSH_USERNAME,
        password=SSH_KEY,
        # host='postgres-replica1.pinket.local',
        # port='5432',
        host='localhost',
        port='5433',
    )
    # Get a database cursor
    cur = conn.cursor()

except:
    print("Database Connection Failed")
    # os._exit(0)


def normal_distribuation(a, b):

    cur.execute(f"""select c.id, c.registerdate,min(so.checkoutdate) from vshop.customers c
    inner join vshop.shopping_orders so on c.id = so.customerid
    where so.status in ('completed','in_progress','canceled') and
          c.registerdate::date>= current_date - interval '180 days'
    group by 1,2; """)

    user_history = pd.DataFrame(cur.fetchall(), columns=['id', 'register', 'first_order'])
    user_history['difference'] = (user_history['first_order'] - user_history['register'])

    # to extract day from timedelta format array you should access to every element
    l = []  # empty list
    for i in range(len(user_history['difference'])):
        d = user_history['difference'][i].days
        # user_history['difference'][i] row i from column 'difference'
        l.append(d)
        # append day to empty list gradually
    user_history['difference'] = l
    m = user_history["difference"].mean()
    s = user_history["difference"].std()
    #a = 1
    #b = 1
    t = user_history[(user_history['difference'] < m + (a * s)) & (user_history['difference'] > m - (b * s))]
    #print(a, b)


#normal_distribuation(1, 1)
