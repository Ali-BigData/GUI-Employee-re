from tkinter import Tk # This for Form Central function.
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel # This for general inbox
from tkinter import StringVar
from tkinter import IntVar
from tkinter import BooleanVar
from tkinter import Listbox
from tkinter import Frame


# Stringvar reference.

def stringvar():
    return StringVar()

# Intvar reference.

def intvar():
    return IntVar()

# Booleanvar reference.

def booleanvar():
    return BooleanVar()

# Frame reference.

def frame(form,bg=None):
    if bg!=None:
        return Frame(form,bg=bg)
    else:
        return Frame(form)



# Central Form reference.

def form(geometry='450x300',title='',iscenter=True):  # geometry is default.
    f=Tk()
    f.geometry(geometry)
    f.title(title)
    if iscenter:
        tkcenter(f)
    return f

# Toplevel reference.

def toplevel(geometry='350x200',title='',iscenter=True):  # geometry is default.
    f=Toplevel()
    f.geometry(geometry)
    f.title(title)
    if iscenter:
        tkcenter(f)
    return f


# Button function.

def button (form, text='Button',command=None):# Button = botton default , also possible set text only.
    btn=ttk.Button(form,text= text)
    if command != None:    # Command reference function.
        btn.config(command=command)
    return btn


# Button function.

def label(form,text='Label'):
    return ttk.Label(form,text=text)

# Entry function.

def entry(form):
    txt=ttk.Entry(form)
    return txt

# Entry function accept only number.

def entry1(form,isnumber=False):# False mean dosnt work this function only when put True.
    
     def onlynumber(text):
        if str.isdigit(text):
            True
        elif text=='':
            return True    
        else:
            return False
     reg=form.register(onlynumber)
     
     txt=ttk.Entry(form)
     if isnumber:
         txt.config(validate='key', validatecommand=(reg,'%P'))
     return txt


# Entry function with variable and accept only number.


def entry2(form,variable= None,isnumber=False, read_only=False ,password =False):
    
     def onlynumber(text):
        if str.isdigit(text):
            True
        elif text=='':
            return True    
        else:
            return False
     reg=form.register(onlynumber)
     
     txt=ttk.Entry(form)
     if password==True:      # to give *** in password.
         txt.config( show='*')
     if read_only== True:         # For reading only
         txt.config(state='readonly')
     if isnumber:
         txt.config(validate='key', validatecommand=(reg,'%P'))
     if variable!=None:
         txt.config(textvariable=variable)
    
    
     return txt


# Radiobutton reference.

def radio(form,text='Radio',value=0,variable=None):
    rdo=ttk.Radiobutton(form,text=text,value=value)
    if variable!=None:
        rdo.config(variable=variable)
    return rdo

# Checkbox

def checkbutton(form, text='Checkbox',variable=None):
    cbx=ttk.Checkbutton(form, text=text)
    if variable !=None:
        cbx.config(variable=variable)
    return cbx

# Combobox reference.

def combobox(form, values=None, readonly=False):
    cbx=ttk.Combobox(form)
    if values!=None:
        cbx.config(values=values)
    if readonly:
        cbx.config(state='readonly')
    return cbx
    
# Listbox reference.

def listbox(form, values=None):
    lbx=Listbox(form)
    
    if values!= None:
        i=0
        for x in values:
            lbx.insert(i,x)
            i+=1
    return lbx

# central form reference.

def tkcenter(form):
    form.update()
    fw=form.winfo_width()
    fh=form.winfo_height()
    sw=form.winfo_screenwidth()
    sh=form.winfo_screenheight()
    x=(sw-fw)/2
    y=(sh-fh)/2 -45
    form.geometry('%dx%d+%d+%d' %( fw,fh,x,y))
 
# All tools fpr Background reference.

def bgall(form,bg):
    form.update()
    form.config(bg=bg)
    contr=form.winfo_children() # for all tools.
    my=ttk.Style()
    my.configure('TLabel',background=bg)
    my.configure('TButton',background=bg)
    my.configure('TEntry',background=bg)
    my.configure('TRadiobutton',background=bg)
    my.configure('TCheckbutton',background=bg)
    
    for v in contr:
        if v.winfo_class()=='Frame': # This for applying in 'Frame' function.
            bgall(v,bg)

        try:
            v['bg']=bg
        except:
            pass
        try:
            v['background']=bg
        except:
            pass
      
           
            
