import base64
import requests

url_host = "http://plantgw.nongbangzhu.cn"


app_code = '38ef43ff3c704a7c8bc5f934185b3a3d' #这里替换为你购买的AppCode


# 植物花卉识别接口_v2的请求示例
def recognize2():
    url_path = '/plant/recognize2'

    with open("./pics/杜鹃.jpeg", "rb") as image_file:
        img_base64 = base64.b64encode(image_file.read()).decode('ascii')
        body = {'img_base64': img_base64}

        headers = {'content-type': "application/x-www-form-urlencoded", 'authorization': "APPCODE " + '38ef43ff3c704a7c8bc5f934185b3a3d'}
        response = requests.request("POST", url_host+url_path, data=body, headers=headers) # 默认utf-8
        print(response.text)

    return
recognize2()
