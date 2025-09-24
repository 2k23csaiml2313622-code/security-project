from pymongo.mongo_client import MongoClient
# Highlight: Angle brackets < > removed from the password
uri = "mongodb+srv://2k23csaiml2313622_db_user:wNuEWV1pH6SLiAcY@cluster0.dfk4o1r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB! ✅")
except Exception as e:
    print(e)