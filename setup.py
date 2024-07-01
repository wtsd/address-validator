import os
import subprocess

def install_requirements():
    try:
        subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing packages: {e}")
        exit(1)

def get_user_input():
    google_maps_api_key = input("Enter your Google Maps API key: ")
    excel_address_title = input("Enter the Excel Address Title (default 'Address'): ") or "Address"
    folder_path = input("Enter the folder path (default 'xlsx'): ") or "xlsx"
    
    return google_maps_api_key, excel_address_title, folder_path

def generate_config(google_maps_api_key, excel_address_title, folder_path):
    config_content = f"""
GOOGLE_MAPS_API_KEY = '{google_maps_api_key}'
EXCEL_ADDRESS_TITLE = '{excel_address_title}'
FOLDER_PATH = '{folder_path}'
"""

    with open('config.py', 'w') as config_file:
        config_file.write(config_content.strip())

    print("config.py generated successfully.")

def main():
    install_requirements()
    google_maps_api_key, excel_address_title, folder_path = get_user_input()
    generate_config(google_maps_api_key, excel_address_title, folder_path)

if __name__ == "__main__":
    main()
