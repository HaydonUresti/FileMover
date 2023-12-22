import os

def retrieve_file():
    # Defining the folder to be searched.
    folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    all_files = os.listdir(folder)
    
    # Retrieving only the first 10 files.
    files = [f for f in all_files if os.path.isfile(os.path.join(folder, f))][:10]

    return files