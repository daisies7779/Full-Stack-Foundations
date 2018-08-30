from flask import Flask
app = Flask(__name__)


#@app.route('/')
#@app.route('/hello')
#@app.route('/hola')
def HelloWorld():
    print "Printers"
    return "Hello World1"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)