
def counter(inp):
    import json
    import requests
    url = "https://t4ils.dev:4433/api/beta/albumPlayCount?albumid={}".format(inp)
    resp = requests.get(url).content
    data = json.loads(resp.decode('utf-8'))
    cnt = 0
    for i in data['data']:
        cnt += i['playcount']
    return cnt