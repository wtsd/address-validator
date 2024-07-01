import pandas as pd
import googlemaps
import os
import config
from datetime import datetime

# Load your API keys and folder path from the configuration file
GOOGLE_MAPS_API_KEY = config.GOOGLE_MAPS_API_KEY
EXCEL_ADDRESS_TITLE = config.EXCEL_ADDRESS_TITLE
FOLDER_PATH = config.FOLDER_PATH

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

# Function to validate address with Google Maps
def validate_with_google(address):
    try:
        geocode_result = gmaps.geocode(address)
        if not geocode_result:
            return False, None
        
        formatted_address = geocode_result[0]['formatted_address']
        address_components = geocode_result[0]['address_components']
        
        # Check if the address components include street number and route
        if any(comp['types'][0] in ['street_number', 'route'] for comp in address_components):
            return True, formatted_address
        else:
            return False, None
    except Exception as e:
        print(f"Error validating with Google Maps: {e}")
        return False, None

# Load addresses from Excel file
def load_addresses_from_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Main function to validate addresses in all Excel files within a folder
def main():
    if not os.path.exists(FOLDER_PATH):
        print(f"Folder '{FOLDER_PATH}' does not exist.")
        return

    files = [f for f in os.listdir(FOLDER_PATH) if f.endswith('.xlsx') and '_validated' not in f]
    if not files:
        print(f"No Excel files found in folder '{FOLDER_PATH}' that need validation.")
        return

    for file_name in files:
        file_path = os.path.join(FOLDER_PATH, file_name)
        df = load_addresses_from_excel(file_path)
        validation_results = []

        for index, row in df.iterrows():
            address = row[EXCEL_ADDRESS_TITLE]
            google_valid, google_address = validate_with_google(address)
            validation_results.append({
                'Google Valid': google_valid,
                'Google Address': google_address
            })

        validation_df = pd.DataFrame(validation_results)
        result_df = pd.concat([df, validation_df], axis=1)
        
        # Create a new filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_file_name = f"{os.path.splitext(file_name)[0]}_validated_{timestamp}.xlsx"
        new_file_path = os.path.join(FOLDER_PATH, new_file_name)
        
        result_df.to_excel(new_file_path, index=False)
        print(f"Validation completed for '{file_name}'. Results saved to '{new_file_path}'.")

if __name__ == "__main__":
    main()
