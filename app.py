from flask import Flask

app = Flask(__name__)
DEBUG = True
# 配置mysql 数据库
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:3306/project'
SQLALCHEMY_TRACK_MODIFICATIONS = True
# redis 配置

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/new_root/<name>')
def haha(name):
    return '创建路由%s'%name



def xinde():
    print('aaaa')
    return '稽查试图%s'

@app.route('/word')
def word():
    return '页面错误',404

app.add_url_rule('/new1/',view_func=xinde)



if __name__ == '__main__':
    app.run()
