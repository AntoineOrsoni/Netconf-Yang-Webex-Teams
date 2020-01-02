import requests

def list_webhooks():
    url = "https://api.ciscospark.com/v1/webhooks"

    headers = {
        'Authorization': "Bearer NGVjNjE1ZmItZDljMy00YTFmLTg2YmMtODM2OTVjZWEwYjc1OGRkOTMxYWMtNjVh_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
        'User-Agent': "PostmanRuntime/7.15.2",
        'Accept': "*/*",
        'Host': "api.ciscospark.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive"
        }

    response = requests.request("GET", url, headers=headers)

    print(response.text)