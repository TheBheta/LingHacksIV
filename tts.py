from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
from mingus.containers import Track, Bar, Note
from mingus.midi import fluidsynth
import crepe


def text_to_music(text):
    tts_mp3 = BytesIO()
    tts = gTTS(text=text, lang="en-uk", slow=False)
    tts.write_to_fp(tts_mp3)
    tts_mp3.seek(0)
    tts_segment = AudioSegment.from_file(tts_mp3, format="mp3")
    tts_wav = tts_segment.export(format="wav")
    print(get_pitches.get_pitches(tts_wav))


    #_play_with_simpleaudio(tts_segment)
    #generate_music.generate_music(tts_segment.duration_seconds)
def generate_music(length):
    note_num = 0
    t = Track() #assume tempo is 120 in 4/4 time
    current_length = len(t) * 2
    while current_length < length:
        t += Bar()
        for i in range(4):
            n = Note()
            n.from_int(note_num%12 + 36)

            note_num+=1
            t.add_notes(n)
        current_length = len(t) * 2
    t.velocity = 200
    print()
    fluidsynth.set_instrument(3, 8)
    fluidsynth.play_Track(t)
    return 1;    

def get_pitches(audio_path):
    """
    Get the pitches of the audio file.
    """
    # Get the pitches of the audio file.
    pitches = crepe.predict_pitch(audio_path)
    return pitches

if __name__ == "__main__":
    print("he")
    text_to_music("The Fitness gram pacer test is a multi-stage i don't know the rest sorry")