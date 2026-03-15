import speech_recognition as sr
import datetime
import subprocess
import pywhatkit # type: ignore
import pyttsx3
import webbrowser

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
recognizer=sr.Recognizer()

def cmd():
    with sr.Microphone() as source:
        print('clearing backgroud noises..please wait')
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print('ask me anything')
        recordedaudio=recognizer.listen(source)
        try:
            command=recognizer.recognize_google(recordedaudio, language='en-in')
            print('you said: ' + command)
        except Exception as ex:
            print(ex)
            return

    if command:
        if 'chrome' in command.lower():
            a = 'opening google chrome'
            engine.say(a)
            engine.runAndWait()
            program = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            subprocess.Popen([program])
        elif 'open youtube' in command.lower():
            a = 'opening YouTube'
            engine.say(a)
            engine.runAndWait()
            webbrowser.open('https://www.youtube.com')
        elif 'time' in command.lower():
            
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            engine.say('current time is ' + time)
            engine.runAndWait()
        elif 'play' in command.lower():
            song = command.lower().replace('play', '').strip()
            engine.say('playing ' + song)
            engine.runAndWait()

            pywhatkit.playonyt(song)


if __name__ == "__main__":
    while True:
        cmd()
            