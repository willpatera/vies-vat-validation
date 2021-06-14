import requests
from string import Template
import xmltodict

VIES_URL = "https://ec.europa.eu/taxation_customs/vies/services/checkVatService"
xml_template = Template('''<?xml version="1.0" encoding="ISO-8859-15" standalone="no"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
  xmlns:tns1="urn:ec.europa.eu:taxud:vies:services:checkVat:types"
  xmlns:impl="urn:ec.europa.eu:taxud:vies:services:checkVat">
  <soap:Header>
  </soap:Header>
  <soap:Body>
    <tns1:checkVat xmlns:tns1="urn:ec.europa.eu:taxud:vies:services:checkVat:types"
     xmlns="urn:ec.europa.eu:taxud:vies:services:checkVat:types">
     <tns1:countryCode>$country_code</tns1:countryCode>
     <tns1:vatNumber>$vat_number</tns1:vatNumber>
    </tns1:checkVat>
  </soap:Body>
</soap:Envelope>''')


# replace these with the country + VAT ID you are trying to validate/check
COUNTRY_CODE = "DE"
VAT_NUMBER = "293673193"

request_data = xml_template.substitute(country_code=COUNTRY_CODE, vat_number=VAT_NUMBER)
print("request data: {}".format(request_data))

response = requests.post(VIES_URL,
              headers={'content-type': 'text/xml'},
              data=request_data)

# parse the xml content to python OrderedDict see example_response.py for reference
response_dict = xmltodict.parse(response.content)
print(response_dict)
# if we are only interested in the validity, this will be true | false
# response_dict['soap:Envelope']['soap:Body']['checkVatResponse']['valid']

print("response code: {}\nresponse_content: {}".format(response.status_code,
  response_dict['soap:Envelope']['soap:Body']['checkVatResponse']))