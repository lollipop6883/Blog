from flask import Flask, render_template, request

app = Flask(__name__)


#访问路径:http://localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')


#访问路径:http://localhost:5000/list
@app.route('/list')
def list():
    return render_template('list.html')

#访问路径:http://localhost:5000/login
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        #post请求-接收数据请求，并响应给客户端
        username = request.form['username']
        password = request.form['password']
        return "用户名:%s,密码:%s"%(username,password)

if __name__ == "__main__":
    app.run(debug=True)