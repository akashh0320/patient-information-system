from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy 
from models import db,Patient 

app=Flask(__name__)  
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///patients.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db.init_app(app)  

with app.app_context():
    db.create_all

@app.route('/',methods=['GET','POST']) 
def index():
    return render_template('index.html') 

@app.route('/submit',methods=['POST'])
def submit():
    name = request.form['name'] 
    age = request.form['age'] 
    gender = request.form['gender']
    mobile = request.form['mobile'] 

    patient=Patient(name=name,age=age,gender=gender,mobile=mobile) 
    db.session.add(patient) 
    db.session.commit() 

    return render_template('result.html',name=name,age=age,gender=gender,mobile=mobile)  

@app.route('/patients') 
def patients():
    all_patients=Patient.query.all() 
    return render_template('patients.html',patients=all_patients)
@app.route('/delete/<int:id>') 
def delete(id):
    patient=Patient.query.get(id)
    if patient:
        db.session.delete(patient)
        db.session.commit() 
    return redirect('/patients')

    
if __name__=='__main__': 
    app.run(debug=True) 
        
                              


