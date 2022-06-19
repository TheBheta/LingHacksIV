from gtts import gTTS
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
from mingus.containers import Track, Bar, Note
from mingus.midi import fluidsynth
import mingus.core.chords as chords
import parselmouth 
import random


fluidsynth.init("soundfonts/wii.sf2")

def text_to_music(text):
    tts_mp3 = BytesIO()
    tts = gTTS(text=text, lang="en-uk", slow=False)
    tts.write_to_fp(tts_mp3)
    tts_mp3.seek(0)
    tts_segment = AudioSegment.from_file(tts_mp3, format="mp3")
    tts_wav = tts_segment.export("recordings/sound.wav", format="wav")
    snd = parselmouth.Sound("recordings/sound.wav")
    pitch = snd.to_pitch(0.5)


    _play_with_simpleaudio(tts_segment - 20)
    generate_music(tts_segment.duration_seconds, pitch)
    return 1;

def generate_music(length, pitches):
    note_num = 0
    t = Track() #assume tempo is 120 in 4/4 time
    current_length = len(t) * 2
    while current_length < length + 4:
        t += Bar()
        for i in range(4):
            n = Note()
            if note_num < len(pitches) and pitches[note_num].selected.frequency > 0:
                try:
                    n.from_hertz(pitches[note_num].selected.frequency)
                except:
                    print("invalid frequency: " + str(pitches[note_num].selected.frequency))
                    n.from_hertz(440)
            else:
                n.from_hertz(440)
            note_num+=1
            beats = 0
            while (note_num + beats < len(pitches) and pitches[note_num + beats].selected.frequency == 0):
                beats+=1

            possible_notes = [n, chords.major_triad(n.name), chords.augmented_triad("C")]
            choice = 0
            if n.to_hertz() < 440:
                choice = choice = random.randint(1, 2)
            else: 
                choice = 0
            t.add_notes(possible_notes[choice], (1 + beats + choice))    

        current_length = len(t) * 2
    t.velocity = 300
    fluidsynth.set_instrument(3, 8)
    fluidsynth.play_Track(t)
    return 1;    


f = open("sampletext.txt", "r")
txt = " ".join(f.readlines())
print("grabbed text")
text_to_music(txt)