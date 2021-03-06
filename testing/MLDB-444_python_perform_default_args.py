# This file is part of MLDB. Copyright 2015 mldb.ai inc. All rights reserved.


import json
from mldb import mldb

result = mldb.perform("PUT", "/v1/plugins/mirror", [], {
    "type": "python",
    "params":{
        "source":{
            "routes":
"""
from mldb import mldb
mldb.log(str(request.rest_params))
mldb.log(str(request.payload))

request.set_return({
    "args": request.rest_params,
    "payload": request.payload
})
"""}}})
assert result["statusCode"] < 400, result["response"]

successes = 0

rtn = mldb.perform("POST", "/v1/plugins/mirror/routes/pwet")
if rtn["response"] == '{"args":[],"payload":"null\\n"}':
    successes += 1

rtn = mldb.perform("POST", "/v1/plugins/mirror/routes/pwet", [["patate", "5"]])
mldb.log(str(rtn))
if rtn["response"] == '{"args":[["patate","5"]],"payload":"null\\n"}':
    successes += 1

rtn = mldb.perform("POST", "/v1/plugins/mirror/routes/pwet", [["patate", "10"]], {"ataboy": 5})
mldb.log(str(rtn))
if rtn["response"] == '{"args":[["patate","10"]],"payload":"{\\"ataboy\\":5}\\n"}':
    successes += 1

if successes == 3:
    request.set_return("success")
