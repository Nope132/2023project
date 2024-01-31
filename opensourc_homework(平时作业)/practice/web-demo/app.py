#!/usr/bin/python
#coding utf-8
from flask import Flask,request,render_template
app= Flask(__name__)

#GET?name=zhangsan

@app.route("/hello")
def hello():
	name =request.args.get("name","anonymous")
	return render_template("hello.html",name=name)

if __name__=="__main__":
	app.run()

#CGI common gateway interface
#MVC: model view controller