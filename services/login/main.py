#login service
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
def get_user():
    #get request form
    nik = request.form.get("nik")
    password = request.form.get("password")

    #get user data from database
    doc_ref = db.collection(u'users').document(nik)
    doc = doc_ref.get()
    if doc.exists:
        user = doc.to_dict()
        if user["password"] == password:
            return jsonify(user)
        else:
            return jsonify({"status":"nik dan password tidak sesuai"})
    else:
        return jsonify({"status":"nik tidak terdaftar"})

if __name__ == '__main__':
    app.run(debug=True)