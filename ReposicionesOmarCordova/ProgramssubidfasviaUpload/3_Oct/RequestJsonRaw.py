import requests

r = requests.get('https://api.github.com/events')
r.json()
r = requests.get('https://api.github.com/events', stream=True)

r.raw
r.raw.read(10)
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post("https://httpbin.org/post", data=payload)
print(r.text)
payload_tuples = [('key1', 'value1'), ('key1', 'value2')]
r1 = requests.post('https://httpbin.org/post', data=payload_tuples)
payload_dict = {'key1': ['value1', 'value2']}
r2 = requests.post('https://httpbin.org/post', data=payload_dict)
print(r1.text)
{
  ...
  "form": {
    "key1": [
      "value1",
      "value2"
    ]
  },
  ...
}
r1.text == r2.text