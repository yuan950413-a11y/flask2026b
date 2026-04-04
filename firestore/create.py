import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firestore/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "吳育安",
  "mail": "yuan.950413@gmail.com",
  "lab": 801
}

doc_ref = db.collection("靜宜資管").document("Yu-An Wu")
doc_ref.set(doc)