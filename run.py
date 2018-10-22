import os #引入linux系統指令
from flask import Flask, Response #引入flask及response
from flask import request #引入get post


app = Flask(__name__)

@app.route("/")
def index():
    #os.system("echo 'This is a test' > /opt/a/foo.txt --user") #執行linux指令
    html=''
    html += '<form action="/updateapi" method="GET">'
    html += '<div>odoo path:<input type="text" name="odoopath"/ value="/opt/odoo/"></div>'
    html += '<div>update module:<input type="text" name="module"/ value="wantech_module"></div>'
    html += '<div><input type="submit" value="Update"/></div>'
    html += '</form>'
    return html

@app.route("/updateapi")
def getData():
    odoopath = request.args.get("odoopath")
    module = request.args.get("module")
    os.system("echo 'This is a test %s'" % module)

    return "<div style='color:red'>%s:%s</div>" % (odoopath, module)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
