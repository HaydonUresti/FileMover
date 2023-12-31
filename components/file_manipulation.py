import os
import shutil
import ast

def retrieve_file(term, exclude, folder):
    """
    A function that retrieves files from the downloads folder if they contain a certain term in their title.

    Parameters:
                term: The term that is to be looked for in each file's title.

    Returns:
                files: A list of files that each contain the term in the title.
    """

    # Defining the folder to be searched.

    all_files = os.listdir(folder)
    
    # Retrieving the files that contain the word resume 
    files = [f for f in all_files if os.path.isfile(os.path.join(folder, f)) 
            and f.lower().find(term) != -1]
    
    files = []

    # If both fields are empty do:      
    if term == "" and exclude == "":
        return all_files
    
    
    # If only exclude is empty do: 
    if exclude == "":
        for file in all_files:
            if os.path.isfile(os.path.join(folder, file)) and file.lower().find(term) != -1:
                files.append(file)

    # If only term is empty do:
    if term == "":
        for file in all_files:
            if os.path.isfile(os.path.join(folder, file)) and file.lower().find(exclude) == -1:
                files.append(file)
    
     # If neither field is empty do:
    for file in all_files:
            if os.path.isfile(os.path.join(folder, file)) and file.lower().find(term) != -1 and file.lower().find(exclude) == -1:
                files.append(file)   
    
    if not files:
        return f"No files contain the term {term}"
    return files





def move_files(path, files, folder):
    """
   A function that moves given files to a given directory.
   Parameters
            path: The new path the file will be moved to.
            files: The list of files that will be moved.
            folder: The path/folder that the files are coming from.
   Returns
            None
    """
    try:
        files = ast.literal_eval(files)
    except (SyntaxError, ValueError) as e:
        print(f"List literal Error: {e}")

    try:
        for file in files:
            shutil.move(f'{folder}/{file}', f'{path}/{file}')
    except:
        print("Error in componenets.file_manipulation.move_files")
   