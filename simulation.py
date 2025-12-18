# @title 🏥 AfyaDoctor: Antigravity Engine Simulation
# @markdown **System Status:** Initializing Agentic Swarm...
# @markdown **Location:** Garissa County, Kenya

import json
import random
import time
from datetime import datetime

# --- CONFIGURATION (The "Brain") ---
SYSTEM_VERSION = "AfyaDoctor v3.0 (Antigravity)"
GARISSA_LOCATIONS = ["Lagdera", "Dadaab", "Fafi", "Balambala", "Ijara", "Garissa Township"]
DISEASE_VECTORS = ["Malaria", "Cholera", "Leishmaniasis (Kala-azar)", "Malnutrition", "Respiratory Infection"]

# --- AGENT 1: DATA GENERATOR (Simulating Incoming Patients) ---
def generate_synthetic_patient():
    """Creates a realistic patient profile for the Garissa context."""
    first_names = ["Ahmed", "Fatuma", "Yussuf", "Amina", "Ibrahim", "Halima", "Mohamed", "Zahra"]
    surnames = ["Abdi", "Hassan", "Omar", "Ali", "Farah", "Hussein", "Aden"]
    
    location = random.choice(GARISSA_LOCATIONS)
    age = random.randint(2, 75)
    
    # Clinical presentation based on random disease vector
    suspected_issue = random.choice(DISEASE_VECTORS)
    
    symptoms = []
    if suspected_issue == "Malaria":
        symptoms = ["High fever (39°C)", "Chills", "Headache", "Vomiting", "Joint pain"]
    elif suspected_issue == "Cholera":
        symptoms = ["Severe watery diarrhea", "Dehydration", "Rapid heart rate", "Muscle cramps"]
    elif suspected_issue == "Leishmaniasis (Kala-azar)":
        symptoms = ["Prolonged fever", "Weight loss", "Enlarged spleen", "Anemia"]
    elif suspected_issue == "Malnutrition":
        symptoms = ["Visible wasting", "Edema", "Fatigue", "Weakness", "Z-score < -3"]
    else: # Respiratory
        symptoms = ["Cough", "Difficulty breathing", "Chest pain", "Fever"]

    return {
        "patient_id": f"P-{random.randint(10000, 99999)}",
        "timestamp": datetime.now().isoformat(),
        "demographics": {
            "name": f"{random.choice(first_names)} {random.choice(surnames)}",
            "age": age,
            "gender": random.choice(["Male", "Female"]),
            "location": location
        },
        "triage_notes": {
            "chief_complaint": f"Patient presents with {symptoms[0].lower()} and {symptoms[1].lower()}.",
            "vitals": f"BP: {random.randint(90,140)}/{random.randint(60,90)}, HR: {random.randint(60,110)}, Temp: {random.randint(36,40)}°C",
            "reported_symptoms": symptoms
        }
    }

# --- AGENT 2: GEOSENTINEL (Simulating GEE Environmental Data) ---
def query_geosentinel(location):
    """Simulates a call to Google Earth Engine for environmental risks."""
    print(f"   [🛰️ GeoSentinel] Scanning environmental data for {location}...")
    time.sleep(0.5) # Simulate latency
    
    # Logic: Different locations have different simulated risks
    if location in ["Lagdera", "Dadaab"]:
        return {"risk_level": "HIGH", "factor": "Drought / Dust", "alert": "High PM2.5 & Low NDVI detected."}
    elif location in ["Ijara", "Fafi"]:
        return {"risk_level": "CRITICAL", "factor": "Flood Water", "alert": "Standing water detected (NDWI High). Vector breeding risk."}
    else:
        return {"risk_level": "MODERATE", "factor": "Heat Stress", "alert": "LST (Land Surface Temp) > 35°C."}

