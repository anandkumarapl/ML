import matplotlib.pyplot as plt
import numpy as num
import json
import requests

import requests
url=("https://gist.githubusercontent.com/anandkumarapl/4c451f68267f2e121da48d08bb6032a9/raw/5e9aa6c0e92f60f10c4ca197a75b96e4f404d014/gistfile1.txt")
responce=requests.get(url)
data=responce.text
data=json.loads(data)

x=data["x"]
y=data["y"]

plt.plot(x,y)
plt.scatter(x,y)
plt.show()