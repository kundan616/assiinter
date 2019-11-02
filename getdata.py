def getdata(link):
    
    import urllib.request, json

    with urllib.request.urlopen(link) as url:
        data = json.loads(url.read().decode())
        return data
