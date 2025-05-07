import requests
import json
import re
def delete_household(passw, hh_id, mail=None, phone=None, api_url=None):

    # Default API endpoint if not provided
    if api_url is None:
        api_url = "http://10.129.33.145:8082/RightvAPIWS/services/CRMAPIWS83"
    # SOAP request headers
    header1 = {
        'Content-Type': 'text/xml;charset=UTF-8',
        'SOAPAction': 'inactivateHousehold'
    }

    header2 = {
        'Content-Type': 'text/xml;charset=UTF-8',
        'SOAPAction': 'removeHouseholdPersonalDetails'
    }
    body_login = {
        'client': "",
        'password': "",
        'phone_number': ""
    }
    # SOAP request body
    if mail is None:
        body_login.update({"phone_number": {phone}, "password": {passw}, 'client': "json"})
    elif phone is None:
        body_login.update({"email": {mail}, "password": {passw}, 'client': "json"})
    body1 = f'''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://CRMAPIWS/xsd" xmlns:xsd1="http://entities.crm.v83.interfaces.rightv.orca.com/xsd" xmlns:xsd2="http://entities.common.v83.interfaces.rightv.orca.com/xsd">
            <soapenv:Header/>
            <soapenv:Body>
            <xsd:inactivateHousehold>
            <xsd:householdIdentifier>
            <xsd1:externalId>{hh_id}</xsd1:externalId>
            </xsd:householdIdentifier>
            </xsd:inactivateHousehold>
            </soapenv:Body>
            </soapenv:Envelope>'''
    body2 = f'''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://CRMAPIWS/xsd" xmlns:xsd1="http://entities.crm.v83.interfaces.rightv.orca.com/xsd" xmlns:xsd2="http://entities.common.v83.interfaces.rightv.orca.com/xsd">
            <soapenv:Header/>
            <soapenv:Body>
            <xsd:removeHouseholdPersonalDetails>
            <xsd:householdIdentifier>
            <xsd1:externalId>{hh_id}</xsd1:externalId>
            </xsd:householdIdentifier>
            </xsd:removeHouseholdPersonalDetails>
            </soapenv:Body>
            </soapenv:Envelope>'''
    # nyamka ugsun
    # body2 = f'''/RightvAPIWS/services/CRMAPIWS83/","request":"
    #         <SOAP-ENV:Envelope
    #             xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\">
    #         <SOAP-ENV:Header/>
    #         <SOAP-ENV:Body>
    #         <ns2:removeHouseholdPersonalDetails
    #                     xmlns:ns2=\"http://CRMAPIWS/xsd\"
    #                     xmlns:ns3=\"http://entities.common.v83.interfaces.rightv.orca.com/xsd\"
    #                     xmlns:ns4=\"http://entities.crm.v83.interfaces.rightv.orca.com/xsd\"
    #                     xmlns:ns5=\"http://entities.vod.v83.interfaces.rightv.orca.com/xsd\"
    #                     xmlns:ns6=\"http://entities.live.v83.interfaces.rightv.orca.com/xsd\"
    #                     xmlns:ns7=\"http://entities.core.v83.interfaces.rightv.orca.com/xsd\">
    #         <ns2:householdIdentifier>
    #         <ns4:externalId>{hh_id}</ns4:externalId>
    #         </ns2:householdIdentifier>
    #         </ns2:removeHouseholdPersonalDetails>
    #         </SOAP-ENV:Body>
    #         </SOAP-ENV:Envelope>'''

    # Make the request
    try:
        response_login = requests.post("https://looktv.mn/Login", data=body_login)
        print(response_login.text)
        response_data = response_login.json()   # response as json
        message = response_data['response']['message']   # finding cookie
        match = re.search(r'=(.+)', message)
        if match:
            cookie_string = match.group(1)
            print(cookie_string)
        else: print("nothing correct was found identity=.....")
        print(body_login)

        response2 = requests.post(api_url, headers=header2, data=body2)
        response1 = requests.post(api_url, headers=header1, data=body1)
        response_del = requests.delete("https://looktv.mn/onlineusers?client=xml",
                                       cookies=response_login.cookies)






        # Print the status code and response
        print(f"Status Code: {response_del.status_code}, {response1.status_code},  {response2.status_code}")
        print(f"Response:\n {response_del.text} \n {response1.text} \n {response2.text}")
        return (response_del.status_code == 200)

        # print(response2.status_code)
        # return ("ok", "ok")
    except Exception as e:
        print(f"An error occurred: {e}")
        return (False, str(e))


if __name__ == "__main__":
    household_id = "7169236"

    phone_number = "89988218"
    # email = "ganchimegulti@gmail.com"
    password = "Ganchimeg.g1"

    # Optional: provide a different API URL if needed
    # api_url = "http://different-server:8082/RightvAPIWS/services/CRMAPIWS83"

    success = delete_household(passw=password, hh_id=household_id, phone=phone_number)

    if success:
        print("Successfully deleted household")
    else:
        print("Failed to delete household")