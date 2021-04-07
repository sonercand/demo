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
      r = c.post('/predict')
      assert(r.status_code == 200)  
