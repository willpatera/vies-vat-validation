from collections import OrderedDict

# here is an example response

response_dict = OrderedDict([('soap:Envelope', OrderedDict([('@xmlns:soap', 'http://schemas.xmlsoap.org/soap/envelope/'), ('soap:Body', OrderedDict([('checkVatResponse', OrderedDict([('@xmlns', 'urn:ec.europa.eu:taxud:vies:services:checkVat:types'), ('countryCode', 'DE'), ('vatNumber', '293673193'), ('requestDate', '2021-06-14+02:00'), ('valid', 'true'), ('name', '---'), ('address', '---')]))]))]))])

print(response_dict['soap:Envelope']['soap:Body']['checkVatResponse']['valid'])