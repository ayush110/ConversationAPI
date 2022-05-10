from distutils.errors import UnknownFileError
import speech_recognition as sr
print(sr.__version__)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        print("please say something...")
        print(r)
        audio = r.listen(source)
        print("recognizing now...")
        said = ""
        
        try:
            said = r.recognize_google(audio)
            
        except UnknownFileError as e:
            print("yes: " + str(e))
        except Exception as e:
            print("Exception: " + str(e))

    return said
