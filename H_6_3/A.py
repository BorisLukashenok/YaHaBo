import requests as r


respon = r.get("http://127.0.0.1:5000")
print(respon.content)