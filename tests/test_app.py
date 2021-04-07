import sys
import app as app_
import flask

app = app_.app
# flask app routes
def test_home():
    with app.test_client() as c:
      r = c.get('/')
      assert(r.status_code == 200)

def test_predict():
    with app.test_client() as c:
      r = c.post('/predict',json={
                "CHAS":{
                    "0":0
                },
                "RM":{
                    "0":6.575
                },
                "TAX":{
                    "0":296.0
                },
                "PTRATIO":{
                    "0":15.3
                },
                "B":{
                    "0":396.9
                },
                "LSTAT":{
                    "0":4.98
                }
                })
      assert(r.status_code == 200)  
