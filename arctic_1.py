from arctic import Arctic
import mysql.connector
from oracle import OracleLiveData
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="invsto"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

store = Arctic('localhost')

library_name = 'demo_1'
if library_name not in store.list_libraries():
    store.initialize_library(library_name)
library = store[library_name]
ora = OracleLiveData(broker_name='finvasia')

ora.login(
    user_id="FA307801",
    password="Vyom@invsto1",
    factor2="44VR726763CN2JS3SAQ5366QLE62H2VA",
    vc="FA307801_U",
    api_key="3ecf70874d69583b02d599b1471c749b",
    imei="abc1234",
)
stored_data = {}

def onmessage(msg):
    try:
        # data = msg
        # print(data)
        # feature_to_store = data['lp']
        # item = library.write(data['ts'], feature_to_store)
        # print(f"Stored data for {data['ts']}")
        # print(item)
        # stored_Data.append(feature_to_store)
        # data = msg
        # print(data)
        # feature_to_store = data.get('lp')
        # token = data.get('tk')
        # timestamp = data.get('time')
        
        
        data = msg
        print(data)
        feature_to_store = data.get('lp')
        timestamp = data.get('time')

        if timestamp:
            item = library.write(timestamp, feature_to_store)
            print(f"Stored data for {timestamp}")
            print(feature_to_store)
            # stored_data[token]['data'].append(feature_to_store)
            # print(f"Appended data for {token}")
            # print(stored_data[token]['data'])
            
        # else:
        #     stored_data[token] ={'data': [feature_to_store], 'timestamp': timestamp}
        #     print(f"Created new entry for {token}")
        #     print(stored_data[token]['data'])
    except Exception as e:
        print(f"Error storing data: {e}")

def onerror(ms):
    print(ms)

def onclose(ms):
    print(ms)

instruments = ["TATAMOTORS-EQ", "TATASTEEL-EQ", "TCS-EQ"]

ora.get_livedata(
    instruments=instruments,
    exchange="NSE",
    onclose=onclose,
    onerror=onerror,
    onmessage=onmessage,
    searchscrip=True
)

print(stored_data)