import pandas as pd
import googlemaps
import os
import config
from datetime import datetime

# Load your API keys from configuration file
GOOGLE_MAPS_API_KEY = config.GOOGLE_MAPS_API_KEY
EXCEL_ADDRESS_TITLE = config.EXCEL_ADDRESS_TITLE

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

# Main function to validate addresses
def main(file_path):
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
    
    # Create a new filename with postfix and timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_file_path = f"{os.path.splitext(file_path)[0]}_validated_{timestamp}.xlsx"
    
    result_df.to_excel(new_file_path, index=False)
    print(f"Validation completed. Results saved to '{new_file_path}'.")

if __name__ == "__main__":
    file_path = config.EXCEL_FILE  # Replace with your Excel file path
    main(file_path)
