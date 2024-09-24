import requests
import csv
from datetime import datetime
import time
import os

# Create a session to reuse HTTP connections
session = requests.Session()

def get_zones(api_key, account_name, page, per_page):
    url = "https://api.cloudflare.com/client/v4/zones"
    headers = {
        "Authorization": f"Bearer {api_key}",
    }
    params = {
        "page": page,
        "per_page": per_page
    }
    retries = 3
    for _ in range(retries):
        response = session.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if data['success'] and data['result']:
                # Filter zones based on the account name provided by the user
                dxp_zones = [zone for zone in data['result'] if zone['account']['name'] == account_name]
                return True, dxp_zones
        else:
            print("Failed to fetch zones:", response.text)
            time.sleep(5)  # Wait for 5 seconds before retrying
    return False, None

def write_hostnames_to_csv(dxp_zones):
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f'dxp_customer_hostnames_{current_date}.csv'
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        for zone in dxp_zones:
            writer.writerow([zone['name']])
            print(f"Hostname: {zone['name']}")

# Example usage
api_key = os.getenv('API_KEY')
account_name = os.getenv('ACCOUNT_NAME')  # Get account name from environment variable

page = 1
per_page = 1000
retry_delay = 1  # Initial delay time
all_dxp_zones = []

while True:
    success, zones = get_zones(api_key, account_name, page, per_page)
    if success:
        if zones:
            all_dxp_zones.extend(zones)
            write_hostnames_to_csv(zones)  # Write to CSV immediately after fetching
            page += 1
            retry_delay = 1  # Reset the retry delay on successful fetch
            # Introduce a delay between requests to avoid rate limit issues
            time.sleep(1)
        else:
            print("No more zones to process.")
            break
    else:
        retry_delay *= 2  # Double the delay time on failure
        print(f"Retrying in {retry_delay} seconds due to errors.")
        time.sleep(retry_delay)
        if retry_delay > 60:  # Maximum delay threshold
            print("Maximum retry delay reached. Exiting.")
            break
