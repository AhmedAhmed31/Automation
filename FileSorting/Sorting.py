
import os
import shutil



current_dir=os.path.dirname(os.path.realpath(__file__))

for filename  in os.listdir(current_dir):
    if filename.endswith(('png','jpg','jpeg')):
        if not os.path.exists("images"):
            os.mkdir("images")
        shutil.copy(filename,'images')
        os.remove(filename)
        print('Done')


    if filename.endswith(('pdf','doc','docx','ppt','pptx')):
        if not os.path.exists("document"):
            os.mkdir("document")
        shutil.copy(filename,'document')
        os.remove(filename)
        print('Done')


    if filename.endswith(('mp4','avi','TS')):
        if not os.path.exists("videos"):
            os.mkdir("videos")
        shutil.copy(filename,'videos')
        os.remove(filename)
        print('Done')


    if filename.endswith(('rar','zip')):
        if not os.path.exists("archives"):
            os.mkdir("archives")
        shutil.copy(filename,'archives')
        os.remove(filename)
        print('Done')


    if filename.endswith(('.exe','app','.msi')):
        if not os.path.exists("apps"):
            os.mkdir("apps")
        shutil.copy(filename,'apps')
        os.remove(filename)
        print('Done')


    print("Done")
