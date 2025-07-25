# First-Order Logic Knowledge Base
knowledge_base = {
    "flu": {"fever", "cough", "sore_throat"},
    "common_cold": {"sneezing", "runny_nose", "mild_fever"},
    "malaria": {"fever", "chills", "sweating", "headache"},
    "covid19": {"fever", "cough", "shortness_of_breath", "loss_of_taste"},
    "strep_throat": {"sore_throat", "swollen_lymph_nodes", "fever"}
}

# Advice base with at least 3 tips per disease
advice_base = {
    "flu": [
        "Drink plenty of fluids",
        "Get rest",
        "Take antiviral medication if prescribed"
    ],
    "common_cold": [
        "Stay hydrated",
        "Use over-the-counter cold medications",
        "Rest and recover"
    ],
    "malaria": [
        "Seek immediate medical attention",
        "Take prescribed antimalarial drugs",
        "Avoid mosquito bites"
    ],
    "covid19": [
        "Isolate yourself",
        "Monitor oxygen levels",
        "Consult a healthcare provider"
    ],
    "strep_throat": [
        "Take prescribed antibiotics",
        "Avoid sharing utensils",
        "Get plenty of rest"
    ]
}

def get_user_symptoms():
    print("Welcome to HealthBot!")
    print("Enter your symptoms (comma-separated, e.g. fever, cough):")
    user_input = input("Symptoms: ").lower()

    # Clean and split the input
    symptoms = {sym.strip() for sym in user_input.split(",")}
    return symptoms

def infer_disease(user_symptoms):
    possible_diseases = []

    # Check for diseases that match all symptoms
    for disease, symptoms in knowledge_base.items():
        if symptoms.issubset(user_symptoms):
            possible_diseases.append(disease)

    return possible_diseases

def run_chatbot():
    user_symptoms = get_user_symptoms()
    diseases = infer_disease(user_symptoms)

    if diseases:
        print("\nBased on your symptoms, you might have:")
        for disease in diseases:
            print(f"- {disease.title()}")
            print("  Advice:")
            for tip in advice_base[disease]:
                print(f"   • {tip}")
    else:
        print("\nNo matching disease found.")
        print("Please consult a healthcare professional.")

# Run the chatbot
run_chatbot()
