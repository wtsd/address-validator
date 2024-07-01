# address-validator

## INSTALLATION

### Option 1
1. Clone repository
2. Install the required modules:

```
pip install -r requirements.txt
```

3. Create a Google Cloud Platform project and get an API key for Maps: https://console.cloud.google.com/apis/credentials (Pricing: https://mapsplatform.google.com/pricing/)

4. Create `config.py` file:
```
cp config-example.py config.py
```

4. Edit `config.py` with your API key, title caption (name of your column in Excel — exact match), and excel file(s) directory.

OR

### Option 2

1. Clone repository

2. Run the setup script:
```
python setup.py
```

## USAGE

Clone repository.
Create `config.py` file and edit your key
Copy your Excel files to `xlsx` directory.
Run in console:

```
python validate-address.py
```

The result will be saved to a file next to your original file with a postfix "_validated_{timestamp}". In a new file, there are supposed to be two additional columns: "Google Valid" and "Google Address". The first indicates if the address exists and is correct, the second will show a valid full address.
