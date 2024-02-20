import requests

domain = input("Enter a domain or subdomain name here:\n")
api_url = 'https://api.api-ninjas.com/v1/dnslookup?domain={}'.format(domain)
response = requests.get(api_url, headers={'X-Api-Key': 'API_Key'}) #Get an API key from here: https://api-ninjas.com/api/dnslookup
ipv4_addresses = []
if response.status_code == requests.codes.ok:
    json_data = response.json()
    for record in json_data:
        if record['record_type'] == 'A':
            ipv4_addresses.append(record['value'])
    print(ipv4_addresses)
    print(json_data)
else:
    print("Error:", response.status_code, response.text)
