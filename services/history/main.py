#history service
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
def get_history():
    #get request form
    nik = request.form.get("nik")

    #get user data from database
    doc_ref = db.collection(u'users').document(nik)
    doc = doc_ref.get()
    user = doc.to_dict()

    #return field bantuan as history of bantuan
    bantuan = user["bantuan"]
    history = []
    for data in bantuan:
        #check if bantuan already validated
        #only return bantuan that already validated
        if 'validasi' in data:
            validasi = data['validasi']
            if validasi != None:
                history.append(data)
    return jsonify(history)

if __name__ == '__main__':
    app.run(debug=True)
