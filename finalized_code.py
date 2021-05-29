import sqlite3
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import ttkthemes as t
import csv
import pandas as pd
from PIL import ImageTk,Image
import re

conn = sqlite3.connect('finaldatabase.db', isolation_level=None,detect_types=sqlite3.PARSE_COLNAMES)
cur = conn.cursor()
def insertion():

    def isValidEmail(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex,email)):
            return True
        return False

    def isValidDate(s):
    	try:
    		year = int(s[:4])
    		month = int(s[5:7])
    		day = int(s[8:])
    		if(year<2020 and month<13 and month>0 and day>0 and day<32):
    			return True
    		return False

    	except:
    		return False

    def isValidExperience(s):
        try:
            if(len(s)!=4):
                return False
            s = int(s)
            if(s>1920 and s<2021):
                return True

                return False
        except:
            return False

    def isValidPhone(s):
        # 1) Begins with 0 or 91
        # 2) Then contains 7 or 8 or 9.
        # 3) Then contains 9 digits
        Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
        return Pattern.match(s)

    def emp_submit():
        name = name_entry.get()
        dob = dob_var.get()
        phone_no = ph_var.get()
        experience = exp_var.get()
        if (len(name) != 0 and len(dob) != 0 and len(phone_no) != 0 and isValidPhone(phone_no) and len(experience) != 0 and isValidDate(dob) and isValidExperience(experience)):
            cur.execute('SELECT COUNT(employee_id) FROM employee_personal_details')
            result = cur.fetchall()
            empId = result[0][0] + 1001
            cur.execute('INSERT INTO employee_personal_details VALUES (?,?,?,?,?)', (empId, name, phone_no, dob, experience))
            conn.commit()
            print('inserted record sucessfully')
            tkinter.messagebox.showinfo("Values inserted", "The values have been inserted")
        else:
            tkinter.messagebox.showinfo("Insertion error ", "One or more of the values entered were null/ value entered was not in the right format")
        name_var.set("")
        exp_var.set("")
        ph_var.set("")
        dob_var.set("")

    def skill_submit():
        #skill_id = skill_id_var.get()
        skill_name = skill_name_var.get()
        if(len(skill_name)>0):
            cur.execute('SELECT COUNT(skill_id) FROM skills')
            result = cur.fetchall()
            skillId = result[0][0] + 2001
            cur.execute('INSERT INTO skills VALUES (?,?)', (skillId, skill_name))
            conn.commit()
            print('inserted record sucessfully')
            tkinter.messagebox.showinfo("Values inserted", "The values have been inserted")
        else:
            tkinter.messagebox.showinfo("NULL Value error ", "The value entered was null")

        skill_name_var.set("")
        #skill_id_var.set("")

    def app_submit():
        app_name = appname_var.get()
        app_dob = appdob_var.get()
        app_phone_no = appph_var.get()
        app_experience = appexp_var.get()
        if (len(app_name) != 0 and len(app_dob) != 0 and len(app_phone_no) != 0 and isValidPhone(app_phone_no) and len(app_experience) != 0 and isValidDate(app_dob) and isValidExperience(app_experience)):
            cur.execute('SELECT COUNT(applicant_id) FROM new_applicants')
            result = cur.fetchall()
            appId = result[0][0] + 3001
            cur.execute('INSERT INTO new_applicants VALUES (?,?,?,?,?)', (appId, app_name, app_phone_no, app_dob, app_experience))
            conn.commit()
            print('inserted record sucessfully')
            tkinter.messagebox.showinfo("Values inserted", "The values have been inserted")
        else:
            tkinter.messagebox.showinfo("Insertion error ", "One or more of the values entered were null/ value entered was not in the right format")
        appname_var.set("")
        appexp_var.set("")
        appph_var.set("")
        appdob_var.set("")

    def client_submit():
        cli_name = cliname_var.get()
        cli_phone_no = cliph_var.get()
        cli_email = cliemail_var.get()
        cli_dob = clidob_var.get()

        if (len(cli_name) != 0 and len(cli_dob) != 0 and len(cli_phone_no) != 0 and isValidPhone(cli_phone_no) and len(cli_email) != 0 and isValidDate(cli_dob) and isValidEmail(cli_email)):
            cur.execute('SELECT COUNT(client_id) FROM client')
            result = cur.fetchall()
            cliId = result[0][0] + 4001
            cur.execute('INSERT INTO client VALUES (?,?,?,?,?)', (cliId, cli_name, cli_phone_no, cli_email, cli_dob ))
            conn.commit()
            print('inserted record sucessfully')
            tkinter.messagebox.showinfo("Values inserted", "The values have been inserted")
        else:
            tkinter.messagebox.showinfo("Insertion error ", "One or more of the values entered were null/ value entered was not in the right format")
        cliname_var.set("")
        cliph_var.set("")
        cliemail_var.set("")
        clidob_var.set("")

    '''def project_details_submit():
        pro_cost = procost_var.get()
        pro_expected_time = protime_var.get()'''

    window = Toplevel(root)
    window.title("Table Value Insertion")
    TAB_CONTROL = ttk.Notebook(window)

    # variables declaration
    name_var = StringVar()
    exp_var = StringVar()
    ph_var = StringVar()
    dob_var = StringVar()
    skill_id_var = StringVar()
    skill_name_var = StringVar()
    appname_var=StringVar()
    appdob_var=StringVar()
    appph_var=StringVar()
    appexp_var=StringVar()
    cliname_var=StringVar()
    cliph_var=StringVar()
    cliemail_var=StringVar()
    clidob_var=StringVar()
    procost_var=StringVar()
    protime_var=StringVar()

    # Employee Table Tab
    TAB1 = ttk.Frame(TAB_CONTROL)
    TAB_CONTROL.add(TAB1, text='Employee Table')

    # Skills Table Tab
    TAB2 = ttk.Frame(TAB_CONTROL)
    TAB_CONTROL.add(TAB2, text='Skills Table')
    TAB_CONTROL.pack(expand=1, fill="both")

    # employee details insertion gui
    name_label = ttk.Label(TAB1, text='Name', font=('calibre', 10, 'normal'))
    name_entry = ttk.Entry(TAB1, textvariable=name_var, font=('calibre', 10, 'normal'))
    ph_label = ttk.Label(TAB1, text='Phone NO', font=('calibre', 10, 'normal'))
    ph_entry = ttk.Entry(TAB1, textvariable=ph_var, font=('calibre', 10, 'normal'))
    exp_label = ttk.Label(TAB1, text='Experience', font=('calibre', 10, 'normal'))
    exp_entry = ttk.Entry(TAB1, textvariable=exp_var, font=('calibre', 10, 'normal'))
    emp_sub_btn = ttk.Button(TAB1, text='Submit', command=emp_submit)
    dob_label = ttk.Label(TAB1, text='Date of birth', font=('calibre', 10, 'normal'))
    dob_entry = ttk.Entry(TAB1, textvariable=dob_var, font=('calibre', 10, 'normal'))

    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    ph_label.grid(row=2, column=0)
    ph_entry.grid(row=2, column=1)
    exp_label.grid(row=1, column=0)
    exp_entry.grid(row=1, column=1)
    dob_label.grid(row=3, column=0)
    dob_entry.grid(row=3, column=1)
    emp_sub_btn.grid(row=4, column=1)
    # employee insertion gui ends here!!

    # skills insertion gui
    #skill_id_label = ttk.Label(TAB2, text='Skill ID', font=('calibre', 10, 'normal'))
    #skill_id_entry = ttk.Entry(TAB2, textvariable=skill_id_var, font=('calibre', 10, 'normal'))
    skill_name_label = ttk.Label(TAB2, text='Skill Name', font=('calibre', 10, 'normal'))
    skill_name_entry = ttk.Entry(TAB2, textvariable=skill_name_var, font=('calibre', 10, 'normal'))
    skill_sub_btn = ttk.Button(TAB2, text='Submit', command=skill_submit)

    #skill_id_label.grid(row=0, column=0)
    #skill_id_entry.grid(row=0, column=1)
    skill_name_label.grid(row=0, column=0)
    skill_name_entry.grid(row=0, column=1)
    skill_sub_btn.grid(row=2, column=1)
    # end of skills insertion gui

    # variables declaration
    app_name_var = StringVar()
    app_dob_var = StringVar()
    app_phone_no_var = StringVar()
    app_experience_var = StringVar()
    cli_name_var = StringVar()
    cli_phone_no_var = StringVar()
    cli_email_var = StringVar()
    cli_dob_var = StringVar()
    pro_cost_var = StringVar()
    pro_expected_time_var = StringVar()

    # New_Applicants Table Tab
    TAB3 = ttk.Frame(TAB_CONTROL)
    TAB_CONTROL.add(TAB3, text='New Applicants Table')

    # Client Table Tab
    TAB4 = ttk.Frame(TAB_CONTROL)
    TAB_CONTROL.add(TAB4, text='Client Table')

    # Project_Details Table Tab
    #TAB5 = ttk.Frame(TAB_CONTROL)
    #TAB_CONTROL.add(TAB5, text='Project Details Table')

    # New_Applicants details insertion gui
    app_name_label = ttk.Label(TAB3, text='Applicant Name', font=('calibre', 10, 'normal'))
    app_name_entry = ttk.Entry(TAB3, textvariable=app_name_var, font=('calibre', 10, 'normal'))
    app_dob_label = ttk.Label(TAB3, text='Applicant DOB', font=('calibre', 10, 'normal'))
    app_dob_entry = ttk.Entry(TAB3, textvariable=app_dob_var, font=('calibre', 10, 'normal'))
    app_phone_no_label = ttk.Label(TAB3, text='Applicant Phone NO', font=('calibre', 10, 'normal'))
    app_phone_no_entry = ttk.Entry(TAB3, textvariable=app_phone_no_var, font=('calibre', 10, 'normal'))
    app_experience_label = ttk.Label(TAB3, text='Applicant Experience', font=('calibre', 10, 'normal'))
    app_experience_entry = ttk.Entry(TAB3, textvariable=app_experience_var, font=('calibre', 10, 'normal'))
    app_sub_btn = ttk.Button(TAB3, text='Submit', command=app_submit)

    app_name_label.grid(row=0, column=0)
    app_name_entry.grid(row=0, column=1)
    app_dob_label.grid(row=1, column=0)
    app_dob_entry.grid(row=1, column=1)
    app_phone_no_label.grid(row=2, column=0)
    app_phone_no_entry.grid(row=2, column=1)
    app_experience_label.grid(row=3, column=0)
    app_experience_entry.grid(row=3, column=1)
    app_sub_btn.grid(row=4, column=1)

    # Client details insertion gui
    cli_name_label = ttk.Label(TAB4, text='Client Name', font=('calibre', 10, 'normal'))
    cli_name_entry = ttk.Entry(TAB4, textvariable=cli_name_var, font=('calibre', 10, 'normal'))
    cli_phone_no_label = ttk.Label(TAB4, text='Client Phone NO', font=('calibre', 10, 'normal'))
    cli_phone_no_entry = ttk.Entry(TAB4, textvariable=cli_phone_no_var, font=('calibre', 10, 'normal'))
    cli_email_label = ttk.Label(TAB4, text='Client EMAIL', font=('calibre', 10, 'normal'))
    cli_email_entry = ttk.Entry(TAB4, textvariable=cli_email_var, font=('calibre', 10, 'normal'))
    cli_dob_label = ttk.Label(TAB4, text='Client DOB', font=('calibre', 10, 'normal'))
    cli_dob_entry = ttk.Entry(TAB4, textvariable=cli_dob_var, font=('calibre', 10, 'normal'))
    cli_sub_btn = ttk.Button(TAB4, text='Submit', command=client_submit)

    cli_name_label.grid(row=0, column=0)
    cli_name_entry.grid(row=0, column=1)
    cli_dob_label.grid(row=1, column=0)
    cli_dob_entry.grid(row=1, column=1)
    cli_phone_no_label.grid(row=2, column=0)
    cli_phone_no_entry.grid(row=2, column=1)
    cli_email_label.grid(row=3, column=0)
    cli_email_entry.grid(row=3, column=1)
    cli_sub_btn.grid(row=4, column=1)

    window.resizable(0, 0)
    window.mainloop()




