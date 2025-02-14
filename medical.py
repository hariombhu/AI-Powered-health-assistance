import streamlit as st
import openai
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Define medical-specific response logic
def medical_health_assistant(user_input):
    user_input = user_input.lower()
    
    if "symptom" in user_input:
        return "It looks like you're experiencing some symptoms. Please consult a healthcare professional for proper diagnosis."
    elif "doctor" in user_input:
        return "Would you like assistance in finding a doctor or scheduling an appointment?"
    elif "prescription" in user_input or "medication" in user_input:
        return "Ensure you take your prescribed medications as directed. For any concerns, consult your healthcare provider."
    elif "vaccine" in user_input or "vaccination" in user_input:
        return "Vaccines are crucial for preventing diseases. Please consult your healthcare provider for vaccination schedules and recommendations."
    elif "diet" in user_input or "nutrition" in user_input:
        return "A balanced diet is essential for maintaining good health. Consider consulting a nutritionist for personalized advice."
    elif "exercise" in user_input or "fitness" in user_input:
        return "Regular exercise contributes to overall well-being. Aim for at least 30 minutes of physical activity daily."
    elif "mental health" in user_input or "stress" in user_input:
        return "Mental health is just as important as physical health. If you're feeling stressed or anxious, consider speaking with a mental health professional."
    elif "emergency" in user_input or "urgent care" in user_input:
        return "If this is a medical emergency, please call emergency services or go to the nearest hospital immediately."
    elif "allergy" in user_input or "reaction" in user_input:
        return "Allergic reactions can be serious. If you are experiencing severe symptoms, seek medical attention immediately."
    elif "blood pressure" in user_input or "hypertension" in user_input:
        return "Maintaining a healthy blood pressure is important. Regular check-ups and a balanced diet can help manage hypertension."
    elif "diabetes" in user_input or "sugar level" in user_input:
        return "Managing diabetes requires a healthy diet, regular exercise, and medication as prescribed by your doctor."
    elif "headache" in user_input or "migraine" in user_input:
        return "Headaches can have many causes. Rest, hydration, and stress reduction can help. If headaches persist, consult a doctor."
    elif "fever" in user_input:
        return "A fever can indicate an infection. Stay hydrated and rest. If the fever is high or persistent, seek medical advice."
    elif "cold" in user_input or "flu" in user_input:
        return "Colds and flu are common. Stay hydrated, rest, and consider over-the-counter remedies. See a doctor if symptoms worsen."
    elif "heart" in user_input or "cardiac" in user_input:
        return "Heart health is critical. Regular check-ups, a balanced diet, and exercise can help prevent cardiac issues."
    elif "cancer" in user_input:
        return "Cancer treatment varies depending on the type and stage. Consult an oncologist for proper diagnosis and treatment options."
    elif "pregnancy" in user_input or "prenatal" in user_input:
        return "Pregnancy care is crucial for both mother and baby. Regular check-ups and a balanced diet can help ensure a healthy pregnancy."
    elif "asthma" in user_input or "breathing problem" in user_input:
        return "Asthma management includes avoiding triggers and using prescribed medications. Consult your doctor for personalized advice."
    elif "arthritis" in user_input or "joint pain" in user_input:
        return "Arthritis can cause joint pain and stiffness. Regular exercise, a healthy diet, and medication can help manage symptoms."
    elif "stroke" in user_input or "paralysis" in user_input:
        return "Stroke symptoms require immediate medical attention. Rehabilitation and lifestyle changes can help in recovery."
    elif "skin problem" in user_input or "dermatology" in user_input:
        return "Skin conditions vary widely. Consult a dermatologist for accurate diagnosis and treatment."
    elif "infection" in user_input or "antibiotics" in user_input:
        return "Infections require proper treatment, often with antibiotics. Consult a doctor to determine the appropriate medication."
    else:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"]

# Streamlit web app interface
def main():
    st.title("Medical Health Assistant Chatbot")
    
    # User input field
    user_input = st.text_input("How can I help with your medical queries today?", "")
    
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = medical_health_assistant(user_input)
            st.write("Medical Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()