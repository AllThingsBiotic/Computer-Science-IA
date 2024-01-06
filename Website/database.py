import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
import os

db_key = "mysql+pymysql://tjhiurdpnl5ze4wmdxvu:pscale_pw_MAWO5SPpp7GB0O2S2HJLy5FyDD3Fo9S5plH80uaQsLk@aws.connect.psdb.cloud/starlight?charset=utf8mb4"    

engine = create_engine(
db_key,
connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    result = conn.execute(text("select * from reservations"))
    print(result.all())

def load_reservations():
  with engine.connect() as conn:
    result = conn.execute(text("select * from reservations"))
    reserves = []
    for row in result.all():
      reserves.append(dict(row))
    return reserves

def write_reservations(reservation_id, data):
  with engine.connect() as conn:
    query = text("insert into reservations (id, title, phone_number, whatDay, whatTime, party_size) VALUES (:name, :phone, :date, :time, :party-size)")

    conn.execute(query, 
                 id=reservation_id, 
                 title=data['name'],
                 phone_number=data['phone'],
                 whatDay=data['date'],
                 whatTime=data['time'],
                 party_size=data['party-size']
    )    

print(sqlalchemy.__version__)








menu_appetizer = [
    {
        'id' : '1',
        'name' : 'Spring Roll (2)',
        'price' : '3.99'
    },
  {
        'id' : '2',
        'name' : 'Egg Roll (1)',
        'price' : '2.99'
    },
  {
        'id' : '3',
        'name' : 'Deep Fried Chicken Wings',
        'price' : '14.50'
    },
    {
        'id' : '3A',
        'name' : 'Salt & Pepper Chicken Wings',
        'price' : '14.50'
    },
{
        'id' : '4',
        'name' : 'Deep Fried Wonton',
        'price' : '13.50'
    },
    {
        'id' : '4A',
        'name' : 'Cheese Wonton',
        'price' : '13.50'
    },
    {
        'id' : '5',
        'name' : 'Grilled Pork with Vegetable Dumplings',
        'price' : '13.50'
    },
{
        'id' : '6',
        'name' : 'Dry Garlic Ribs',
        'price' : '14.99'
    },
    {
        'id' : '7',
        'name' : 'Honey Garlic Chicken Wings',
        'price' : '14.50'
    },
    {
        'id' : '8',
        'name' : 'Sliced B.B.Q. Pork',
        'price' : '14.50'
    },
]

menu_soup = [
{
        'id' : '9',
        'name' : 'Wonton Soup (small)',
        'price' : '6.99'
    },
    {
        'id' : '9A',
        'name' : 'Wonton Soup (large)',
        'price' : '12.99'
    },
    {
        'id' : '10',
        'name' : 'Wor Wonton Soup (small)',
        'price' : '8.99'
    },
    {
        'id' : '10A',
        'name' : 'Wor Wonton Soup (Large)',
        'price' : '16.99'
    },
    {
        'id' : '11',
        'name' : 'Hot & Sour Soup',
        'price' : '8.99'
    },
    {
        'id' : '12',
        'name' : 'Chicken with Sweet Corn Soup',
        'price' : '8.99'
    },
    {
        'id' : '14',
        'name' : 'Chicken Noodle Soup',
        'price' : '8.99'
    },
]
menu_sizzlingRice = [
    {
    'id' : '15',
    'name' : 'Prawn & Meats with Vegetables on Sizzling Rice',
    'price' : '17.50'
    },
    {
    'id' : '16',
    'name' : 'Sliced Beef & Vegetables on Sizzling Rice',
    'price' : '15.50'
    },
    {
    'id' : '17',
    'name' : 'Sliced Chicken & Vegetables on Sizzling Rice',
    'price' : '15.50'
    },
    {
    'id' : '18',
    'name' : 'Mixed Vegetables on Sizzling Rice',
    'price' : '15.50'
    },
    {
    'id' : '19',
    'name' : 'Tomato & Shrimps on Sizzling Rice',
    'price' : '17.50'
    },
    {
    'id' : '20',
    'name' : 'Hot & Sour Soup on Sizzling Rice',
    'price' : '15.50'
    }
]
