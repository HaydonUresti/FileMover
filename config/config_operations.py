import json 

config_path = 'config/config.json'

def update_value(key, new_value):
    with open(config_path, "r+") as json_file:
        json_data = json.load(json_file)
        json_data[key] = new_value
        
        # Move the file pointer to the beginning
        json_file.seek(0)

        # Truncate the file in case the new content is shorter than the original
        json_file.truncate()

        # Write the updated data back to the file
        json.dump(json_data, json_file, indent=2)

def read_data(key):
    with open(config_path, "r") as json_file:
        return json.load(json_file)[key]