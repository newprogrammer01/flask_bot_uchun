from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'
@app.route('/jasurbek')
def main():
    return 'bu sayt sinov tariqasida yasalgan'
if __name__ == '__main__':
    app.run()