#change password service for admin app
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
def change_password():
    #get request form
    email = request.form.get("email")
    current_password = request.form.get("currentpass")
    new_password = request.form.get("newpass")

    #get user data from database
    doc_ref = db.collection(u'admins').document(email)
    doc = doc_ref.get()
    #update existing password
    admin = doc.to_dict()
    if admin["password"] == current_password:
        doc_ref.update({
            u'password' : new_password
        })
        return jsonify({"status":"update password berhasil"})
    else:
        return jsonify({"status":"password salah"})

if __name__ == '__main__':
    app.run(debug=True)
