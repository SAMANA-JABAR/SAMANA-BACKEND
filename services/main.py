#DEFAULT SERVICE
from flask import Flask

app = Flask(__name__)

@app.route('/')
def intro():
    return "Hello This is default page of Samana."

if __name__ == '__main__':
    app.run(debug=True)
