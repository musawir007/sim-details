import re
import json

# Your JSON string (truncated for brevity)
import requests
n = '03099127047'
response = requests.get(
    f'https://simownerdetails.net.pk/wp-admin/admin-ajax.php?action=get_number_data&get_number_data=searchdata={n}'
)
json_data = json.loads(response.text)

html_data = json_data['data'].replace('\\/', '/') 
records = re.findall(
    r'<label class="info">FULL NAME<\/label>\s*<div>(.*?)<\/div>.*?'
    r'<label class="info">PHONE #<\/label>\s*<div>(\d+)<\/div>.*?'
    r'<label class="info">CNIC #<\/label>\s*<div>(\d+[*]*\d)<\/div>.*?'
    r'<label class="info">ADDRESS<\/label>\s*<div>(.*?)<\/div>',
    html_data,
    re.DOTALL
)

# Step 5: Print the results
if not records:
    print("No records found.")
else:
    for i, record in enumerate(records, 1):
        full_name, phone, cnic, address = record
        print(f"--- Record {i} ---")
        print(f"Full Name: {full_name.strip()}")
        print(f"Phone #: {phone.strip()}")
        print(f"CNIC #: {cnic.strip()}")
        print(f"Address: {address.strip()}\n")
