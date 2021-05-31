#check user service
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

    #get user data from database
    doc_ref = db.collection(u'users').document(nik)
    doc = doc_ref.get()
    if doc.exists:
        user = doc.to_dict()
        bantuan = user['bantuan']
        current_bantuan = bantuan[-1]

        #get user data
        profile = {
            u'nama' : user['nama'],
            u'tanggal_lahir' : user['tanggal_lahir'],
            u'tanggungan_keluarga' : user['tanggungan_keluarga'],
            u'pendidikan' : user['pendidikan'],
            u'profesi' : user['profesi'],
            u'status' : user['status'],
            u'gaji' : user['gaji'],
            u'kota_kabupaten' : user['kota_kabupaten'],
            u'kecamatan' : user['kecamatan'],
            u'kelurahan' : user['kelurahan'],
            u'rt' : user['rt'],
            u'rw' : user['rw'],
            u'alamat' : user['alamat'],
            u'kesehatan' : user['kesehatan'],
            u'atap' : user['atap'],
            u'dinding' : user['dinding'],
            u'lantai' : user['lantai'],
            u'penerangan' : user['penerangan'],
            u'air' : user['air'],
            u'luas_rumah' : user['luas_rumah'],
            u'bantuan' : current_bantuan['jenis'],
            u'status' : current_bantuan['status']
        }
        return jsonify(profile)
    else:
        return jsonify({"status":"nik tidak terdaftar"}), 401

if __name__ == '__main__':
    app.run(debug=True)
