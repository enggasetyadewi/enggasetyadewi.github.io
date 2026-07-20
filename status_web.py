import urllib.request

websites = [
    "https://google.com",
    "https://github.com",
    "https://youtube.com"
]

for url in websites:
    try:
        response = urllib.request.urlopen(url)
        print(f"{url} -> {response.status}")
    except Exception as e:
        print(f"{url} -> Error")
