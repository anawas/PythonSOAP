"""
https://docs.python-zeep.org/en/master/client.html#configuring-the-client
"""

import zeep

if __name__ == '__main__':
    wsdl = 'http://localhost:7789/?wsdl'
    client = zeep.Client(wsdl=wsdl)
    response = client.service.say_hello("Andreas", 10)
    for res in response:
        print(res)
