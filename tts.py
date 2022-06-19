from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import mingus

text_object = gTTS(text="Hello, how are you doing today?", lang="en", slow=False)
text_object.save("recordings/example.wav")

def text_to_music(text):
    tts_fp = BytesIO()
    tts = gTTS(text=text, lang="en", slow=False)
    tts.write_to_fp(tts_fp)
    tts_fp.seek(0)
    tts_segment = AudioSegment.from_file(tts_fp, format="mp3")



    play(tts_segment)
    

def generate_music(length):
    print("hi") 




text_to_music("Hello, how are you doing today?")