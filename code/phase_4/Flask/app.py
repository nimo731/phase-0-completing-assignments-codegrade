#setting up the virtual environment
#setting up A flask application
#impor the Flask class from the flask module
#create an instance of the Flask class
#use the route() decorator to tell Flask what URL should call the function



from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/welcome/<name>')
def student( name):
    return f'<h1>welcome to phase 4 sn Developer {name}!<h1>'


@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    result = num1 + num2
    return f'<h1> Sum of {num1} and {num2} is {result}<h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0' , port=5000, debug=True)