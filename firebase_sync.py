import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

def sync_to_firestore(json_file="medical_records_bulk.json", key_file="firebase-key.json"):
    """Pushes synthetic patient records to Firestore."""
    
    if not os.path.exists(key_file):
        print(f"❌ Error: {key_file} not found.")
        print("Please download your Service Account JSON from the Firebase Console and save it as 'firebase-key.json' in this folder.")
        return

    print("🚀 Initializing Firebase...")
    cred = credentials.Certificate(key_file)
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    print(f"📂 Loading data from {json_file}...")
    with open(json_file, "r") as f:
        records = json.load(f)

    print(f"📡 Syncing {len(records)} records to 'patients' collection...")
    
    # We use a batch for efficiency
    batch = db.batch()
    for i, record in enumerate(records):
        doc_id = record["patient"]["patient_id"]
        doc_ref = db.collection("patients").document(doc_id)
        batch.set(doc_ref, record)
        
        # Firestore batch supports up to 500 writes
        if (i + 1) % 500 == 0:
            batch.commit()
            batch = db.batch()

    batch.commit()
    print("✅ Sync complete. Data is now live in Firestore!")

if __name__ == "__main__":
    sync_to_firestore()
