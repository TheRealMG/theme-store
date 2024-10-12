import os
import json

def update_theme_files(themes_json_path):
    """Update each theme.json file based on themes.json data."""
    # Load themes.json
    with open(themes_json_path, 'r') as f:
        themes_data = json.load(f)

    # Iterate through each theme in themes.json
    for theme in themes_data:
        theme_id = theme['id']
        theme_json_path = os.path.join('themes', theme_id, 'theme.json')

        # Check if theme.json file exists
        if os.path.exists(theme_json_path):
            # Update the theme.json file
            with open(theme_json_path, 'r') as f:
                theme_file_data = json.load(f)

            # Update fields
            theme_file_data['createdAt'] = theme.get('createdAt', theme_file_data.get('createdAt'))
            theme_file_data['updatedAt'] = theme.get('updatedAt', theme_file_data.get('updatedAt'))
            theme_file_data['tags'] = theme.get('tags', theme_file_data.get('tags', []))

            # Write the updated theme data back to theme.json
            with open(theme_json_path, 'w') as f:
                json.dump(theme_file_data, f, indent=2)
        else:
            print(f"Theme JSON file not found for theme ID: {theme_id}")

if __name__ == "__main__":
    update_theme_files('themes.json')