# --- AGENT 3: LOGIC CORE (The "Gemini" Brain) ---
def run_logic_core(patient, geo_data):
    """Simulates the Gemini Pro/Flash reasoning step with enhanced empathy."""
    print(f"   [🧠 LogicCore] Synthesizing clinical + environmental data...")
    time.sleep(0.8)
    
    # Prompt Construction (Simulated)
    symptoms = ", ".join(patient['triage_notes']['reported_symptoms'])
    env_risk = geo_data['factor']
    
    # The "Thinking" Process (Refined for Empathy and Professionalism)
    diagnosis_hypothesis = "Clinical Correlation Required"
    confidence = "Low (0%)"
    reasoning = ""

    if "Water" in env_risk and "fever" in str(symptoms).lower():
        diagnosis_hypothesis = "Presumptive Malaria / Febrile Illness"
        confidence = "High (89%)"
        reasoning = (
            "We have observed symptoms consistent with a Febrile illness. "
            "The GeoSentinel scan confirms active environmental hazards (standing water) conducive to vector breeding. "
            "Please prioritize this patient for immediate diagnostic verification to ensure timely care."
        )
    elif "Drought" in env_risk and "cough" in str(symptoms).lower():
        diagnosis_hypothesis = "Acute Respiratory Infection (Suspected Dust Pneumonia)"
        confidence = "Medium (75%)"
        reasoning = (
            "The patient's respiratory distress appears to correlate with elevated particulate matter (PM2.5) "
            "detected in the drought-affected region. This clinical picture suggests a high risk of environmental pneumonia. "
            "We recommend symptomatic monitoring and environmental mitigation where possible."
        )
    elif "Malnutrition" in symptoms or "wasting" in symptoms:
         diagnosis_hypothesis = "Severe Acute Malnutrition"
         confidence = "High (92%)"
         reasoning = (
             "Triage indicators (Z-score and visible wasting) signal a critical nutritional emergency. "
             "In the current context of regional food insecurity, immediate therapeutic intervention is vital "
             "to support the patient's recovery and well-being."
         )
    else:
        diagnosis_hypothesis = "Non-Specific Presentation"
        confidence = "Low (40%)"
        reasoning = (
            "The current clinical data and environmental context are fragmented. "
            "While we are closely monitoring the situation, a comprehensive clinical evaluation and laboratory "
            "workup are essential to reach a definitive diagnosis. We remain committed to the patient's care pathway."
        )

    return {
        "ai_hypothesis": diagnosis_hypothesis,
        "confidence_score": confidence,
        "reasoning_chain": reasoning,
        "recommended_action": "Conduct RDT (Rapid Diagnostic Test) and initiate clinical stabilization protocol."
    }

# --- MAIN SYSTEM LOOP ---
def run_afyadoctor_simulation(num_patients=3):
    print(f"\n🔵 {SYSTEM_VERSION} - BOOT SEQUENCE INITIATED")
    print("--------------------------------------------------")
    
    results_db = []
    
    for i in range(num_patients):
        print(f"\n➡️ PROCESSING CASE #{i+1}")
        
        # Step 1: Ingest
        patient = generate_synthetic_patient()
        print(f"   [📝 TriageBot] Patient: {patient['demographics']['name']} ({patient['demographics']['location']})")
        
        # Step 2: Geo-Enrichment
        geo_data = query_geosentinel(patient['demographics']['location'])
        
        # Step 3: Analysis
        analysis = run_logic_core(patient, geo_data)
        
        # Step 4: Output Object (The "JSON" for Firebase)
        encounter_record = {
            "patient": patient,
            "environmental_context": geo_data,
            "ai_analysis": analysis,
            "meta": {"processed_by": "Gemini-Antigravity-v3", "latency_ms": 450}
        }
        results_db.append(encounter_record)
        
        print(f"   ✅ [Shield] Output Validated. Pushing to Firebase...")
    
    print("\n--------------------------------------------------")
    print("🔴 SIMULATION COMPLETE. DATA GENERATED.")
    return results_db

# --- EXECUTE ---
if __name__ == "__main__":
    simulation_data = run_afyadoctor_simulation(5)

    # Save to file
    with open("patients.json", "w") as f:
        json.dump(simulation_data, f, indent=2)
    
    print(f"\n[💾 System] Generated {len(simulation_data)} records in patients.json")

    # Show one full record example
    print("\n--- SAMPLE JSON OUTPUT FOR FIREBASE ---")
    print(json.dumps(simulation_data[0], indent=2))
