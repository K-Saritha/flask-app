from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def function():
    return "<h1>Hello world</h1>"


@app.route('/hello',methods=['GET','POST'])
def hello():
    if request.method=='POST':
        return 'Hello from POST method'
    elif request.method=='GET':
        return 'Hello from GET method'  
    else:
        return 'Unsupported method'

@app.route('/greet/<name>')
def greet(name):
    return f'hello {name}'

@app.route('/add/<int:num1>/<int:num2>')
def add_numbers(num1,num2):
    return f'{num1}+{num2}={num1+num2}'


@app.route('/handle_url_params')
def url_params():
    if 'greetings' in request.args and 'name' in request.args:
        greeting=request.args.get('greetings')
        myname=request.args.get('name') 
        return f'{greeting}, {myname}'
    else:
        return 'Please provide both "greetings" and "name" parameters.'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)