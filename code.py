import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Function to convert voice to text
def voice_to_text():
    # Use microphone as source for input
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        # Listen to the user's input from the microphone
        audio = r.listen(source)

        try:
            print("Recognizing...")
            # Convert speech into text using Google Speech Recognition
            text = r.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Sorry, the service is not available.")

# Call the function
voice_to_text()
# List all available microphone devices
print(sr.Microphone.list_microphone_names())
