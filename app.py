from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def function():
    return "<h1>Hello world</h1>"




@app.route('/greet/<name>')
def greet(name):
    return f'hello {name}'

@app.route('/add/<int:num1>/<int:num2>')
def add_numbers(num1,num2):
    return f'{num1}+{num2}={num1+num2}'


@app.route('/handle_url_params')
def url_params():
    greeting=request.args.get('greetings')
    myname=request.args['name']
    
    return f'{greeting}, {myname}'


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)