from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask!!!"

@app.route('/second')
def second():
    return 'Bize Her Yer Trabzon!!!!'


@app.route('/third/subthird')
def third():
    return 'Bu Sayfa 3. sayfanın alt sayfasıdır!!!'



@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'



if __name__ == '__main__' :
    app.run(debug=True)