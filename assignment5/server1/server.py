from flask import Flask,jsonify,request
from empinfo.add import insert_empinfo
from empinfo.display import get_empinfo
from empinfo.delete import delete_empinfo
from empinfo.update import update_empinfo

srv = Flask(__name__)

#homepage
@srv.route('/',methods = ['GET'])
def homepage():
    return "Welcome to empinfo"

#display records 
@srv.route('/emp',methods = ['GET'])
def print_display():   
    return jsonify(get_empinfo())

@srv.route('/empadd',methods = ['POST']) 
def create_emp():
    empid = request.form.get('empid')
    name = request.form.get('name')
    email = request.form.get('email')
    dept = request.form.get('dept')
    mobile_no = request.form.get('mobile_no')

    insert_empinfo(empid,name,email,dept,mobile_no)

    return "Insert Succesful"

@srv.route('/empdel',methods = ['DELETE'])
def delete_emp():
    empid = request.form.get('empid')

    delete_empinfo(empid)

    return f"employee with {empid} empid is deleted"

@srv.route('/empupt',methods = ['PUT']) 
def update_emp():
    choice = request.form.get('choice')
    nvalue = request.form.get('nvalue')
    empid = request.form.get('empid')

    update_empinfo(choice,nvalue,empid)

    return f"employee with {empid} empid is updated" 


if __name__ == '__main__':
    srv.run(host = '0.0.0.0', port=4000, debug=True)
    