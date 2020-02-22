

def playcount(inp,track):
    import json
    import requests
    url = "https://t4ils.dev:4433/api/beta/albumPlayCount?albumid={}".format(inp)
    resp = requests.get(url).content
    data = json.loads(resp.decode('utf-8'))
    for i in data['data']:
        if i['uri'] == track:
            return i['playcount']
    return 'Couldnt Find'