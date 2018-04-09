from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import os

class Nameform(FlaskForm):
    name = StringField('What is s your name',validators = [DataRequired()])
    submit = SubmitField('Submit')


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tell me why'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
bootstrap = Bootstrap(app)



#数据库系列database


db = SQLAlchemy(app)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64),unique = True)
    users = db.relationship('User',backref = 'role')
    def __repr__(self):
        return '<Role %r>' % self.name
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(64),unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username



#路由：将URL映射到函数上。
#动态生成页面示例。<name>默认是字符串，<int:id>则指定为整数。int\float\path也可以使用
#path类型也是字符串，但不把斜线是做分隔符而是动态片段的一部分

#模板的渲染
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
@app.route('/',methods = ['GET','POST'])
def index():
    name = None
    form = Nameform()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    flash('Hello Everyone')
    return render_template('index.html',form = form , name = session.get('name'))
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


    

