from flask import Flask,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)




#路由：将URL映射到函数上。
#动态生成页面示例。<name>默认是字符串，<int:id>则指定为整数。int\float\path也可以使用
#path类型也是字符串，但不把斜线是做分隔符而是动态片段的一部分

#模板的渲染
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
@app.route('/')
def index():
    return render_template('index.html')
#错误信息
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')
#启动服务器
if __name__=='__main__':
    app.run(debug=True)


    

