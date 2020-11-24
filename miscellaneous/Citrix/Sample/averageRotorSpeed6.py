# quite a badly worded question tbf but oh well I did my best?

"""
6. Get IOT devices by Parent Id
In this challenge, the REST API contains information about a collection of IoT devices. Given the status query and the identifier of the parent device, get the average rotor speed of available IoT devices with the given status parent identifier.



To access the collection of devices, perform an HTTP GET request to:

https://jsonmock.hackerrank.com/api/iot_devices/search?status=<statusQuery>&page=<pageNumber>

where <statusQuery> is a given string to query and <pageNumber> is the page number of the results to return.



For example, GET request to:

https://jsonmock.hackerrank.com/api/iot_devices/search?status=STOP&page=2

will return the second page of the devices with their status containing "STOP".



The response to such request is a JSON with the following 5 fields:



page: The current page of the results
per_page: The maximum number of devices returned per page.
total: The total number of devices available on all pages of the result.
total_pages: The total number of pages with results.
data: An array of objects containing devices returned on the requested page


Each device object has the following schema:

id: The unique ID of the device
timestamp: The timestamp when the device was added to the collection, in UTC milliseconds
status: The status of the device
operatingParams: the object containing operating parameters of the device
asset: The object containing information about the asset of the device
parent: Optional. The object containing information about the parent of the device


The operating parameters object has the following schema:

rotorSpeed: The rotor speed of the device
slack: The slack in the device
rootThreshold: The root threshold for the device


The asset object has the following schema:

id: The unique ID of the asset
alias: The alias for the asset
The parent object, if it is present, will have one or both of the following fields:

id: The unique ID of the parent of the asset
alias: The alias for the parent of the asset


Given string statusQuery, and numerical parentId value, the goal is to return the floor of the average rotor speed of all returned devices that have their parent identifier matching the parentId value. If there are no devices matching the given criteria, the result must be 0.





Function Description

Complete the function avgRotorSpeed in the editor below.



avgRotorSpeed has the following parameter(s):

    statusQuery: string to query for

    parentId: id of the parent to match



Returns:

    int: the floor of the average rotor speed of matching devices or 0 if there are none



Input Format For Custom Testing
Sample Case 0
Sample Input For Custom Testing

RUNNING
7
Sample Output

3880
Explanation

The status query is "RUNNING" and the parent identifier is 7, so we are interested in the average rotor speed of all returned devices having a parent identifier of 7. There are 4 such devices and their rotor speeds are 4721, 4446, 1592 and 4761 respectively. Their average rotor speed is (4721 + 4446 + 1592 + 4761)/4 = 15520/4 = 3880. Therefore, the final answer is 3880 rounded down to integer value which is 3880.

# URL for cut and paste
# https://jsonmock.hackerrank.com/api/iot_devices/search?status={statusQuery}&page={number}
#
# The function is expected to return an INTEGER.

"""

import os
import random
import re
import sys
import math
import requests
import json


def avgRotorSpeed(statusQuery, parentId):
    output = 0
    searching = {"status": statusQuery}
    getting = requests.get("https://jsonmock.hackerrank.com/api/iot_devices/search", params=searching)
    summary = json.loads(getting.text)  # {'page': 1, 'per_page': 10, 'total': 35, 'total_pages': 4, 'data': [...]}
    # print(json.dumps(summary, indent=2))
    page = 1
    devices_count = 0
    total_rotor_speeds = 0
    while page <= summary["total_pages"]:# and devices_count <:
        searching = {"status": statusQuery, "page": page}
        content = json.loads(requests.get("https://jsonmock.hackerrank.com/api/iot_devices/search", params=searching).text)
        data = content["data"]
        for device in data:
            try:
                if device["asset"]["parent"]["id"] == parentId: ###??? dapi
                    devices_count += 1
                    total_rotor_speeds += device["operatingParams"]["rotorSpeed"]
            except:
                pass
    output = math.floor(float(total_rotor_speeds/devices_count))
    return output

avgRotorSpeed("RUNNING", 7)
