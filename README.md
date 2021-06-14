# VIES EU VAT Validation

Quick test to demonstrate to validate EU VAT IDs using VIES SOAP API + Python.

Reference: [VIES WSDL](https://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl)

## Request

Below is a sample POST request. Replace variables for `$country_code` and `$vat_number` for the VAT ID you are trying to validate.

```xml
<?xml version="1.0" encoding="ISO-8859-15" standalone="no"?>
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
</soap:Envelope>
```

## Example Response

VIES will return if a VAT ID validity (true or false). Sometimes you will also get company name and address otherwise response will contain '---'.  

```xml
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <checkVatResponse xmlns="urn:ec.europa.eu:taxud:vies:services:checkVat:types">
            <countryCode>DE</countryCode>
            <vatNumber>123456789</vatNumber>
            <requestDate>2021-06-14+02:00</requestDate>
            <valid>true</valid>
            <name>---</name>
            <address>---</address>
        </checkVatResponse>
    </soap:Body>
</soap:Envelope>

```