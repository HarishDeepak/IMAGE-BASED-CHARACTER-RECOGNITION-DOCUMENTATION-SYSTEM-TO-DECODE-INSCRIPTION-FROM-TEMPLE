import os
os.chdir('data')
print(os.listdir('./'));
number_of_files = len(os.listdir('./'))

for i in range(0, number_of_files):
   os.system(f"tesseract -l atam atam.anc.exp{i}.jpg atam.anc.exp{i} --psm 6 batch.nochop makebox")

#export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/
#os.system(f"tesseract -l tam atam.anc.exp0.jpg atam.anc.exp0 batch.nochop makebox")
