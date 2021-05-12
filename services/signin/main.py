#signin service
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials

#add firebase credentials to the app
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route('/', methods=['POST'])
def add_user():
    #get json file
    data = flask.request.json
    nik = data["nik"]
    password = data["password"]

    #add nik and password to users collection
    doc_ref = db.collection(u'users').document(u'nik')
    doc_ref.set({
        u'nik' : nik,
        u'password' : password
    })

if __name__ == '__main__':
    app.run(debug=True)
