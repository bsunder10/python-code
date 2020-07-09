import pyttsx3

engine = pyttsx3.init()
ssound = engine.getProperty('voices')
for sound in ssound:
    print('voice')
    print('id  %s' %sound.id)
    print('gender %s' %sound.gender)
    print('**************************')
