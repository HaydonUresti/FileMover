import os

def retrieve_file():
    # Defining the folder to be searched.
    folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    all_files = os.listdir(folder)
    
    # Retrieving the files that contain the word resume 
    files = [f for f in all_files if os.path.isfile(os.path.join(folder, f)) 
            and f.lower().find('resume') != -1]
    # files = []

    # for i in all_files:
    #     if os.path.isfile(os.path.join(folder, i)):
    #         if i.lower().find('poop'):
    #             files.append(i)
    

    return files

# print(retrieve_file())