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

        #assign user data to profile dict
        profile = {
            u'nik' : user['nik'],
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
            u'alamat' : user['alamat'],
            u'kesehatan' : user['kesehatan'],
            u'atap' : user['atap'],
            u'dinding' : user['dinding'],
            u'lantai' : user['lantai'],
            u'penerangan' : user['penerangan'],
            u'air' : user['air'],
            u'luas_rumah' : user['luas_rumah']
        }

        #add rt and rw field if keys exists
        if 'rt' and 'rw' in user:
            profile['rt'] = user['rt']
            profile['rw'] = user['rw']

        #add penerangan field if key exists
        if 'penerangan' in user:
            profile['penerangan'] = user['penerangan']

        #add bantuan field if key exists
        if 'bantuan' in user:
            bantuan = user['bantuan']
            #get the latest bantuan
            current_bantuan = bantuan[-1]

            profile['bantuan'] = current_bantuan['jenis']
            profile['status_bantuan'] = current_bantuan['status']

            #add validasi field if current bantuan already validated
            if 'validasi' in current_bantuan:
                profile['validasi'] = current_bantuan['validasi']
                return jsonify(profile)

            else:
                return jsonify(profile)
        else:
            return jsonify(profile)

    else:
        return jsonify({"status":"nik tidak terdaftar"}), 401

if __name__ == '__main__':
    app.run(debug=True)
