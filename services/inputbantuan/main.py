#input user profile for social assistance service
from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore
import datetime

#add firebase credentials to the app
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.Client()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def add_user():
    #get request form
    nama = request.form.get("nama")
    nik = request.form.get("nik")
    tgl_lahir = request.form.get("tgl lahir")
    jml_tanggungan = request.form.get("tanggungan")
    pendidikan = request.form.get("pendidikan")
    profesi = request.form.get("profesi")
    status = request.form.get("status")
    gaji = request.form.get("gaji")
    kota = request.form.get("kota")
    kecamatan = request.form.get("kecamatan")
    kelurahan = request.form.get("kelurahan")
    rt = request.form.get("rt")
    rw = request.form.get("rw")
    alamat = request.form.get("alamat")
    bantuan = request.form.get("bantuan")
    tahap = request.form.get("tahap")
    kesehatan = request.form.get("kesehatan")
    atap = request.form.get("atap")
    dinding = request.form.get("dinding")
    lantai = request.form.get("lantai")
    penerangan = request.form.get("penerangan")
    air = request.form.get("air")
    luas_rumah = request.form.get("luas rumah")

    #assign current assistance name
    now = datetime.datetime.now()
    current_assistance = str(now.year) + "-" + bantuan + "-" + tahap

    #get user data
    doc_ref = db.collection(u'users').document(nik)
    doc = doc_ref.get()
    #check if user already exists
    if doc.exists:
        #check if nik has already signed
        return jsonify({"status":"nik sudah terdaftar"})
    else:
        #add user to the database
        doc_ref.set({
            u'nama' : nama,
            u'nik' : nik,
            u'tgl lahir' : tgl_lahir,
            u'tanggungan' : jml_tanggungan,
            u'pendidikan' : pendidikan,
            u'profesi' : profesi,
            u'status' : status,
            u'gaji' : gaji,
            u'kota' : kota,
            u'kecamatan' : kecamatan,
            u'kelurahan' : kelurahan,
            u'rt' : rt,
            u'rw' : rw,
            u'alamat' : alamat,
            u'bantuan' : {
                current_assistance : {
                    u'jenis' : bantuan,
                    u'tahap' : tahap,
                    u'status' : u'pengajuan'
                }
            },
            u'kesehatan' : kesehatan,
            u'atap' : atap,
            u'dinding' : dinding,
            u'lantai' : lantai,
            u'penerangan' : penerangan,
            u'air' : air,
            u'luas rumah' : luas_rumah
        })
        return jsonify({"status":"nik telah terdaftar"})

if __name__ == '__main__':
    app.run(debug=True)
