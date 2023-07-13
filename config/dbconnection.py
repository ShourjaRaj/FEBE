from pymongo import MongoClient

from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("DB_URL"))
# url="mongodb+srv://shourjaganguly99:Y1wZJrCicEfk4n7w@cluster0.ywyeuxj.mongodb.net/?retryWrites=true&w=majority"

try:
    conn=MongoClient(os.getenv("DB_URL"))
    disease=conn.disease
    user=disease.user

except Exception as e:
    print(e)




