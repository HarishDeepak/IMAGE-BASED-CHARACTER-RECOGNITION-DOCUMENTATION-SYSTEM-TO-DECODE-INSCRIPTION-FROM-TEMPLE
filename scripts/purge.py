import os
import subprocess
srcdir = 'data'
destdir = 'trainfiles'
outdir = 'trainoutput'
# Removing all previous trained files.
try:
    os.remove('tesseract/tessdata/eng.traineddata')
except OSError:
    pass
files = os.listdir(srcdir)
for item in files:
    if not item.endswith(('.jpg','.png','.box','.jpeg')):
        os.remove(os.path.join(srcdir, item))
files = os.listdir(destdir)
for item in files:
    if not item.endswith(('.jpg')):
        os.remove(os.path.join(destdir, item))
files = os.listdir(outdir)
for item in files:
    if not item.endswith(('.jpg')):
        os.remove(os.path.join(outdir, item))