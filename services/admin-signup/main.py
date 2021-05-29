#signup service
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
def add_admin():
    #get request form
    email = request.form.get("email")
    name = request.form.get("nama")
    username = request.form.get("username")
    password = request.form.get("password")

    #get user data
    doc_ref = db.collection(u'admins').document(email)
    doc = doc_ref.get()
    #check if user already exists
    if doc.exists:
        admin = doc.to_dict()
        #check if password already set
        if "password" in admin:
            return jsonify({"status":"email sudah terdaftar"}), 401
        else:
            #add nik and password to users collection
            doc_ref.update({
                u'password' : password
            })
            return jsonify({"status":"user telah terdaftar"})
    else:
        #add nik and password to users collection
        doc_ref.set({
            u'email' : email,
            u'nama' : name,
            u'username' : username,
            u'password' : password
        })
        return jsonify({"status":"user telah terdaftar"})

if __name__ == '__main__':
    app.run(debug=True)
