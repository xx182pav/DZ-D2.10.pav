from bottle import Bottle, request
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(dsn="https://57e12d8dd8584bb98c28aa72be50f9df@sentry.io/1827333",integrations=[BottleIntegration()])

app = Bottle()
    
@app.route("/succss")
def succss():

    return 

@app.route("/fail")
def fail():
    raise RuntimeError("There is an error")
    
app.run(host="localhost", port=8080)
