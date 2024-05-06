trainining code for custom data in tesseract


data : 

        add pre-processed images(jpeg,jpg,tiff,png) here

scripts : 
        
        purge.py  -- use it to clear previously trained files for a fresh start/n
        
        rename.py -- the input images needs to be renames in the format <language>.<font>.exp<i>.png
        
        boxgen.py -- generate box files for our images.
       
        openjTess.py -- open jtessbox editor to edit miss predicted box files
       
        trainimgs.py -- run this train all the images in a cnn network

testout:
        
        output of test.py gets stored here

trainfiles:
        
        contains important train files and properties files necessary for training

trainoutput:
       
        contains the .traindata file and other intermediary output file.
