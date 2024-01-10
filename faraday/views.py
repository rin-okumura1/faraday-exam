




from datetime import datetime
import email
from email.policy import HTTP
from json import loads
from pickle import GET
import secrets
from ssl import AlertDescription
from turtle import title
import urllib.request, json
from flask import Flask, flash, g, render_template, session
import flask
from faraday import app
from flask import redirect,request,flash


listaDeUsuarios=[]

app.secret_key = 'BAD_SECRET_KEY'


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='faraday',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

def Entra():
    return session.get('email')




@app.route('/members_only',methods=['POST',"GET"])
def members_only():
    print(Entra())
    if Entra()==None:
        print("regresando")
        return redirect('/')
    url=urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts")
    datos = json.load(url)
    print(datos)
    nro=(len(datos))-1
    if request.method=='POST':
        nroI=request.form["id"]
        return render_template('members_only.html',nro=nro,obj=datos[int(nroI)])
    
    return render_template('members_only.html',nro=nro)



@app.route('/registrar',methods=['POST',"GET"])
def registrar():
    if request.method=='POST':
        email=request.form["email"]
        password=request.form["password"]
        listaDeUsuarios.append({"email":email,"password":password})
       
        return redirect("/login")
    else:

        return render_template('registrar.html')



@app.route("/login",methods=['POST',"GET"])
def login():
        if request.method=='POST':
            for i in listaDeUsuarios:
                if i["email"]==request.form["email"] and i["password"]==request.form["password"]:
                   login=i
                   print(i["email"])
                   session["email"]=i["email"]
            if Entra(): 
                return render_template('login.html',msg="sesion iniciada "+Entra())
            
            elif Entra()==None: 
                return render_template('login.html',msg="sesion no iniciada revise sus datos")
        
        return render_template('login.html')

 
@app.route("/logout",methods=['POST',"GET"])
def logout():
    session.pop('email',None)
    return render_template('index.html')


