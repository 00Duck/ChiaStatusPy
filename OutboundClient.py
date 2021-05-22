import http.client
import json
from configparser import ConfigParser
import base64

"""
OutboundClient
    Sends a request to an endpoint that assumes basic authentication and HTTPS. Please
    note that https:// should not be used in the config.ini host value as it is already
    assumed in the code.

    Gives the response status after the collected object is sent. Does not contain any data
    from the response.
"""
class OutboundClient:
    def __init__(self) -> None:
        config = ConfigParser()
        config.read('config.ini')

        self.host = config.get("outboundclient", "host")
        if self.host == "":
            print("Cannot sent status JSON: missing host. Please update the config.ini")
            exit()

        self.endpoint = config.get("outboundclient", "endpoint")
        if self.endpoint == "":
            print("Cannot sent status JSON: missing user endpoint. Please update the config.ini")
            exit()

        user = config.get("outboundclient", "user")
        pw = config.get("outboundclient", "password")
        if user == "" or pw == "":
            print("Cannot sent status JSON: missing user name or password. Please update the config.ini")
            exit()
        
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Basic " + str(base64.urlsafe_b64encode((user + ":" + pw).encode("utf-8")), "utf-8")
        }        

    def send(self, method: str, body: dict = {}) -> dict:
        conn = http.client.HTTPSConnection(host=self.host, port=443)
        conn.request(method, url=self.endpoint, headers=self.headers, body=json.dumps(body))

        resp = conn.getresponse()

        if resp.status != 200 and resp.status != 201:
            return {"error": str(resp.status) + " " + resp.reason}

        return {"success": resp.status}