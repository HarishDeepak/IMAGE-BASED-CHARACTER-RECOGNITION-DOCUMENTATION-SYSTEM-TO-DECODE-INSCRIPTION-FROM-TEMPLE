import os
#open jtesseditor
os.chdir('/home/shangavelan/jTessBoxEditor-2.5.0/jTessBoxEditor')
print(os.listdir())
os.system('java -Xms128m -Xmx1024m -jar jTessBoxEditor.jar')