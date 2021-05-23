from flask import Flask
from cassandra.cluster import Cluster

app=Flask(__name__)

@app.route("/")
def index():
    return ("CONGRATULATIONS. If you can see this page, it means that you have completed it successfully.")

@app.route("/app", methods = ['POST'])
def app_ep():
    cluster = Cluster(['192.168.10.11'])
    session = cluster.connect()
    session.execute('insert into test.test ("ts") values (toTimestamp(now()));')
    return "Success"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=80)
