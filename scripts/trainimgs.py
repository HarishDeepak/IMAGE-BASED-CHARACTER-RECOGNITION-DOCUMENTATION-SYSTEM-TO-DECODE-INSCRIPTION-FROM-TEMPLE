import os
import subprocess
srcdir = 'data'
destdir = 'trainfiles'
# Removing all previous trained files.
try:
    os.remove('tesseract/tessdata/eng.traineddata')
except OSError:
    pass
files = os.listdir(srcdir)
for item in files:
    if not item.endswith(('.jpg','.png','.box','.jpeg')):
        os.remove(os.path.join(srcdir, item))

# Generating the tuples of filenames
files = os.listdir(srcdir)
jpgs = [x for x in files if x.endswith('.jpg') or x.endswith('.png')]
boxes = [x for x in files if x.endswith('.box')]
trainfiles = list(zip(jpgs, boxes))

# generating TR files and unicode charecter extraction
unicharset = f"unicharset_extractor --output_unicharset ../{destdir}/unicharset "
unicharset_args = f""
errorfiles = []
for image, box in trainfiles:
    unicharset_args += f"{box} "
    if os.path.isfile(f"{destdir}/{image[:-4]}.tr"):
        continue
    try:
        print(image)
        os.system(f"tesseract {srcdir}/{image} {destdir}/{image[:-4]} -l atam --psm 6 nobatch box.train")
    except:
        errorfiles.append((image, box))
os.chdir(srcdir)
print(os.listdir())
os.system(unicharset+unicharset_args)
os.chdir('../')
print(os.listdir())

# Creating font properties file
with open(f"{destdir}/font_properties", 'w') as f:
    f.write("anc 0 0 0 1 0")

# # Getting all .tr files and training
output = '../trainoutput'
trfiles = [f for f in os.listdir(destdir) if f.endswith('.tr')]
os.chdir(destdir)
mftraining = f"mftraining -F font_properties -U unicharset -O {output}/atam.unicharset -D {output}"
cntraining = f"cntraining -D {output}"
for file in trfiles:
    mftraining += f" {file}"
    cntraining += f" {file}"
os.system(mftraining)
os.system(cntraining)

# # Renaming training files and merging them
os.chdir(output)
os.rename('inttemp', 'atam.inttemp')
os.rename('normproto', 'atam.normproto')
os.rename('pffmtable', 'atam.pffmtable')
os.rename('shapetable', 'atam.shapetable')
os.system(f"combine_tessdata atam.")

#finally paste below command in terminal to be able to access our trained data from tesseract terminal
#sudo cp trainoutput/atam.traineddata /usr/share/tesseract-ocr/4.00/tessdata