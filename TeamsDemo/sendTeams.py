import urllib3
import json


class TeamsWebhookException(Exception):
    """custom exception for failed webhook call"""
    pass


class ConnectorCard:
    def __init__(self, hookurl, http_timeout=60):
        self.http = urllib3.PoolManager()
        self.payload = {}
        self.hookurl = hookurl
        self.http_timeout = http_timeout

    def text(self, mtext):
        self.payload["text"] = mtext
        return self

    def send(self):
        headers = {"Content-Type":"application/json"}
        r = self.http.request(
                'POST',
                f'{self.hookurl}',
                body=json.dumps(self.payload).encode('utf-8'),
                headers=headers, timeout=self.http_timeout)
        if r.status == 200: 
            return True
        else:
            raise TeamsWebhookException(r.reason)


if __name__ == "__main__":
    myTeamsMessage = ConnectorCard(https://lenovobeijing.webhook.office.com/webhookb2/58df5cea-0eb6-4e5b-a01e-cacfc6d19e6e@5c7d0b28-bdf8-410c-aa93-4df372b16203/IncomingWebhook/5fdb9c2b330740f1beb6459d1287d210/df8158c5-308c-45c3-be28-af7ea258765b)
    myTeamsMessage.text("this is my test message to the teams channel.")
    myTeamsMessage.send()