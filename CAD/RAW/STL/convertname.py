import os
import glob 

stlfiles = []
prefix = 'Assembly_ALL_PARTS_FOR_EXPORT_'
for file in glob.glob("*.stl"):
    print(file)
    # remove prefix
    if len(file.split(prefix))>1:
        myfilename = file
        myfilename_split = myfilename.split(prefix)[-1].split('_')
        myfilename_new = ''
        for i in range(len(myfilename_split)-1):
            myfilename_new += (myfilename_split[i])
            if i < (len(myfilename_split)-1):
                myfilename_new += '_'
        myfilename_new += '.stl'
        print("renaming: "+myfilename+" => "+myfilename_new)
        os.rename(myfilename,myfilename_new)

