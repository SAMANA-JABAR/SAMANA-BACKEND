#login service for admin app
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
def get_admin():
    #get request form
    email = request.form.get("email")
    password = request.form.get("password")

    #get admin data from database
    doc_ref = db.collection(u'admins').document(email)
    doc = doc_ref.get()
    if doc.exists:
        admin = doc.to_dict()
        #check if password already set
        if "password" in admin:
            if admin["password"] == password:
                return jsonify(admin)
            else:
                return jsonify({"status":"email dan password tidak sesuai"}), 401
        else:
            return jsonify({"status":"user belum terdaftar"}), 401
    else:
        return jsonify({"status":"email tidak terdaftar"}), 401

if __name__ == '__main__':
    app.run(debug=True)