# All tools for font reference.

def fontall(form,font):
    form.update()
    conts=form.winfo_children() # for all tools.
    my=ttk.Style()
    my.configure('TLabel', font=font)
    my.configure('TButton', font=font)
    my.configure('TEntry', font=font)
    my.configure('TRadiobutton', font=font)
    my.configure('TCheckbutton',font=font)

    for y in conts:

        if y.winfo_class()=='Frame':fontall(y,font)# This for applying in 'Frame' function.
     
        try:
            y['font']=font
        except:
            pass
        
        
            
# All tools for frontground reference.

def fgall(form,fg):
    form.update()
    cotz=form.winfo_children()
    
    my=ttk.Style()
    my.configure('TLabel',foreground=fg) # Hint shoud write foreground.
    my.configure('TButton',foreground=fg)
    my.configure('TEntry',foreground=fg)
    my.configure('TRadiobutton',foreground=fg)
    my.configure('TCheckbutton',foreground=fg)

    for c in cotz:
        if c.winfo_class()=='Frame':# This for applying in 'Frame' function.
            fgall(c,fg)
        try:
            c['fg']=fg
        except:
            pass 

           
# Justify tools  for setting frontground in center of box.

def justall(form,just):
    form.update()
    cotz=form.winfo_children()
    
    my=ttk.Style()
    my.configure('TButton', justify=just)# Hint shoud write foreground
    my.configure('TRadiobutton', justify=just)
    my.configure('TCheckbutton', justify=just)

    for c in cotz:
        if c.winfo_class()=='Frame':# This for applying in 'Frame' function.
            justall(c,just)
        try:
            c['justify']=just
        except:
            pass

# Width tools  for setting width.

def widthall(form, mywidth):
    form.update()
    cotz=form.winfo_children()
    
    my=ttk.Style()
    my.configure('TButton', width=mywidth)# Hint shoud write foreground
    my.configure('TRadiobutton', width=mywidth)
    my.configure('TCheckbutton', width=mywidth)

    for c in cotz:
        if c.winfo_class()=='Frame':# This for applying in 'Frame' function.
            widthall(c, mywidth)
        try:
            c['width']=mywidth
        except:
            pass

    
            
# for messagebox showinfo.

def msgbox(text):
    messagebox.showinfo('',text)
    
# for messagebox askyesno.

def msgask (text):
    return messagebox.askyesno('',text)

# Generate input box.
def inbox(text):
    f=Toplevel()
    f.title(text)
    f.geometry('400x150')
    f.resizable(False,False)
    tkcenter(f)
    ttk.Label(f, text=text,font='None 15').pack(pady=10)
    sv=StringVar()
    txt=ttk.Entry(f,font='None 15', width=35, textvariable=sv)
    txt.pack(pady=10)
    txt.bind('<Return>',lambda my:f.destroy())

    ttk.Style().configure('Ali.TButton',font='None=15')# setting name.TButton to custmize font when applying.
    ttk.Button(f,text='OK',command=lambda: f.destroy(),style='Ali.TButton')
    f.grab_set()
    txt.focus()
    f.wait_window()#This method for make sure closing window before return.
    return sv.get()

# Generate input box accept only number.
def inbox1(text,isnumber=False):# False mean  this  function is off only work when insert True.
    f=Toplevel()
    f.title(text)
    f.geometry('400x150')
    f.resizable(False,False)
    tkcenter(f)
    ttk.Label(f, text=text,font='None 15').pack(pady=10)
    sv=StringVar()

    def onlynumber(text):
        if str.isdigit(text):
            return True
        elif text=='':
                True
        else:
            return False
    reg=f.register(onlynumber)
        
        
    txt=ttk.Entry(f,font='None 15', width=35, textvariable=sv)
    if isnumber:
        txt.config(validate='key', validatecommand= (reg,'%P'))
    txt.pack(pady=10)
    txt.bind('<Return>',lambda my:f.destroy())

    ttk.Style().configure('Ali.TButton',font='None=15')# setting name.TButton to custmize font when applying.
    ttk.Button(f,text='OK',command=lambda: f.destroy(),style='Ali.TButton')
    f.grab_set()
    txt.focus()
    f.wait_window() #This method for make sure closing window before return.
    return sv.get()


                          
                          
                          
    
    


 
             

        

        
            
        


            
       
        


          
        

            
