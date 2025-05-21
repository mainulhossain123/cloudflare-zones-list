# Cloudflare DXP Hostname Exporter

This script fetches all zone names (hostnames) from a Cloudflare account filtered by account name and saves them into a CSV file. It is ideal for auditing or reporting hostnames associated with a Digital Experience Platform (DXP) or similar services.

---

## 📦 Features

- Authenticates via Cloudflare API token.

- Filters zones by Cloudflare account name.

- Outputs zone hostnames to a timestamped CSV file.

- Handles pagination automatically.

- Retries on failure with exponential backoff.

---

## ⚙️ Requirements
- Python 3.7+

- requests library (install via pip install requests)

---

## 🔑 Environment Variables
Set the following environment variables before running the script:

| Variable       | Description                                        | Required |
| -------------- | -------------------------------------------------- | -------- |
| `API_KEY`      | Cloudflare API token with permission to list zones | ✅ Yes    |
| `ACCOUNT_NAME` | Name of the Cloudflare account to filter zones     | ✅ Yes    |

---

## 🚀 Usage

```bash
# Set environment variables
export API_KEY="your_cloudflare_api_token"
export ACCOUNT_NAME="your_account_name"

# Run the script
python cf_dxp_hostnames_export.py
```

## 📄 Output
The script creates a CSV file in the current directory with the following naming convention:

```css
dxp_customer_hostnames_YYYY-MM-DD.csv
```
Each row in the CSV contains a zone (hostname) under the specified Cloudflare account:
| Hostname         |
| ---------------- |
| example.com      |
| sub.example.org  |
| customer.site.io |
---

## 🔁 Pagination & Retry Logic
- Handles pagination using the page and per_page parameters (fetches up to 1000 zones per request).

- If a request fails, the script waits and retries up to a maximum delay of 60 seconds using exponential backoff.

## 🐳 Docker-Friendly
The script does not write outside the current working directory and only depends on environment variables—making it container-ready.

## 📘 Example .env File
You can use a .env file with the following content:
```env
API_KEY=your_cloudflare_api_token
ACCOUNT_NAME=your_account_name
```
Then load the environment and run the script:
```bash
source .env
python cf_dxp_hostnames_export.py
```

## 📬 Notes
- Make sure your API token has permissions to list zones under the specified account.

- Duplicate entries are not removed—consider post-processing if needed.

## 🤝 Contributing
Pull requests are welcome. For major changes:
* Fork the repo
* Create a feature branch
* Test your changes
* ubmit a PR with context

## 📝 License
This project is licensed under the MIT License

## 📬 Contact
For issues, questions, or feature requests, please contact:
Author: Mainul Hossain
Email: hossainmainul83@gmail.com
