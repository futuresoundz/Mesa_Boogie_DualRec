import numpy as np
import scipy.io.wavfile as wav

file = 'clean_guitar.wav'
rate, data = wav.read(file)

volume_boost = 20 
distorted = data * volume_boost


for i in range(len(distorted)):
    if distorted[i] > 15000:
        distorted[i] = 15000
    if distorted[i] < -15000:
        distorted[i] = -15000


final_sound = distorted + (data * 2)


final_sound = final_sound * 0.5


out = final_sound.astype(np.int16)

wav.write('BOOGIE_DISTORTION_V1.wav', rate, out)
