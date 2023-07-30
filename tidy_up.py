# Tidies up the given file path, putting all files in a folder (Music, Video, Document, etc.) based on the file extention

import os

# target directory to be tidied
target = "TargetDirectoyPath"
print(target)

# map = directory name: relevant file extensions
dirs = {"Documents": (".txt",".doc",".docx",".pdf",".xls",".xlsx"), 
         "Music": (".mp3",".wav",".flac",".aac",".alac",".ogg"), 
         "Videos": (".mp4",".mov",".mkv"),
         "Archives": (".rar",".zip", ".7z"), 
         "Pictures": (".jpg", ".png"),
         "Executables": (".exe", ".msi", ".py")}

def move_files(target: str, dirs: map, directory: str):
    """move the files to the relevant directory"""
    # for files in target
    for file in os.listdir(target):
    # if fileExtension in X
        current_path = target + file
        if file.endswith(dirs[directory]):       
    # move file to X
            new_path = target + directory + "\\" + file
            os.rename(current_path, new_path)

# create directories unless already present (an exception is thrown if the directories already exist)
# move relevant files to directory once created
for directory in dirs.keys():
    try:
        os.mkdir(target + directory)
    except:
        print("An error occurred, this is likely to be because the directories already exist.")
    move_files(target, dirs, directory)
    

    


        

            

