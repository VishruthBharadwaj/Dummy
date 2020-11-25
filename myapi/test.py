'''import requests
response=requests.get('http://dummy.restapiexample.com/api/v1/employees')
print(response.__dict__)'''




from flask import Flask
import requests
app = Flask(__name__)
@app.route('/')
def employee():
    response = requests.get("http://dummy.restapiexample.com/api/v1/employees")
    return response.json()
if __name__ == '__main__':
    app.run()


    '''# queryset = Member.objects.all()'''