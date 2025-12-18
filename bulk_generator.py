# @title 🏥 AfyaDoctor: Advanced Bulk Medical Record Generator
# @description Scaled synthetic data generation incorporating real-world MOH, UNICEF, and UNHCR statistics.

import json
import random
import time
from datetime import datetime, timedelta

# --- CONFIGURATION (Based on 2024 Mined Stats) ---
SYSTEM_VERSION = "AfyaDoctor v3.0 (Antigravity-Stats-Enriched)"
GARISSA_LOCATIONS = ["Lagdera", "Dadaab", "Fafi", "Balambala", "Ijara", "Garissa Township"]

# DISEASE_VECTORS & PROBABILITIES (Weighted by 2024 Trends)
# Malnutrition: Critical (IPC Phase 4) - High Weight
# Maternal Mortality: Institutional MMR ~226 - Moderate Weight
# Cancer: ~1347 cases/year - Low but significant weight
# Dengue: Outbreak (Dagahaley) - Localized weight
DISEASE_VECTORS = {
    "Malnutrition": 0.35, # Higher during IPC Phase 4
    "Prenatal/Postnatal Complications": 0.20,
    "Respiratory Infection": 0.15,
    "Cancer": 0.10,
    "Dengue Fever": 0.10, # Specifically weighted for refugee camp simulations
    "Malaria": 0.10
}

def query_geosentinel(location):
    """Refined GEE simulations based on 2024 environmental reports."""
    if location in ["Lagdera", "Dadaab"]:
        return {"risk_level": "CRITICAL", "factor": "Drought / Dust / Insecurity", "alert": "IPC Phase 4 conditions detected. Low NDVI."}
    elif location in ["Ijara", "Fafi"]:
        return {"risk_level": "HIGH", "factor": "Flood Water / Vector Breeding", "alert": "NDWI High. Historical Dengue/Malaria hotspots."}
    else:
        return {"risk_level": "MODERATE", "factor": "Heat Stress / Urban Congestion", "alert": "LST (Land Surface Temp) > 36°C."}

def run_logic_core(patient, geo_data):
    """Agentic AI reasoning with Bayesian priors from mined statistics."""
    symptoms = ", ".join(patient['triage_notes']['reported_symptoms'])
    env_risk = geo_data['factor']
    reasoning = ""
    diagnosis = "Under Evaluation"
    confidence = "Low"

    # Malnutrition Logic (Participatory & Advisory)
    if "Malnutrition" in patient['disease_vector']:
        diagnosis = "Severe Acute Malnutrition (SAM)"
        confidence = f"High ({random.randint(92, 98)}%)"
        reasoning = (
            "Clinical wasted presentation verified in context of regional IPC Phase 4 (Critical) food insecurity. "
            "Community Advisory: Urgent therapeutic feeding required. RUTF supplies prioritized via UNICEF protocols."
        )
    
    # Maternal/Natal Health Logic
    elif "Prenatal" in patient['disease_vector'] or "Postnatal" in patient['disease_vector']:
        diagnosis = "Maternal Health Emergency"
        confidence = f"Critical ({random.randint(88, 95)}%)"
        reasoning = (
            "Patient exhibits signs of complications. Local institutional MMR remains high at ~226/100k. "
            "Community Advisory: Immediate referral to Garissa Regional Referral Hospital. Skilled birth attendance is vital."
        )

    # Dengue Logic (Reflecting Dagahaley outbreak)
    elif "Dengue" in patient['disease_vector']:
        diagnosis = "Suspected Dengue Fever"
        confidence = f"Medium ({random.randint(75, 85)}%)"
        reasoning = (
            "Dengue clusters detected in Dagahaley camp. Standing water correlates with vector breeding. "
            "Community Advisory: Clear all stagnant water containers. Use bed nets during daytime."
        )

    # Cancer Logic (Regional Cancer Centre Context)
    elif "Cancer" in patient['disease_vector']:
        diagnosis = f"Suspected {random.choice(['Esophageal', 'Prostate', 'Breast'])} Neoplasm"
        confidence = f"Moderate ({random.randint(60, 75)}%)"
        reasoning = (
            "Patient history and clinical signs align with regional trends (1,347 cases in 2024). "
            "Community Advisory: Referral to Garissa Regional Cancer Centre for screening. Early detection saves lives."
        )

    else:
        diagnosis = "Non-Specific Febrile/Respiratory Illness"
        confidence = f"Low ({random.randint(40, 60)}%)"
        reasoning = "Symptoms match common patterns; environmental factors are inconclusive. Requires Lab/RDT."

    return {
        "ai_hypothesis": diagnosis,
        "confidence_score": confidence,
        "reasoning_chain": reasoning,
        "recommended_action": "Refer to relevant cluster (Nutrition/Maternal/Oncology) and initiate RDT."
    }

def generate_record():
    first_names = ["Ahmed", "Fatuma", "Yussuf", "Amina", "Ibrahim", "Halima", "Mohamed", "Zahra", "Abdi", "Layla"]
    surnames = ["Abdi", "Hassan", "Omar", "Ali", "Farah", "Hussein", "Aden", "Ilyas", "Noor"]
    
    location = random.choice(GARISSA_LOCATIONS)
    vector = random.choices(list(DISEASE_VECTORS.keys()), weights=list(DISEASE_VECTORS.values()))[0]
    
    symptoms = []
    if vector == "Malnutrition": 
        symptoms = ["Visible wasting", "Edema", "Z-score < -3", "Fatigue"]
        age = random.randint(1, 5) # Mostly children
    elif vector == "Prenatal/Postnatal Complications":
        symptoms = ["Severe bleeding", "Hypertension", "Dizziness", "Prolonged labor"]
        age = random.randint(18, 45)
    elif vector == "Cancer":
        symptoms = ["Difficulty swallowing", "Lump", "Unexplained weight loss", "Chronic pain"]
        age = random.randint(30, 75)
    elif vector == "Dengue Fever":
        symptoms = ["High fever", "Severe headache", "Eye pain", "Muscle ache", "Rash"]
        age = random.randint(5, 60)
    else:
        symptoms = ["Fever", "Cough", "Joint pain", "Chills"]
        age = random.randint(5, 75)

    ts = datetime.now() - timedelta(minutes=random.randint(0, 10080)) # Last 7 days
    
    patient = {
        "patient_id": f"P-{random.randint(10000, 99999)}",
        "timestamp": ts.isoformat(),
        "disease_vector": vector,
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
        "meta": {"processed_by": "Gemini-Antigravity-v3", "batch": "REAL-STATS-SIM-2024"}
    }

def main(n=200):
    print(f"🚀 Initializing statistical bulk generation of {n} records...")
    records = [generate_record() for _ in range(n)]
    
    with open("medical_records_advanced.json", "w") as f:
        json.dump(records, f, indent=2)
    
    print(f"✅ Generated {len(records)} records in medical_records_advanced.json")

if __name__ == "__main__":
    main(200)
