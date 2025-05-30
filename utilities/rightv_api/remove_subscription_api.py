import requests

def remove_service_plan_subscription(hh_id, sp_id, api_url=None):

    # Default API endpoint if not provided
    if api_url is None:
        api_url = "http://10.129.43.130:8082/RightvAPIWS/services/CRMAPIWS83"

    # SOAP request headers
    headers = {
        'Content-Type': 'text/xml;charset=UTF-8',
        'SOAPAction': 'removeServicePlanSubscription'
    }

    # SOAP request body
    body = f'''<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <removeServicePlanSubscription xmlns="http://CRMAPIWS/xsd">
      <IServicePlanSubscriptionIdentifier>
        <householdExternalId>{hh_id}</householdExternalId>
        <servicePlanExternalId>{sp_id}</servicePlanExternalId>
      </IServicePlanSubscriptionIdentifier>
    </removeServicePlanSubscription>
  </soap:Body>
</soap:Envelope>'''

    # Make the request
    try:
        resp = requests.post(api_url, headers=headers, data=body)

        # Print the status code and response
        print(f"Status Code: {resp.status_code}")
        print("Response:\n", resp.text)
        # Return success status and response
        return resp.status_code == 200, resp.text

    except Exception as e:
        print(f"An error occurred: {e}")
        return False, str(e)


if __name__ == "__main__":
    household_id = "4146984"
    service_plan_id = "SP_OTT_BASIC_BASIC"

    # Optional: provide a different API URL if needed
    # api_url = "http://different-server:8082/RightvAPIWS/services/CRMAPIWS83"

    success, response = remove_service_plan_subscription(household_id, service_plan_id)

    if success:
        print("Successfully removed service plan subscription")
    else:
        print("Failed to remove service plan subscription")