#validate service
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
def get_validate():
    #get request form
    nik = request.form.get("nik")
    validasi = request.form.get("validasi")

    #get user data from database
    doc_ref = db.collection(u'users').document(nik)
    doc = doc_ref.get()
    user = doc.to_dict()
    if 'bantuan' in user:
        #get the latest bantuan
        bantuan = user['bantuan']
        current_bantuan = bantuan[-1]

        #remove current bantuan
        #this will be added again after update
        doc_ref.update({
            u'bantuan' : firestore.ArrayRemove([current_bantuan])
        })

        #add validation
        current_bantuan['validasi'] = validasi

        #add updated bantuan
        doc_ref.update({
            u'bantuan' : firestore.ArrayUnion([current_bantuan])
        })

        return jsonify({"status":"nik berhasil divalidasi"})

    else:
        return jsonify({"status":"nik belum didaftarkan sebagai calon penerima bantuan"})

if __name__ == '__main__':
    app.run(debug=True)
