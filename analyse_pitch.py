from cmath import pi
import random
import parselmouth 

snd = parselmouth.Sound("C:/Users/Chinmay/Downloads/Gnat.wav")
pitch = snd.to_pitch(0.5)
print(len(pitch))