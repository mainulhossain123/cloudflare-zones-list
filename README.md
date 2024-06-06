# Cloudflare_Zones_List_Extraction
Simple Python script for extracting a list of all Cloudflare zones, generating output to a CSV file

## Prerequisites 
* **Python 3.12 or higher**. Download it from https://www.python.org/downloads/
* **IDE** - I personally used Visual Studio Code but it is upto your preference.
* **Libraries - requests**: Run in Terminal of enviornment or in command prompt **pip install requests**
* **Libraries - datetime**: Run in Terminal of enviornment or in command prompt **pip install datetime**
* **Libraries - csv**: Run in Terminal of enviornment or in command prompt **pip install csv**
* **Cloudflare API Key**. You must have the API key enabled with minimum Read permissions from your Cloudflare account.

## Languages, Frameworks and API calls used in the script
The Script uses the following:

- *[Python 3.12.3](https://www.python.org/downloads/release/python-3123/)* as the primary Programming Language.
- *[Visual Studio Code](https://code.visualstudio.com/download)* as the IDE.
- *[Cloudflare V4 Zone entrypoint HTTP firewall request Check](https://developers.cloudflare.com/api/operations/getZoneEntrypointRuleset)* as the secondary endpoint for WAF Authorization header.
- *[Cloudflare V4 Zone list Check](https://developers.cloudflare.com/api/operations/zones-get)* as the primary endpoint for zone Authorization header.
- *[Requests Module](https://pypi.org/project/requests/)* allows us to make HTTP/1.1 request calls.
- *[Datetime Module](https://docs.python.org/3/library/datetime.html)* for usage of current date and time on file naming schemes
- *[Time Module](https://docs.python.org/3/library/time.html)* primarily used in the script to produce delays in the frequency of each request in case of rate-limiting issues
- *[CSV Module](https://docs.python.org/3/library/csv.html)* allows us to write or read CSV files, in this case write all retrieved data to a CSV file.

## Legal
* This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Cloudflare or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk. Commercial use of this code/repo is strictly prohibited.

## Basic Usage

### API_Key Replacement
Simply replace the value in **api_key** with your own API key and run the script. 

#Set your Cloudflare API key
```
api_key = 'YOUR_API_KEY'
```

### User Input
If you have multiple accounts in your Cloudflare account then you can set up a parameter below in **ZN_zones** to include the parent sub account name under which all the zones you wish to get the list for. enter in **zone['account']['name'] == 'Input your account you wish to download'**
```python
for _ in range(retries):
        response = session.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['success'] and data['result']:
                # Filter zones for only DXP customers
                ZN_zones = [zone for zone in data['result'] if zone['account']['name'] == 'Input your account you wish to download']
                return True, ZN_zones
        else:
            print("Failed to fetch zones:", response.text)
            time.sleep(5)  # Wait for 5 seconds before retrying
    return False, None
```

### Extracted data and CSV File
The data will be saved in a CSV file **customer_hostnames_{current_date}.csv**, which you can change to your desire and also include a path for saving if you wish but by default. For the current code the following information below are being written over to the CSV file as shown below. The print statements are there simply for showing progress of the code.
```python
ef write_hostnames_to_csv(ZN_zones):
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f'customer_hostnames_{current_date}.csv'
    with open(filename, mode='a', newline='') as file:  # Change 'w' to 'a' to append data to the file
        writer = csv.writer(file)
        for zone in ZN_zones:
            writer.writerow([zone['name']])
            print(f"Hostname: {zone['name']}")
```

### Disclaimer
- I have not used multi-threading in this script unlike previous scripts as due to varying number of zones and dataset size, Cloudflare has a tendency to run into ratelimiting issues, particularly with multi-threading for multiple requests, which was causing loss of data.
