import speech_recognition as sr
import pyttsx3
from transformers import pipeline

# Training data and responses
training_data = [
    {"intent": "greeting", "text": "Hi!"},
    {"intent": "greeting", "text": "Hello there!"},
    {"intent": "greeting", "text": "Hey! How can I assist you today?"},
    {"intent": "greeting", "text": "Greetings!"},
    {"intent": "greeting", "text": "Good day!"},
    {"intent": "greeting", "text": "Hello! What can I do for you?"},
    {"intent": "greeting", "text": "Hi there! How can I help?"},
    {"intent": "greeting", "text": "Hey! How can I assist you today?"},
    {"intent": "greeting", "text": "Hi! How can I help?"},
    {"intent": "greeting", "text": "Hello! How can I assist you today?"},
    {"intent": "goodbye", "text": "Goodbye! Have a great day!"},
    {"intent": "goodbye", "text": "Bye! Take care!"},
    {"intent": "goodbye", "text": "See you later!"},
    {"intent": "goodbye", "text": "Farewell! Have a good one!"},
    {"intent": "goodbye", "text": "Goodbye! Have a wonderful day!"},
    {"intent": "goodbye", "text": "Take care! See you soon!"},
    {"intent": "goodbye", "text": "Bye! Have a great day ahead!"},
    {"intent": "goodbye", "text": "Take care! See you around!"},
    {"intent": "goodbye", "text": "Goodbye! Until next time!"},
    {"intent": "thanks", "text": "Thanks! I appreciate your help."},
    {"intent": "thanks", "text": "Thank you! You've been very helpful."},
    {"intent": "thanks", "text": "Thanks a lot!"},
    {"intent": "thanks", "text": "Thank you! I'm grateful for your assistance."},
    {"intent": "thanks", "text": "Thanks a bunch! You're awesome."},
    {"intent": "thanks", "text": "Thanks so much!"},
    {"intent": "thanks", "text": "Thank you very much! I really appreciate it."},
    {"intent": "thanks", "text": "Thanks a million! You've been amazing."},
    {"intent": "thanks", "text": "Thanks a ton!"},
    {"intent": "apply_job", "text": "How do I apply for a job?"},
    {"intent": "apply_job", "text": "What is the process to apply for a job?"},
    {"intent": "apply_job", "text": "Can you tell me how to apply for a job?"},
    {"intent": "apply_job", "text": "I want to apply for a job. What should I do?"},
    {"intent": "apply_job", "text": "How can I submit my application for a job?"},
    {"intent": "apply_job", "text": "Can you guide me through the application process?"},
    {"intent": "apply_job", "text": "What are the steps to apply for a job?"},
    {"intent": "apply_job", "text": "How do I go about applying for a job?"},
    {"intent": "apply_job", "text": "Where can I find the job application form?"},
    {"intent": "deadline", "text": "When is the last date to apply for job X?"},
    {"intent": "deadline", "text": "What is the deadline for job Y?"},
    {"intent": "deadline", "text": "Can you tell me the last date for job Z?"},
    {"intent": "deadline", "text": "What is the application deadline for a software engineer position?"},
    {"intent": "deadline", "text": "When do applications close for marketing roles?"},
    {"intent": "deadline", "text": "When is the deadline for submitting applications for the data analyst role?"},
    {"intent": "deadline", "text": "Could you please let me know the final submission date for the sales job?"},
    {"intent": "deadline", "text": "When is the last date to apply for a content creation job?"},
    {"intent": "deadline", "text": "What is the deadline for applying to this internship?"},
    {"intent": "criteria", "text": "What are the eligibility criteria for a software engineer role?"},
    {"intent": "criteria", "text": "Can you tell me the qualifications needed for a marketing position?"},
    {"intent": "criteria", "text": "What skills are required for a data analyst job?"},
    {"intent": "criteria", "text": "What are the requirements for a sales position?"},
    {"intent": "criteria", "text": "What qualifications do I need for a content creation job?"},
    {"intent": "criteria", "text": "Could you explain the eligibility criteria for this internship?"},
    {"intent": "criteria", "text": "What educational background is required for this role?"},
    {"intent": "criteria", "text": "Can you provide details about the qualifications needed for this job?"},
    {"intent": "criteria", "text": "What experience is necessary for this position?"},
    {"intent": "criteria", "text": "What certifications are required for this role?"},
    {"intent": "job_query", "text": "Tell me more about the roles available at your company."},
    {"intent": "job_query", "text": "What job opportunities do you have?"},
    {"intent": "job_query", "text": "Can you give me details about the job openings?"},
    {"intent": "job_query", "text": "I'm interested in learning about the different job roles."},
    {"intent": "job_query", "text": "Could you provide information about the positions available?"},
    {"intent": "job_query", "text": "What types of jobs are currently open?"},
    {"intent": "job_query", "text": "Where can I find information about job roles and responsibilities?"},
    {"intent": "job_query", "text": "Can you describe the various job descriptions?"},
    {"intent": "job_query", "text": "What kinds of job opportunities are there at your company?"},
    {"intent": "job_query", "text": "What positions are currently hiring?"},
    {"intent": "interview_process", "text": "What is the interview process like?"},
    {"intent": "interview_process", "text": "Can you explain the steps in the interview process?"},
    {"intent": "interview_process", "text": "How does your company conduct interviews?"},
    {"intent": "interview_process", "text": "Could you provide details about the interview rounds?"},
    {"intent": "interview_process", "text": "What can I expect during the interview process?"},
    {"intent": "interview_process", "text": "How are interviews conducted for different positions?"},
    {"intent": "interview_process", "text": "Can you describe the interview procedure?"},
    {"intent": "interview_process", "text": "What stages are there in the interview process?"},
    {"intent": "interview_process", "text": "How do you conduct interviews for various job roles?"},
    {"intent": "interview_process", "text": "What are the typical interview questions asked?"},
    {"intent": "salary", "text": "What is the salary range for this position?"},
    {"intent": "salary", "text": "Could you tell me about the compensation package?"},
    {"intent": "salary", "text": "What are the salary details for this job?"},
    {"intent": "salary", "text": "What is the pay scale for this role?"},
    {"intent": "salary", "text": "Can you provide information about the salary package?"},
    {"intent": "salary", "text": "How much does this position pay?"},
    {"intent": "salary", "text": "Can you give me an idea about the salary structure?"},
    {"intent": "salary", "text": "What is the remuneration offered for this job?"},
    {"intent": "salary", "text": "What are the monetary benefits for this position?"},
    {"intent": "salary", "text": "Could you explain the salary and benefits package?"},
    {"intent": "location", "text": "Where is the job located?"},
    {"intent": "location", "text": "What are the job locations for this position?"},
    {"intent": "location", "text": "Can you tell me where the job is based?"},
    {"intent": "location", "text": "What are the work locations available?"},
    {"intent": "location", "text": "Where will I be working if I get this job?"},
]

