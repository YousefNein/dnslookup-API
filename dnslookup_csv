import requests
import csv

def dnslookup(domain):
    api_url = 'https://api.api-ninjas.com/v1/dnslookup?domain={}'.format(domain)
    response = requests.get(api_url, headers={'X-Api-Key': 'API-Key'}) #Get an API key from here: https://api-ninjas.com/api/dnslookup
    ipv4_addresses = []
    if response.status_code == requests.codes.ok:
        json_data = response.json()
        for record in json_data:
            if record['record_type'] == 'A':
                ipv4_addresses.append(record['value'])
                print(f"Added {domain} IP(s)")
                print(143*'-')
        return ipv4_addresses
    else:
        print("Error:", response.status_code, response.text)

with open('your_file.csv', newline='') as csvfile: #Put your CSV file name that is in the same path here.
    reader = csv.DictReader(csvfile)
    
    with open('results.csv', 'w', newline='') as resultfile:
        fieldnames = ['Domain', 'IP Addresses']
        writer = csv.DictWriter(resultfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            domain = row['domain']
            ip_addresses = dnslookup(domain)
            if ip_addresses:
                writer.writerow({'Domain': domain, 'IP Addresses': ', '.join(ip_addresses)})
            else:
                writer.writerow({'Domain': domain, 'IP Addresses': 'N/A'})
