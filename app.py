from flask import Flask, render_template,request,session,redirect,url_for,make_response,flash

app=Flask(__name__)
app.secret_key="panda"

@app.route("/")
def index():
    # name='Dipendra'
    # age=16
    # return render_template("index.html",data=name,age=age)
    # data={"name":"Kritika","age":19}
    return render_template("home.html")

# def sayHello():
#     return "Hello BCA"

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# @app.route("/admission")
# def admission():
#     return render_template("admission.html")

@app.route("/admission",methods=['GET','POST'])
def admission():
    if request.method=="POST":
        error=""
        Fullname=request.form['txtname']
        # Address=request.form['txtaddress']
        # Gender=request.form['txtgender']
        # Class=request.form['txtclass']
        # Phone=request.form['txtphone']
        # Age=request.form['txtage']
        if Fullname!="":
            return render_template("studentDetails.html",Fullname=Fullname)
        else:
            error="field is required"
            return render_template("studentDetails.html",error=error)    
        # if Address!="":
        #     return render_template("studentDetails.html",Address)
        # else:
        #     error="field is required"  
        # if Gender!="":
        #     return render_template("studentDetails.html",Gender)
        # else:
        #     error="field is required"    
        # if Class!="":
        #     return render_template("studentDetails.html",Class)
        # else:
        #     error="field is required" 
        # if Phone!="":
        #     return render_template("studentDetails.html",Phone)
        # else:
        #     error="field is required"
        # if Age!="":
        #     return render_template("studentDetails.html",Age)
        # else:
        #     error="field is required"   
    
    return render_template("admission.html")


@app.route("/products")
def products():
    data=[
        {"name":"Marker","price":140,"image":"marker.jpeg","description":"Marker with black ink"},
        {"name":"Pen","price":15,"image":"pen.jpeg","description":"Ball pen with black ink"},
        {"name":"Notebook","price":100,"image":"notebook.jpeg","description":"Long flat notebook"},
        {"name":"Colorpens","price":120,"image":"colorpens.jpeg","description":"12 different colour pens"},
        {"name":"Sticky notes","price":50,"image":"stickynotes.jpeg","description":"Colourful sticky notes"},
        {"name":"Clear Bag","price":30,"image":"clearbag.jpeg","description":"Transparent clear bag"}
    ]
    return render_template("products.html",products=data)
 
@app.route("/login") 
def login():
    return render_template("login.html")

@app.route("/sessiontest")
def demo_session():
    if 'visits' in session:
        session['visits']=session.get('visits')+1
    else:
        session['visits']=1
    return render_template('visits.html')

@app.route('/deletesession')
def delete():
    session.pop('visits') 
    # return redirect("/sessiontest")
    return redirect(url_for('demo_session'))

@app.route("/setcookie")
def cookie():
    resp=make_response("Cookie is Set.")
    # resp.set_cookie('name','value','age')
    resp.set_cookie('user','Dipendra',max_age=60)
    return resp

@app.route("/getcookie")
def getcookie():
    name=request.cookies.get('user')
    return f"Name={name}"

@app.route("/deletecookie")
def deletecookie():
    resp=make_response("Cookie deleted.")
    resp.set_cookie('user','',expires=0)
    return resp

@app.route("/flash")
def set_flash():
    flash("this is message from flash url")
    return redirect(url_for("message"))


@app.route("/message")
def message():
    return render_template("message.html")

if __name__=="__main__":
    app.run(debug=True)
    
