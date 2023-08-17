from flask import Flask, render_template, request
import requests
import json
import time
import replicate

# os.environ["REPLICATE_API_TOKEN"] = "r8_VhVmhA0awA91ptTJNAMPDXBEXndBdBu0hb7zh"
# token = r8_VhVmhA0awA91ptTJNAMPDXBEXndBdBu0hb7zh
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")#!!!key 要严格对应
        body = json.dumps({"version": "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf", \
                           "input": { "prompt": q } })
        headers = {'Authorization': 'Token r8_VhVmhA0awA91ptTJNAMPDXBEXndBdBu0hb7zh',\
                   'Content-Type': 'application/json'}
        
        output = requests.post('https://api.replicate.com/v1/predictions', \
                                   data=body, \
                                   headers=headers)
        time.sleep(10)
        print('this is',output)
        get_url = output.json()['urls']['get']
        print(get_url)
        # 重新包装 post请求 ['output']
        get_result_all = requests.post(get_url, headers=headers).json()
        print(get_result_all)
        get_result =get_result_all['output'] # 返回 一张图片
        print(get_result)
        return(render_template("index.html", result=get_result[0]))
    else:
        return(render_template("index.html", result="waiting"))

if __name__ == "__main__" :
    app.run()
