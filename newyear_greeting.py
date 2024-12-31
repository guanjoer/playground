import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:
    if "English" in voice.name:
        engine.setProperty('voice', voice.id)
        break


# for index, voice in enumerate(voices):
#     print(f"Voice {index}:")
#     print(f" - ID: {voice.id}")
#     print(f" - Name: {voice.name}")
#     print(f" - Languages: {voice.languages}")



engine.say(
    "Happy New Year 2025! "
    "Let's welcome this wonderful new year with open arms and a heart full of dreams. "
    "May this year bring you immense happiness, success, and endless opportunities. "
    "Remember, every day is a chance to grow, to learn, and to be a better version of yourself. "
    "Let's make 2025 a year to remember! Cheers to new beginnings and limitless possibilities!"
)

print("Happy New Year 2025! \
Let's welcome this wonderful new year with open arms and a heart full of dreams. \
May this year bring you immense happiness, success, and endless opportunities. \
Remember, every day is a chance to grow, to learn, and to be a better version of yourself. \
Let's make 2025 a year to remember! Cheers to new beginnings and limitless possibilities!")


engine.runAndWait()