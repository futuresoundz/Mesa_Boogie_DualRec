import numpy as np
import scipy.io.wavfile as wav

file_path = 'mysound.wav'
rate, data = wav.read(file_path)

volume_boost = 20 
distorted = data * volume_boost


#for i in range(len(distorted)):
   # if distorted[i] > 15000:
      #  distorted[i] = 15000
    #if distorted[i] < -15000:
       # distorted[i] = -15000

distorted = np.clip(distorted, -15000, 15000)

window_size=20
filtered = np.convolve(distorted, np.ones(window_size)/window_size, mode = 'same')

final_sound = filtered + (data * 2)


final_sound = final_sound * 0.5


out = final_sound.astype(np.int16)

wav.write('DISTORTION.wav', rate, out)
