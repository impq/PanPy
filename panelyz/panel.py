import requests, typing

class Panel:

    def __init__(self):
        self.api_key = "YOUR OWN API KEY"
        self.base_url = "https://panelyz.com/api/v2"

    def getBalance(self):
        try:

            p = {
                "key": self.api_key,
                "action": "balance"
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)


    def addOrder(self, service: int, quantity: int, link: str):
        try:
            p = {
                "key": self.api_key,
                "action": "add",
                "service": service,
                "link": link,
                "quantity": quantity
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)

    def getOrderStat(self, order: int):
        try:
            p = {
                "key": self.api_key,
                "action": "status",
                "order": order
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)


    def getMultOrderStat(self, orders: typing.Union[list, int]):
        try:
            p = {
                "key": self.api_key,
                "action": "status",
            }

            if type(orders) == int:
                p["order"] = orders
            else:
                p["orders"] = orders

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)


    def getServices(self):
        try:
            p = {
                "key": self.api_key,
                "action": "services"
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)


    def createRefill(self, order: int):
        try:
            p = {
                "key": self.api_key,
                "action": "refill",
                "order": order
            }

            re = requests.post(self.base_url, params=p)

            if re.status_code == 200:
                print(re.text)

        except Exception as e:
            print(e)


    def getRefillStat(self, refill_id: int):
            try:
                p = {
                    "key": self.api_key,
                    "action": "refill_status",
                    "refill": refill_id
                }

                re = requests.post(self.base_url, params=p)

                if re.status_code == 200:
                    print(re.text)

            except Exception as e:
                print(e)
