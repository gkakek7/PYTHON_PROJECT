import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

def cutMute(arr_n):
    idx_f = 0
    while True:
        if arr_n[idx_f]<0.01:
            pass    
        else:
            break
        idx_f+=1
        
    idx_f-=500
    
    
    idx_l = len(arr_n)-1
    while True:
        if arr_n[idx_l]<0.01:
            pass
        else:
            break
        idx_l-=1
        
    idx_l+=500
    
    return arr_n[idx_f:idx_l]

def wav2jpg(file_wav,file_jpg):
    y, sr = librosa.load(file_wav)
    
    y_trim = cutMute(y)
    
    t = np.arange(0, len(y_trim))
    print(sr)
    print(y_trim)
    
    plt.clf()
    plt.specgram(y_trim)
    plt.savefig(file_jpg)

# wav2jpg("animal_en/0/M01.wav","animal_en_s/0/M01.jpg")

path = "animal_en"
f_list = os.listdir(path)

for idx,fn in enumerate(f_list):
    fsub_list = os.listdir("animal_en/{}".format(fn))
    for idx_s,fs in enumerate(fsub_list):
        file_wav = "animal_en/{}/{}".format(fn,fs)
        file_jpg = "animal_en_s/{}/{}".format(fn,fs.replace(".wav",".jpg"))
        print(file_wav,file_jpg)
        wav2jpg(file_wav,file_jpg)











