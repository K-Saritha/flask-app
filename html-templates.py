from flask import Flask,render_template
app=Flask(__name__, template_folder='templates')
@app.route('/')
def function():
    value=30
    name="saritha"
    return render_template('index.html',value=value,name=name)

@app.route('/items')
def list_items():
    values=[10,20,30,40,50]
    return render_template('items.html', items=values)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)