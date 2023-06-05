import requests
from config import url


#params = {"q": "demotivators"}
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Dnt": "1",
    "Host": "httpbin.org",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-647dc9de-0b3b26ee5c8a8ded2ac62f48"
  }

cust_data = {
    "custname": "Alex",
    "custtel": "89835306089",
    "custemail": "pilotmaestro@gmail.com",
    "size": "medium",
    "topping": "bacon",
    "delivery": "None",
    "comments": "None"
}


#response = requests.get(url, headers=headers)

#response = requests.post(url, headers=headers, data=cust_data)

sess_var = requests.Session()

sess_var.get('https://httpbin.org/form/post')
response = sess_var.post(url, headers=headers, data=cust_data)

print(f'status_code: {response.status_code}')
#print(f'headers: {response.headers}')
#print(f'content: {response.content}')
print(f'text: {response.text}')
