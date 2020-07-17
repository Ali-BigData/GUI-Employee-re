from tools import *
from tkinter import ttk 
from mysqldb import*

def create_table():
    dbrun("""
        CREATE TABLE IF NOT EXISTS employee
          (emp_id int primary key,
            emp_name varchar (99),
            address  varchar (150),
            salary int  )""")



fg='navy'
bg='lightblue'
ft='verdana 16'
pad =3


frm=form('800x600')

button(frm, 'CREATE TABLE',  create_table).pack(pady=pad)
# Making variable for table's values under the FORM.



empid_vr        =intvar()
empname_vr =stringvar()
address_vr    =stringvar()
salary_vr       =intvar()

def clear_emp():
    empid_vr.set(dbautonum('employee' , ' emp_id'))
    empname_vr.set("")
    address_vr.set("")
    salary_vr.set('')
     # This function to close and open buttons.
    frm.winfo_children()[9].config(state='enable')
    frm.winfo_children()[11].config(state='disable')
    frm.winfo_children()[12].config(state='disable')
    frm.winfo_children()[4].focus()# coz did nt give like textbox 4  as used here entry2 then using form.winfo_children.


def add_emp():
    isadd=dbrun(" INSERT INTO employee VALUES ( %d, '%s','%s',%d)"
          %(empid_vr.get(), empname_vr.get(), address_vr.get(), salary_vr.get()))
    

    if isadd :
         msgbox ( "Employee is added.......")
         clear_emp()
    
        
def find_emp():
   
     enum=inbox1("Enter Employee ID :",True)
     row =dbget("SELECT * FROM employee where emp_id=" +str(enum))[0]
    #  row=dbget("SELECT * FROM employee WHERE  emp_id like '%"+enum+"%'  ")[0]
     empid_vr.set( row[0] )
     empname_vr.set( row[1] )
     address_vr.set( row[2] )
     salary_vr.set( row[3] )
     # This function to close and open buttons.
     frm.winfo_children()[9].config(state='disable')
     frm.winfo_children()[11].config(state='enable')
     frm.winfo_children()[12].config(state='enable')
    # print(row) to display on shell.
     
   

def edit_emp():
    isedit=dbrun("UPDATE employee SET  emp_name = ' "+empname_vr .get()+"  ' , address=' "+address_vr.get()+" ' ,salary="+str(salary_vr.get())+" WHERE emp_id = "+str(empid_vr.get())   ) 
    if isedit:
         msgbox('Employee is deited....')
    clear_emp()
         
      
      
                 
    
def delete_emp():
    pass



label (frm,"Employee ID :").pack()
entry2 (frm, empid_vr, True, True ).pack(pady=pad)



label (frm,"Employee Name : ").pack()
#    entry2 (frm, empname_vr, False, False, True).pack()  # can use to show ****** when insert values in box.
entry2 (frm, empname_vr).pack(pady=pad)

label (frm, "Address : ").pack()
entry2 (frm, address_vr).pack(pady=pad)

label (frm, "Salary : ").pack()
entry2 (frm, salary_vr, True ).pack(pady=pad)

button(frm,"Add Employee", add_emp).pack(pady=pad)
button(frm, "Find Employee", find_emp).pack(pady=pad)
button(frm, "Edit Employee", edit_emp).pack(pady=pad)
button(frm, "Delete Employee", delete_emp).pack(pady=pad)
button(frm, "Clear Fields", clear_emp).pack(pady=pad)
button(frm, "Exit", frm.destroy).pack(pady=pad)



       
tkcenter(frm)

bgall(frm, bg)
fgall(frm, fg)
fontall(frm, ft)
justall(frm, "center")
widthall(frm, 15)

clear_emp() #  for making autonumber , clear and focus when open GUI.

frm.mainloop()
    



        
                    
       

        
  

    
