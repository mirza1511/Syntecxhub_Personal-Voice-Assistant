# ==========================================================
# Project 1 - Personal Assistant (NO AUDIO LIBS VERSION)
# Works anywhere (Replit / Python / OnlineGDB / PC)
# ==========================================================

import datetime
import webbrowser
import random

assistant_name = "SyntecxHub Assistant"

# Speak function (text only - no pyttsx3)
def speak(text):
    print(f"\n{assistant_name}: {text}")

# Wish user
def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am ready. Type help for commands.")

# Help menu
def show_help():
    speak("You can type these commands:")
    speak("hello, time, date, open google, open youtube, open github, joke, exit")

# Command processor
def process_command(command):
    command = command.lower()

    if "hello" in command:
        speak("Hello! How are you?")

    elif "your name" in command:
        speak("My name is SyntecxHub Assistant.")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + time)

    elif "date" in command:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "google" in command:
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif "youtube" in command:
        speak("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "github" in command:
        speak("Opening GitHub...")
        webbrowser.open("https://github.com")

    elif "joke" in command:
        jokes = [
            "Why do programmers hate nature? Too many bugs.",
            "Why did Python break up? Too many exceptions.",
            "Debugging: Removing bugs you didn’t invite."
        ]
        speak(random.choice(jokes))

    elif "help" in command:
        show_help()

    elif "exit" in command or "bye" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, I didn't understand that.")

    return True


# ================= MAIN PROGRAM =================

wish()

while True:
    try:
        user_command = input("\nYou: ")
        run = process_command(user_command)

        if run == False:
            break

    except KeyboardInterrupt:
        speak("Program stopped.")
        break

    except Exception:
        speak("Some error occurred.")

print("\nCode Executed Successfully")