responses = {
    "greeting": "Hello! How can I help you?",
    "goodbye": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Happy to help!",
    "apply_job": "To apply for a job, please visit our careers page and follow the instructions to submit your application.",
    "deadline": "The deadline for applications varies by job. Please check the specific job listing on our website for the most accurate information.",
    "criteria": "The eligibility criteria for each job are listed in the job description on our careers page.",
    "job_query": "You can find more information about job roles and responsibilities in the job description on our careers page.",
    "interview_process": "The interview process typically involves multiple rounds, including a phone screen and in-person interviews. Details will be provided if you are shortlisted.",
    "salary": "Salary information is typically provided in the job listing. Compensation varies by role and experience.",
    "location": "Job locations are specified in each job posting. Please refer to the job listing on our careers page.",
    "benefits": "We offer a comprehensive benefits package, including health insurance, retirement plans, and more. Details are provided during the hiring process."
}

# Initialize speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Load the NLP model for intent classification
nlp = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, my speech service is down.")
            return ""

# Function to classify intent
def classify_intent(text):
    intents = [item["intent"] for item in training_data]
    results = nlp(text, candidate_labels=intents)
    return results["labels"][0]

# Function to respond based on the intent
def respond(intent):
    response = responses.get(intent, "Sorry, I don't understand.")
    print(f"AI: {response}")
    tts_engine.say(response)
    tts_engine.runAndWait()

# Main conversation loop
def main():
    while True:
        text = recognize_speech()
        if not text:
            continue

        intent = classify_intent(text)
        respond(intent)

        if intent == "goodbye":
            break

if __name__ == "__main__":
    main()
