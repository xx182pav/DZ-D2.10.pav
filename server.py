from bottle import Bottle, request
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(dsn="Enter your SDN",integrations=[BottleIntegration()])

app = Bottle()
    
@app.route("/succss")
def succss():

    return 

@app.route("/fail")
def fail():
    raise RuntimeError("There is an error")
    
app.run(host="localhost", port=8080)
