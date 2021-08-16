import speech_recognition as sr

r = sr.Recognizer()
filename = "audios/Test-job-for-transcriber.wav"

with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    try:
        with open('example.txt', 'a') as f:
            f.write(text)
            f.write('\n')
            print(text)
    except:
        print('imekata mzae')