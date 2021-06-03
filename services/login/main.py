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
        #check if password already set
        if "password" in user:
            if user["password"] == password:
                if 'bantuan' in user:
                    #get the latest bantuan
                    bantuan = user['bantuan']
                    current_bantuan = bantuan[-1]

                    profile = {
                        "nik" : user['nik'],
                        "nama" : user['nama'],
                        "password" : user['password'],
                        "bantuan" : current_bantuan['jenis'],
                        "status" : current_bantuan['status']
                    }
                    return jsonify(profile)
                elif 'nama' in user:
                    profile = {
                        "nik" : user['nik'],
                        "nama" : user['nama'],
                        "password" : user['password']
                    }
                    return jsonify(profile)
                else:
                    profile = {
                        "nik" : user['nik'],
                        "password" : user['password']
                    }
                    return jsonify(profile)
            else:
                return jsonify({"status":"nik dan password tidak sesuai"}), 401
        else:
            return jsonify({"status":"user belum terdaftar"}), 401
    else:
        return jsonify({"status":"nik tidak terdaftar"}), 401

if __name__ == '__main__':
    app.run(debug=True)
