import os
from shutil import copyfile

f_list=os.listdir("animal")
for idx,fn in enumerate(f_list):
    fsub_list=os.listdir(f"animal/{fn}")
    for idx_sub,fs in enumerate(fsub_list):
        file_old="animal/" + fn + "/" + fs
        lbl = fs[0:1]
        file_wav = "animal_en/"+lbl+"/"+chr(idx+65)+fs
        print(file_old,file_wav)
        copyfile(file_old,file_wav)
    

# os.listdir("animal/")