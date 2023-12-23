import os

def retrieve_file(term):
    """
    A function that retrieves files from the downloads folder if they contain a certain term in their title.

    Parameters:
                term: The term that is to be looked for in each file's title.

    Returns:
                files: A list of files that each contain the term in the title.
    """


    # Defining the folder to be searched.
    folder = os.path.join(os.path.expanduser('~'), 'Downloads')

    all_files = os.listdir(folder)
    
    # Retrieving the files that contain the word resume 
    files = [f for f in all_files if os.path.isfile(os.path.join(folder, f)) 
            and f.lower().find(term) != -1]
    
    if not files:
        return f"No files contain the term {term}"
    return files

