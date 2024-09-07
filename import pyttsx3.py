import pyttsx3
import pyautogui
import speech_recognition as sr
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something:")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
            return ""
        except sr.RequestError as e:
            print("Error fetching results; {0}".format(e))
            return ""
def main():
    
    print("TEXT TO SPEECH SOFTWARE ")
    input_text = input("Enter text to convert to speech: ")
    text_to_speech(input_text)
    print("REVERSED TEXT : ")
    input_text1 = input_text[::-1]
    print(input_text1)
    print("SPEECH TO TEXT SOFTWARE ")
    output_text = speech_to_text()
    if output_text:
        print("Converted speech to text:", output_text)
    else:
        print("No speech recognized.")
    print("REVERSED TEXT : ")
    output_text1 = output_text[::-1]
    print(output_text1)
    

if __name__=="__main__":
    main()