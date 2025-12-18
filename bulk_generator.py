# @title 🏥 AfyaDoctor: Bulk Medical Record Generator
# @description Scaled synthetic data generation for Garissa County simulation.

import json
import random
import time
from datetime import datetime, timedelta

# --- CONFIGURATION ---
SYSTEM_VERSION = "AfyaDoctor v3.0 (Antigravity-Bulk)"
GARISSA_LOCATIONS = ["Lagdera", "Dadaab", "Fafi", "Balambala", "Ijara", "Garissa Township"]
DISEASE_VECTORS = ["Malaria", "Cholera", "Leishmaniasis (Kala-azar)", "Malnutrition", "Respiratory Infection"]

def query_geosentinel(location):
    """Simulates GEE environmental risk assessment."""
    if location in ["Lagdera", "Dadaab"]:
        return {"risk_level": "HIGH", "factor": "Drought / Dust", "alert": "High PM2.5 & Low NDVI detected."}
    elif location in ["Ijara", "Fafi"]:
        return {"risk_level": "CRITICAL", "factor": "Flood Water", "alert": "Standing water detected (NDWI High). Vector breeding risk."}
    else:
        return {"risk_level": "MODERATE", "factor": "Heat Stress", "alert": "LST (Land Surface Temp) > 35°C."}

def run_logic_core(patient, geo_data):
    """Refined LogicCore reasoning."""
    symptoms = ", ".join(patient['triage_notes']['reported_symptoms'])
    env_risk = geo_data['factor']
    
    if "Water" in env_risk and "fever" in str(symptoms).lower():
        diagnosis = "Presumptive Malaria / Febrile Illness"
        confidence = f"High ({random.randint(85, 94)}%)"
        reasoning = "Symptoms align with Febrile illness; environmental context (standing water) suggests high vector activity."
    elif "Drought" in env_risk and "cough" in str(symptoms).lower():
        diagnosis = "Acute Respiratory Infection (Suspected Dust Pneumonia)"
        confidence = f"Medium ({random.randint(70, 79)}%)"
        reasoning = "Respiratory distress correlates with environmental PM2.5 levels in drought-prone areas."
    elif "Malnutrition" in symptoms or "wasting" in symptoms:
        diagnosis = "Severe Acute Malnutrition"
        confidence = f"High ({random.randint(90, 98)}%)"
        reasoning = "Critical Z-score and physical wasting detected in context of food insecurity."
    elif "watery diarrhea" in str(symptoms).lower():
        diagnosis = "Suspected Cholera / Acute Watery Diarrhea"
        confidence = f"Critical ({random.randint(92, 99)}%)"
        reasoning = "Severe gastrointestinal symptoms in potentially flood-impacted or poor-WASH regions require immediate isolation."
    else:
        diagnosis = "Non-Specific / Laboratory Validation Required"
        confidence = f"Low ({random.randint(30, 50)}%)"
        reasoning = "Signs are non-specific; clinical and environmental data are currently inconclusive."

    return {
        "ai_hypothesis": diagnosis,
        "confidence_score": confidence,
        "reasoning_chain": reasoning,
        "recommended_action": "Conduct RDT / Lab panels and initiate standard care protocol."
    }

def generate_record():
    first_names = ["Ahmed", "Fatuma", "Yussuf", "Amina", "Ibrahim", "Halima", "Mohamed", "Zahra", "Abdi", "Layla"]
    surnames = ["Abdi", "Hassan", "Omar", "Ali", "Farah", "Hussein", "Aden", "Ilyas", "Noor"]
    
    location = random.choice(GARISSA_LOCATIONS)
    age = random.randint(1, 80)
    issue = random.choice(DISEASE_VECTORS)
    
    symptoms = []
    if issue == "Malaria": symptoms = ["High fever", "Chills", "Headache"]
    elif issue == "Cholera": symptoms = ["Severe watery diarrhea", "Dehydration", "Cramps"]
    elif issue == "Leishmaniasis (Kala-azar)": symptoms = ["Prolonged fever", "Enlarged spleen", "Weight loss"]
    elif issue == "Malnutrition": symptoms = ["Visible wasting", "Edema", "Z-score < -3"]
    else: symptoms = ["Cough", "Chest pain", "Fever"]

    # Random timestamp within last 48 hours
    ts = datetime.now() - timedelta(minutes=random.randint(0, 2880))
    
    patient = {
        "patient_id": f"P-{random.randint(10000, 99999)}",
        "timestamp": ts.isoformat(),
        "demographics": {
            "name": f"{random.choice(first_names)} {random.choice(surnames)}",
            "age": age,
            "gender": random.choice(["Male", "Female"]),
            "location": location
        },
        "triage_notes": {
            "chief_complaint": f"Patient presents with {symptoms[0].lower()}.",
            "vitals": f"BP: {random.randint(90,140)}/{random.randint(60,90)}, Temp: {random.randint(36,40)}C",
            "reported_symptoms": symptoms
        }
    }
    
    geo = query_geosentinel(location)
    logic = run_logic_core(patient, geo)
    
    return {
        "patient": patient,
        "environmental_context": geo,
        "ai_analysis": logic,
        "meta": {"processed_by": "Gemini-Antigravity-v3", "batch": "SIM-BATCH-001"}
    }

def main(n=100):
    print(f"🚀 Initializing bulk generation of {n} records...")
    records = [generate_record() for _ in range(n)]
    
    with open("medical_records_bulk.json", "w") as f:
        json.dump(records, f, indent=2)
    
    print(f"✅ Generated {len(records)} records in medical_records_bulk.json")

if __name__ == "__main__":
    main(100)
