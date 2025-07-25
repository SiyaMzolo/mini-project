Healthcare Chatbot
This is a simple console-based Healthcare Chatbot designed to infer potential diseases based on user-provided symptoms and offer basic advice.

Features:
Symptom-based Disease Inference: Identifies potential diseases by matching user-entered symptoms against a predefined knowledge base.

Basic Health Advice: Provides general advice for identified diseases.

User-Friendly Interface: Simple command-line interaction.

How it Works?
The chatbot operates on a first-order logic knowledge base. It takes a list of symptoms from the user, then compares these symptoms to sets of symptoms associated with various diseases. If a disease's entire set of symptoms is present in the user's input, that disease is considered a possible match. For each matched disease, relevant health advice is displayed.

Knowledge Base:
The knowledge_base dictionary stores diseases and their associated symptoms. Each disease is a key, and its value is a set of symptoms.

knowledge_base = {
    "flu": {"fever", "cough", "sore_throat"},
    "common_cold": {"sneezing", "runny_nose", "mild_fever"},
    "malaria": {"fever", "chills", "sweating", "headache"},
    "covid19": {"fever", "cough", "shortness_of_breath", "loss_of_taste"},
    "strep_throat": {"sore_throat", "swollen_lymph_nodes", "fever"}
}

Advice Base:
The advice_base dictionary provides health tips for each disease. Each disease is a key, and its value is a list of advice strings.

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

Getting Started
Prerequisites:
You only need Python 3 installed on your system.

Installation:
No special installation steps are required beyond having Python. Simply save the provided code as a .py file (e.g., chatbot.py).

How to Run?
Save the code into a file named chatbot.py.

Open your terminal or command prompt.

Navigate to the directory where you saved chatbot.py.

Run the script using Python:

python chatbot.py

Usage:
Once you run the script, the chatbot will prompt you to enter your symptoms.

Welcome to HealthBot!
Enter your symptoms (comma-separated, e.g. fever, cough):
Symptoms: fever, cough, sore throat

Enter your symptoms separated by commas. The chatbot will then process your input and display any matching diseases along with relevant advice. If no matching diseases are found, it will advise you to consult a healthcare professional.

Example Interaction:

Welcome to HealthBot!
Enter your symptoms (comma-separated, e.g. fever, cough):
Symptoms: fever, cough, sore throat

Based on your symptoms, you might have:
- Flu
  Advice:
   • Drink plenty of fluids
   • Get rest
   • Take antiviral medication if prescribed

Contributing
Feel free to fork this repository and contribute by:

Adding more diseases and symptoms to the knowledge_base.

Expanding the advice in the advice_base.

Improving the user interface or adding new features.
