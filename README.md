# DNS Lookup Script

This repository contains two Python scripts to perform DNS lookups for domain names and extract their IPv4 addresses. The scripts utilize the API provided by api-ninjas.com to retrieve DNS records.

### Files:

1. **dnslookup_csv.py**: This script reads domain names from a CSV file, performs DNS lookups for each domain, extracts their IPv4 addresses, and saves the results to a CSV file named 'results.csv'.

2. **dnslookup_terminal.py**: This script allows users to input a domain or subdomain name in the terminal, performs a DNS lookup for the entered domain, extracts its IPv4 addresses, and displays the results in the terminal.

### Usage:

**dnslookup_csv.py**:
1. Ensure you have a CSV file containing a list of domain names in the same directory as the script.
2. Replace `'your_file.csv'` in the script with the name of your CSV file.
3. Run the script. It will read domain names from the CSV file, perform DNS lookups, and save the results to 'results.csv'.

**dnslookup_terminal.py**:
1. Run the script.
2. Enter a domain or subdomain name when prompted.
3. The script will perform a DNS lookup for the entered domain, extract its IPv4 addresses, and display them in the terminal.

### Note:
- You can obtain an API key for the api-ninjas.com DNS lookup service from [here](https://api-ninjas.com/api/dnslookup).
- The scripts currently extract only IPv4 addresses. To include IPv6 addresses, add a second if condition in the `dnslookup()` function with `'record_type': 'AAAA'`.

### Additional Information:
- Both scripts use the `requests` library to interact with the API and handle HTTP requests.
- The CSV files are read and written using Python's built-in `csv` module.
- The scripts provide a convenient way to perform DNS lookups and extract IPv4 addresses for domains and subdomains.
