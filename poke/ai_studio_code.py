import os
import json

def generate_gamedata(image_folder):
    pokemon_list = []
    
    # Check if directory exists
    if not os.path.exists(image_folder):
        print(f"Error: Folder '{image_folder}' not found.")
        return

    # Loop through every file in the folder
    for filename in os.listdir(image_folder):
        # Process only .png files
        if filename.lower().endswith(".png"):
            try:
                # Remove the file extension (.png)
                name_without_ext = os.path.splitext(filename)[0]
                
                # Split the name and the hex code by the underscore
                # Maxsplit=1 in case the Pokemon name contains an underscore
                parts = name_without_ext.rsplit('_', 1)
                
                if len(parts) == 2:
                    name = parts[0]
                    hex_code = parts[1]
                    
                    # Create the dictionary object
                    pokemon_list.append({
                        "name": name,
                        "color": hex_code,
                        "filename": filename
                    })
                else:
                    print(f"Skipping {filename}: Incorrect format (needs Name_HEX.png)")
            
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    # Create the Javascript content
    # json.dumps converts the list to a valid JSON string
    js_content = f"window.pokemonList = {json.dumps(pokemon_list, indent=4)};"

    # Write the gamedata.js file
    with open("gamedata.js", "w", encoding="utf-8") as f:
        f.write(js_content)

    print(f"Successfully generated gamedata.js with {len(pokemon_list)} entries.")

if __name__ == "__main__":
    # Change 'images' to the name of your folder
    FOLDER_NAME = "images" 
    generate_gamedata(FOLDER_NAME)