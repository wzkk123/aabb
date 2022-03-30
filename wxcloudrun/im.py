import json

import requests
def duixiangcunchu():
  #获取token
  response = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wxfb2997f507abf89e&secret=168726b557fb7221c96955cec59b3347',)
  print()
  data ={
    "env": "prod-0gayxkvve034fe60",
    "path": "ciyunimage/ciyun.jpg"
  }
  #转json
  data = json.dumps(data)
  response = requests.post("https://api.weixin.qq.com/tcb/uploadfile?access_token="+response.json()['access_token'],data)
  print(response.json())
  #response = json.loads(response.json())
  #得到上传链接

  data2={
    "Content-Type":(None,"application/json"),
    "key": (None,"ciyunimage/ciyun.jpg"),
    "Signature": (None,response.json()['authorization']),
    'x-cos-security-token': (None,response.json()['token']),
    'x-cos-meta-fileid': (None,response.json()['cos_file_id']),
    'file': ('ciyun.jpg',open(r"/app/wxcloudrun/ciyun.jpg","rb"),'multipart/form-data')
  }
  #data2 = json.dumps(data2)
  response = requests.post(response.json()['url'], files=data2)
  print(response)

