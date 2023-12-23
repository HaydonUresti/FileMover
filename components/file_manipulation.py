import os

def retrieve_file(term, exclude):
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
    
    files = []

    # for file in all_files:
    #     if os.path.isfile(os.path.join(folder, file)):
    #         if term == "":
    #             if exclude == "":

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

