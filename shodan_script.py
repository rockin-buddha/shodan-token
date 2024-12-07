import os
from shodankey import token

token_file = "tokens.txt"

if os.path.exists(token_file):
    with open(token_file, "r") as file:
        api_keys = file.readlines()

    for api_key in api_keys:
        api_key = api_key.strip()
        print(f"Checking API Key: {api_key}")
        result = token(api_key)
        
        if result["valid"]:
            print(f"Plan: {result['plan']}")
            print(f"Scan Credits: {result['scan_credits']}")
            print(f"Query Credits: {result['query_credits']}")
            print(f"Monitored IPs: {result['monitored_ips']}")
            print(f"Unlocked Left: {result['unlocked_left']}")
            print(f"Telnet Access: {result['telnet']}")
            print(f"HTTPS Supported: {result['https']}")
            print(f"Usage Limits: {result['usage_limits']}")
            print(f"Timestamp: {result['timestamp']}")
        else:
            print(f"Invalid API Key: {api_key}, Error: {result['error']}")
        
        print("-" * 40)
else:
    print(f"{token_file} does not exist. Please create the file and add your Shodan API keys.")
