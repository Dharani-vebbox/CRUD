from pymongo import MongoClient
client=MongoClient("mongodb+srv://dharani:dharanii@cluster0.j3axywx.mongodb.net/")
db=client["datas"]
col=db["users"]