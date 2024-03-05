import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Add a document to a collection
doc_ref = db.collection(u'users').document(u'new_user')
doc_ref.set({
    u'first_name': u'John',
    u'last_name': u'Doe',
    u'age': 30
})

print("Document added to Firestore successfully!")
