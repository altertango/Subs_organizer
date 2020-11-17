#here we call for all the python libraries we are using
from os import listdir, rename
from os.path import isfile, join, dirname, abspath
import inspect
from shutil import copyfile, rmtree

#Function to get the names of every file in a given path (mp)
def onlyfiles(mp):
    return [f for f in listdir(mp) if isfile(mp+chr(92)+f)]

#Function to get the names of every folder in a given path (mp)
def onlyfolders(mp):
    return [f for f in listdir(mp) if not isfile(mp+chr(92)+f)]


#Get the path were the script is located
mypath=dirname(abspath(inspect.stack()[0][1]))

#print the path to the console
print(mypath)

#store the names of every file in the base path (the one were the script is at)
files = onlyfiles(mypath)

#store the names of every folder in the base path (the one were the script is at)
folders = onlyfolders(mypath)

#print them
print(files)
print(folders)

#loop through the name of every folder inside the base path
for f in folders:
    #since f is just the name of the folder to use it as a path we need to add the current path at the beguining and a slash character (\) = chr(92) since slash is used also to write spetial characters, we need to name it this way 
    fpath = mypath+chr(92)+f
    #store the name of the movie file. We are assuming here that there will be only one file in the folder, but if ther's more, it will just take the first it finds
    movie = onlyfiles(fpath)[0]
    
    #here we get all the folders inside the folder f
    subfolder_names=onlyfolders(fpath)
    #here we check if there is a folder called subs so we loop through all the folder names inside f
    for j in subfolder_names:
        if j == "subs": #if we find the folder named subs:
            subsfolderpath=fpath+chr(92)+j #store the name as a full path
            subs_files_names = onlyfiles(subsfolderpath) #get the name of every file inside the subs folder
            for k in subs_files_names: #loop through the names of every file inside the subs folder
                if k[-3:] == "srt": #if the last 3 characters of the file name are srt:
                    subsfile=subsfolderpath +chr(92)+k #get the full path of the srt file
                    #here we copy the file from the original srt file path to the path of the movie (fpath) plus the \ char plus we split the movie name before and after the "." so we get the name before the extension plus the srt extention
                    copyfile(subsfile,fpath +chr(92)+movie.split('.')[0]+".en.srt")
                    #here we rename the subs folder to subs_processed
                    rename(subsfolderpath, subsfolderpath+"_processed")
                    #if you comment the previus line and uncomment this one, you just delete the subs folder
                    #rmtree(subsfolderpath, ignore_errors=True)