#dashboard service
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore

#add firebase credentials to the app
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.Client()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get_dashboard():
    #get request form
    nik = request.form.get("nik")

    #get user data from database
    doc_ref = db.collection(u'users').document(nik)
    doc = doc_ref.get()
    user = doc.to_dict()

    #get the latest bantuan
    bantuan = user['bantuan']
    current_bantuan = max(bantuan, key=lambda x:x['timestamp'])

    #assign user data to profile dict
    profile = {
        "nik" : user['nik'],
        "nama" : user['nama'],
        "bantuan" : current_bantuan['jenis'],
        "status" : current_bantuan['status']
    }
    return jsonify(profile)

if __name__ == '__main__':
    app.run(debug=True)
