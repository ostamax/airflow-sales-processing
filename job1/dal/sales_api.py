import os
import re
import requests
from typing import List, Dict, Any

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
#AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")
AUTH_TOKEN = "2b8d97ce57d401abd89f45b0079d8790edd940e6"

def get_sales(date: str) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    Args:
        date (str): data retrieve the data from

    Returns:
        List[Dict[str, Any]]: list of records
    """    
    fulllist = []
    status_code = 501
    if bool(re.match(r"[0-9+]+-[0-9+]+-[0-9]", date)):

        i = 1
        response = requests.get(
            url=API_URL + "sales?date=" + date + "&page=" + str(i),
            headers={'Authorization':AUTH_TOKEN},
            timeout=5
        )

        status_code = response.status_code

        while response.status_code == 200:
            print(str(i))
            fulllist = fulllist + response.json()
            i+=1
            response = requests.get(
                url=API_URL + "sales?date=" + date + "&page=" + str(i),
                headers={'Authorization':AUTH_TOKEN},
                timeout=5
            )

    if fulllist:
        return {
                "data": fulllist,
                }, status_code
    else:
        return {
                "data": '',
                }, status_code
