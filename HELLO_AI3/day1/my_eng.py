import os
from shutil import copyfile
arr_eng=["GA","NA","DA","RA","MA",
         "BA","SA","AA","JA","CA"]
string="가나다라마바사아가자차"
file_path = 'gana'
list = os.listdir(file_path)
for f in list:
    f_name=f.replace("가", "GA")
    f_name=f_name.replace("나", "NA")
    f_name=f_name.replace("다", "DA")
    f_name=f_name.replace("라", "RA")
    f_name=f_name.replace("마", "MA")
    
    f_name=f_name.replace("바", "BA")
    f_name=f_name.replace("사", "SA")
    f_name=f_name.replace("아", "AA")
    f_name=f_name.replace("자", "JA")
    f_name=f_name.replace("차", "CA")
    print(f_name)
    copyfile('gana/{}'.format(f),'gana_eng/{}'.format(f_name))