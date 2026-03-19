from flask import Flask,request,render_template,redirect,url_for
import modules.calculations as calc
import modules.placeholder as p
import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
logger=logging.getLogger(__name__)
app=Flask(__name__)

@app.route('/')
def function():
    return render_template('index.html', name="saritha")


@app.route('/todos/<int:id>')
def todos(id):
    return p.get_all_todos(id)


@app.route('/hello',methods=['GET','POST'])
def hello():
    if request.method=='POST':
        return 'Hello from POST method'
    elif request.method=='GET':
        return 'Hello from GET method'  
    else:
        return 'Unsupported method'

@app.route('/calc',methods=['POST'])
def calculate():
    num1=int(request.form.get('num1',0))
    num2=int(request.form.get('num2',0))
    result=calc.add(num1,num2)
    return f'The sum of {num1} and {num2} is {result}'

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




@app.template_filter('reverse')
def reverse_filter(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat_filter(s,time=3):
    return s*time

@app.route('/items')
def list_items():
    values=[10,20,30,40,50]
    return render_template('items.html', items=values)


@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('list_items'))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
