
import os
import shutil


# Current directory
# current_dir=os.path.dirname(os.path.realpath(__file__))

# Enter your own directory

path=input("Enter your Folder/directory path")
os.path.dirname(path)
if os.path.exists(path):

    # loop over all files in the directory
    for filename  in os.listdir(path):
        #check for img extentions
        if filename.endswith(('png','jpg','jpeg')):
            if not os.path.exists("images"):
                os.mkdir("images")
            shutil.copy(filename,'images')
            os.remove(filename)
            print('image files Done')

        #check for docs  extentions

        if filename.endswith(('pdf','doc','docx','ppt','pptx')):
            if not os.path.exists("document"):
                os.mkdir("document")
            shutil.copy(filename,'document')
            os.remove(filename)
            print('Docs files  Done')

        #check for video files  extentions

        if filename.endswith(('mp4','avi','TS')):
            if not os.path.exists("videos"):
                os.mkdir("videos")
            shutil.copy(filename,'videos')
            os.remove(filename)
            print('Video files Done')

        #check for compress files  extentions

        if filename.endswith(('rar','zip')):
            if not os.path.exists("archives"):
                os.mkdir("archives")
            shutil.copy(filename,'archives')
            os.remove(filename)
            print('Compress files Done')

        #check for application files  extentions

        if filename.endswith(('.exe','app','.msi')):
            if not os.path.exists("apps"):
                os.mkdir("apps")
            shutil.copy(filename,'apps')
            os.remove(filename)
            print('Application files Done')


        print("Done")