def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()
def display_employee_personal_details():

    db_df = pd.read_sql_query("SELECT * FROM employee_personal_details", conn)
    db_df.to_csv('employee_personal_details.csv', index=False)
    df = pd.read_csv('employee_personal_details.csv')
    print(df)
    root = Toplevel()
    root.title("Employee personal details")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Employee ID", "Name", "Date", 'Phone No','Experience'), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Employee ID', text="Employee ID", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Date', text="Date", anchor=W)
    tree.heading('Phone No', text="Phone", anchor=W)
    tree.heading('Experience', text="Experience", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.column('#2', stretch=YES, minwidth=0, width=120)
    tree.column('#3', stretch=YES, minwidth=0, width=120)
    tree.column('#4', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('employee_personal_details.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            emp_id = row['employee_id']
            name = row['name']
            dt = row['dob']
            ph = row['phone_no']
            exp= row['experience_from']
            tree.insert("", 0, values=(emp_id, name, dt, ph,exp))
    root.mainloop()



def display_skills():

    db_df = pd.read_sql_query("SELECT * FROM skills", conn)
    db_df.to_csv('skills.csv', index=False)
    df = pd.read_csv('skills.csv')
    print(df)
    root = Toplevel()
    root.title("Skills")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Skill ID", "Skill Name"), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Skill ID', text="Skill ID", anchor=W)
    tree.heading('Skill Name', text="Skill Name", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('skills.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            skl_id = row['skill_id']
            skl_name = row['skill_name']
            tree.insert("", 0, values=(skl_id, skl_name))
    root.mainloop()



def display_employee_skills():

    db_df = pd.read_sql_query("SELECT * FROM employee_skills", conn)
    db_df.to_csv('employee_skills.csv', index=False)
    df = pd.read_csv('employee_skills.csv')
    print(df)
    root = Toplevel()
    root.title("Employee skills ")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Employee ID", "Skill ID"), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Employee ID', text="Employee ID", anchor=W)
    tree.heading('Skill ID', text="Skill ID", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('employee_skills.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            emp_id = row['employee_id']
            skl_id = row['skill_id']
            tree.insert("", 0, values=(emp_id, skl_id))
    root.mainloop()



def display_new_applicants():

    db_df = pd.read_sql_query("SELECT * FROM new_applicants", conn)
    db_df.to_csv('new_applicants.csv', index=False)
    df = pd.read_csv('new_applicants.csv')
    print(df)
    root = Toplevel()
    root.title("New Applicants")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Applicant ID", "Applicant Name", "Phone NO", "DOB"), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Applicant ID', text="Applicant ID", anchor=W)
    tree.heading('Applicant Name', text="Applicant Name", anchor=W)
    tree.heading('Phone NO', text="Phone NO", anchor=W)
    tree.heading('DOB', text="DOB", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.column('#2', stretch=YES, minwidth=0, width=120)
    tree.column('#3', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('new_applicants.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            app_id = row['applicant_id']
            app_name = row['applicant_name']
            ph = row['phone_no']
            dob= row['dob']
            tree.insert("", 0, values=(app_id, app_name, ph,dob))
    root.mainloop()

def display_client():
    db_df = pd.read_sql_query("SELECT * FROM client", conn)
    db_df.to_csv('client.csv', index=False)
    df = pd.read_csv('client.csv')
    print(df)
    root = Toplevel()


    root.title("Client")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Client ID", "Client Name", "Phone NO", "Client Email", "DOB"), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Client ID', text="Client ID", anchor=W)
    tree.heading('Client Name', text="Client Name", anchor=W)
    tree.heading('Phone NO', text="Phone NO", anchor=W)
    tree.heading('Client Email', text="Client Email", anchor=W)
    tree.heading('DOB', text="DOB", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.column('#2', stretch=YES, minwidth=0, width=120)
    tree.column('#3', stretch=YES, minwidth=0, width=120)
    tree.column('#4', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('client.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            cli_id = row['client_id']
            cli_name = row['client_name']
            ph = row['phone_no']
            cliem = row['client_email']
            dob = row['dob']
            tree.insert("", 0, values=(cli_id, cli_name, ph, cliem, dob))
    root.mainloop()


def display_applicant_skills():

    db_df = pd.read_sql_query("SELECT * FROM applicant_skills", conn)
    db_df.to_csv('applicant_skills.csv', index=False)
    df = pd.read_csv('applicant_skills.csv')
    print(df)
    root = Toplevel()
    root.title("Applicant Skills")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Applicant ID", "Skill ID"), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Applicant ID', text="Applicant ID", anchor=W)
    tree.heading('Skill ID', text="Skill ID", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('applicant_skills.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            app_id = row['applicant_id']
            skl_id = row['skill_id']
            tree.insert("", 0, values=(app_id, skl_id))
    root.mainloop()



def display_project_details():

    db_df = pd.read_sql_query("SELECT * FROM project_details", conn)
    db_df.to_csv('project_details.csv', index=False)
    df = pd.read_csv('project_details.csv')
    print(df)
    root = Toplevel()
    root.title("Project details")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Project ID", "Project Cost", 'Expected Time','Client ID'), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Project ID', text="Project ID", anchor=W)
    tree.heading('Project Cost', text="Project Cost", anchor=W)
    tree.heading('Expected Time', text="Expected Time", anchor=W)
    tree.heading('Client ID', text="Client ID", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.column('#2', stretch=YES, minwidth=0, width=120)
    tree.column('#3', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('project_details.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            pro_id = row['project_id']
            pro_cost = row['project_cost']
            et = row['expected_time']
            cli_id= row['client_id']
            tree.insert("", 0, values=(pro_id, pro_cost, et, cli_id))
    root.mainloop()



def display_compensations():

    db_df = pd.read_sql_query("SELECT * FROM compensations", conn)
    db_df.to_csv('compensations.csv', index=False)
    df = pd.read_csv('compensations.csv')
    print(df)
    root = Toplevel()
    root.title("Compensations")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Compensation ID", "Basic Pay", "Concession"), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Compensation ID', text="Compensation ID", anchor=W)
    tree.heading('Basic Pay', text="Basic Pay", anchor=W)
    tree.heading('Concession', text="Concession", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.column('#2', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('compensations.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            comp_id = row['compensation_id']
            bp = row['basic_pay']
            concs = row['concession']
            tree.insert("", 0, values=(comp_id, bp, concs))
    root.mainloop()



def display_current_compensation():

    db_df = pd.read_sql_query("SELECT * FROM current_compensation", conn)
    db_df.to_csv('current_compensation.csv', index=False)
    df = pd.read_csv('current_compensation.csv')
    print(df)
    root = Toplevel()
    root.title("Current Compensation")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Employee ID", "Compensation ID"), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Employee ID', text="Employee ID", anchor=W)
    tree.heading('Compensation ID', text="Compensation ID", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('current_compensation.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            emp_id = row['employee_id']
            comp_id = row['compensation_id']
            tree.insert("", 0, values=(emp_id, comp_id))
    root.mainloop()

    #code to display employee.csv to gui old method
"""
    filewin = Toplevel(root)
    filewin.title("Employee")
    filewin.geometry("600x400")

    #old test code


    with open("employee.csv", newline="") as file:
        reader = csv.reader(file)

        r = 0
        for col in reader:
            c = 0
            for row in col:
                label = tkinter.Label(filewin, width=10, height=2,
                                      text=row, relief=tkinter.RIDGE)
                label.grid(row=r, column=c)
                c += 1
            r += 1
"""

def func1():

    db_df = pd.read_sql_query('''select e.name,sk.skill_name
                                from employee_personal_details e, employee_skills s, skills sk
                                WHERE e.employee_id = s.employee_id AND s.skill_id = sk.skill_id
                                ORDER BY e.name''', conn)
    db_df.to_csv('func1.csv', index=False)
    df = pd.read_csv("func1.csv")
    print(df)
    root = Toplevel()
    root.title("Skills Of An Employee ")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Employee", "Skill"), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Employee', text="Employee", anchor=W)
    tree.heading('Skill', text="Skill", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('func1.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            emp = row['name']
            skl = row['skill_name']
            tree.insert("", 0, values=(emp, skl))
    root.mainloop()

def func3():

    db_df = pd.read_sql_query('''select e.name,sk.skill_name
                                from employee_personal_details e, employee_skills s, skills sk
                                WHERE e.employee_id = s.employee_id AND s.skill_id = sk.skill_id
                                ORDER BY sk.skill_name''', conn)
    db_df.to_csv('func1.csv', index=False)
    df = pd.read_csv('func1.csv')
    print(df)
    root = Toplevel()
    root.title("Skills Of An Employee ")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Skill","Employee"), height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Skill', text="Skill", anchor=W)
    tree.heading('Employee', text="Employee", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('func1.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            emp = row['name']
            skl = row['skill_name']
            tree.insert("", 0, values=(skl,emp))
    root.mainloop()

def func2():

    db_df = pd.read_sql_query('''select c.client_name,p.project_cost,p.expected_time,c.phone_no,c.client_email
                                from project_details p, client c
                                WHERE p.client_id = c. client_id''', conn)
    db_df.to_csv('func2.csv', index=False)
    df = pd.read_csv('func2.csv')
    print(df)
    root = Toplevel()
    root.title("List Of Projects and Clients")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)

    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Client name", "Project Cost", 'Expected Time', 'Client Phone No', 'Client Email'),
                        height=400,
                        selectmode="extended",
                        yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Client name', text="Client name", anchor=W)
    tree.heading('Project Cost', text="Project Cost", anchor=W)
    tree.heading('Expected Time', text="Expected Time", anchor=W)
    tree.heading('Client Phone No', text="Client Phone No", anchor=W)
    tree.heading('Client Email', text="Client Email", anchor=W)
    tree.column('#0', stretch=YES, minwidth=0, width=0)
    tree.column('#1', stretch=YES, minwidth=0, width=120)
    tree.column('#2', stretch=YES, minwidth=0, width=120)
    tree.column('#3', stretch=YES, minwidth=0, width=120)
    tree.column('#4', stretch=YES, minwidth=0, width=120)
    tree.pack()
    with open('func2.csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            cliName = row['client_name']
            pro_cost = row['project_cost']
            et = row['expected_time']
            pho= row['phone_no']
            emi= row['client_email']
            tree.insert("", 0, values=(cliName, pro_cost, et, pho, emi))
    root.mainloop()

def about_page():
    root = Toplevel()
    root.title("About")
    im = ImageTk.PhotoImage(Image.open('about.jpg'))
    panel = ttk.Label(root, image=im)
    #root.geometry("1989 x 707")
    panel.pack(side="bottom", fill="both")
    root.resizable(0, 0)
    root.mainloop()

def customSql():


    try:

        var = sql_var.get()
        db_df = pd.read_sql_query(var, conn)
        db_df.to_csv('custom.csv', index=False)
        df = pd.read_csv('custom.csv')
        filewin = Toplevel(root)
        filewin.title("Custom Sql Query Result")
        filewin.geometry("600x400")
        with open("custom.csv", newline="") as file:
            reader = csv.reader(file)

            r = 0
            for col in reader:
                c = 0
                for row in col:
                    label = tkinter.Label(filewin, width=10, height=2,text=row, relief=tkinter.RIDGE)
                    label.grid(row=r,column=c)
                    c += 1
                r += 1

    except pd.io.sql.DatabaseError:
        tkinter.messagebox.showinfo("Invalid Query ","The query is not valid,please re-check the query")





root = t.ThemedTk(theme="arc")
root.geometry("900x600")
root.title("HR-Management system")
menubar = Menu(root)
insertmenu = Menu(menubar, tearoff=0)
insertmenu.add_command(label="Insert Values", command=insertion)
insertmenu.add_separator()
insertmenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Insert Values", menu=insertmenu)
menubar.add_separator()
tablemenu = Menu(menubar, tearoff=0)
tablemenu.add_command(label="Employee personal details", command=display_employee_personal_details)
tablemenu.add_command(label="Skills", command=display_skills)
tablemenu.add_command(label="Employee skills", command=display_employee_skills)
tablemenu.add_command(label="New Applicants", command=display_new_applicants)
tablemenu.add_command(label="Applicant Skills", command=display_applicant_skills)
tablemenu.add_command(label="Client", command=display_client)
tablemenu.add_command(label="Project details", command=display_project_details)
tablemenu.add_command(label="Compensations", command=display_compensations)
tablemenu.add_command(label="Current Compensation", command=display_current_compensation)
menubar.add_cascade(label="Tables", menu=tablemenu)
menubar.add_separator()
funcmenu = Menu(menubar, tearoff=0)
funcmenu.add_command(label="List Of Employee's skills", command=func1)
funcmenu.add_command(label="List Of Projects and Clients", command=func2)
funcmenu.add_command(label="Search Employee Having Skill", command=func3)
menubar.add_cascade(label="Functions", menu=funcmenu)
menubar.add_separator()
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about_page)
menubar.add_cascade(label="Help", menu=helpmenu)
menubar.add_separator()
root.config(menu=menubar)

sql_var=StringVar()


###Tab Widget
TAB_CONTROL = ttk.Notebook(root)

#tab control home
tabHome = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(tabHome, text = "Home")
# Employee Table Tab
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Custom Sql Command')



#tabhome display gui
img=ImageTk.PhotoImage(Image.open ("home.jpg"))
tabHome_label=ttk.Label(tabHome,image=img)

tabHome_label.grid(sticky="")
TAB_CONTROL.pack(expand=1, fill="both")

sql_label = ttk.Label(TAB1, text='Enter the SQL command : ', font=('calibre', 10, 'normal'))
dummy_label1=ttk.Label(TAB1,text=" ")
sql_entry = ttk.Entry(TAB1, textvariable=sql_var, font=('calibre', 10, 'normal'))
sql_sub_btn = ttk.Button(TAB1, text='Submit', command=customSql)
dummy_label2=ttk.Label(TAB1,text="")
dummy_label3=ttk.Label(TAB1,text=" ")

dummy_label1.grid(row=0, column=0)
sql_label.grid(row=1, column=1)
dummy_label2.grid(row=1, column=0)
dummy_label3.grid(row=2,column=0)
sql_entry.grid(row=1, column=2)
sql_sub_btn.grid(row=3, column=2)
root.resizable(0,0)
root.mainloop()
