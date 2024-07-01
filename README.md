# address-validator

## INSTALLATION
1. Install the required modules:

```
pip install -r requirements.txt
```

2. Create a Google Cloud Platform project and get an API key for Maps: https://console.cloud.google.com/apis/credentials

3. Create a `config.py` file with your API key, title caption from the excel file, and excel file/path.

## USAGE
Run in console:

```
$ python validate-address.py
```

The result will be saved to a file next to your original file with a postfix "_validated_{timestamp}". In a new file, there are supposed to be two additional columns: "Google Valid" and "Google Address". The first indicates if the address exists and is correct, the second will show a valid full address.
