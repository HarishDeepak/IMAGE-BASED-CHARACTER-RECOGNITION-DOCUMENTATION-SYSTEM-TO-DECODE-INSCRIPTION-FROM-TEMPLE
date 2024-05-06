import os
import subprocess

os.chdir('/usr/share/tesseract-ocr/4.00/tessdata')
os.system('sudo rm -rf atam.traineddata')
os.system('ls')
os.system('sudo cp ~/fypAncientTamil/trainoutput/atam.traineddata /usr/share/tesseract-ocr/4.00/tessdata/atam.traineddata')
os.system('ls')