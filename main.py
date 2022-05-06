#import useful libraries
from pydub import AudioSegment
import speech_recognition as sr

#Song type conversion
#Initial song name.type
src = 'Legacy.mp3'
#Final song name.type
dest = "Legacy.wav"

sound = AudioSegment.from_mp3(src)
sound.export(dest, format="wav")

audio_file = sr.AudioFile('Legacy.wav')

#show file type
print(type(audio_file))

r =sr.Recognizer()

with audio_file as source:
    audio_text = r.record(source)

    text = r.recognize_google(audio_text)

print(text)
