from flask import Flask          

app = Flask(__name__)

@app.route('/<rule>/<int:value>')
def conversion(rule, value):
    return str(f_to_c(value))

def f_to_c(f):
    return ((f - 32)/9.0) * 5

if __name__ == "__main__":
    app.run()