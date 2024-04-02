import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
from shutil import copyfile

def cutMute(arr_n):
    idx_f = 0
    while True:
        if arr_n[idx_f]<0.05:
            pass
        else:
            break
        idx_f+=1
        
    idx_f-=500
    
    
    idx_l = len(arr_n)-1
    while True:
        if arr_n[idx_l]<0.05:
            pass
        else:
            break
        idx_l-=1
        
    idx_l+=500
    
    return arr_n[idx_f:idx_l]

def wav2png(file_wav,file_png):
    y, sr = librosa.load(file_wav)
    # y, sr = librosa.load("김유미가3.mp3")
    
    y_trim = y

    
    t = np.arange(0, len(y_trim))


    plt.clf()
    plt.plot(t,y_trim)
    plt.savefig(file_png)
    # plt.grid()
    # plt.show()


# wav2png("animal_en/0/A00.wav","animal_en_w/0/00.png")
path="animal_en"
f_list=os.listdir("animal_en")
for idx,fn in enumerate(f_list):
    fsub_list=os.listdir(f"{path}/{fn}")
    for idx_sub,fs in enumerate(fsub_list):
        file_wav=path+"/"+fn+"/"+fs
        fime_png="animal_en_w/{}/{}".format(fn,fs.replace(".wav",".png"))
        wav2png(file_wav,fime_png)
