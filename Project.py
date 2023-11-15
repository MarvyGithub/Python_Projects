from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

root = Tk()

root.title("NEW HORIZON'S STUDENT DATA ENTRY")


student_id_label = Label(root, text="STUDENT'S ID.", padx=1, pady=1)
student_id_label.grid(row=3, column=0)
student_id = Entry(root, border=2, borderwidth=2, highlightthickness=10)
student_id.grid(row=3, column=1)


name_label = Label(root, text="STUDENT'S NAME", padx=1, pady=1)
name_label.grid(row=4, column=0)
name = Entry(root, border=2, borderwidth=2, highlightthickness=10)
name.grid(row=4, column=1)


street_label = Label(root, text="STREET", padx=1, pady=1)
street_label.grid(row=5, column=0)
street = Entry(root, border=2, borderwidth=2, highlightthickness=10)
street.grid(row=5, column=1)


apartment_label = Label(root, text="APARTMENT", padx=1, pady=1)
apartment_label.grid(row=6, column=0)
apartment = Entry(root, border=2, borderwidth=2, highlightthickness=10)
apartment.grid(row=6, column=1)


city_label = Label(root, text="CITY", padx=1, pady=1)
city_label.grid(row=7, column=0)
city = Entry(root, border=2, borderwidth=2, highlightthickness=10)
city.grid(row=7, column=1)


telephone_label = Label(root, text="TELEPHONE", padx=1, pady=1)
telephone_label.grid(row=8, column=0)
phone_no = Entry(root, border=2, borderwidth=2, highlightthickness=10)
phone_no.grid(row=8, column=1)


country_label = Label(root, text="COUNTRY", padx=1, pady=1)
country_label.grid(row=9, column=0)
country= Entry(root, border=2, borderwidth=2, highlightthickness=10)
country.grid(row=9, column=1)


email_label = Label(root, text="EMAIL_ADDRESS", padx=1, pady=1)
email_label.grid(row=10, column=0)
email = Entry(root, border=2, borderwidth=2, highlightthickness=10)
email.grid(row=10, column=1)


course_label = Label(root, text="REGISTERED COURSE", padx=1, pady=1)
course_label.grid(row=11, column=0)

courses_to_amount = {
    'Data Analysis' : 60000, 
    'Advance Excel' : 30000,
    'FrontEnd WebDevelopment': 50000, 
    'BackEnd WebDevelopment': 60000, 
    'FullStack WebDevelopment': 150000, 
    'UI/UX': 80000, 
    'Data Science': 400000,
    'Python': 60000
}

def update_amount(*args):
    selected_course = course.get()
    amount = courses_to_amount.get(selected_course, 0)
    course_amount.delete(0, END)
    course_amount.insert(0, amount)


course = ttk.Combobox(root, values = list(courses_to_amount.keys()), width =2, postcommand=update_amount)
course.grid(row=11, column=1, ipadx=70, ipady=1)
course.bind(update_amount)


course_amount_label = Label(root, text="COURSE AMOUNT", padx=1, pady=1)
course_amount_label.grid(row=12, column=0)
course_amount = Entry(root, border=2, borderwidth=2, highlightthickness=10)
course_amount.grid(row=12, column=1)


payment_type_label = Label(root, text="PAYMENT TYPE", padx=1, pady=1)
payment_type_label.grid(row=13, column=0)
payment_type_lst = ['USSD', 'VISA', 'VERVE', 'MASTERCARD']
options = tk.StringVar()
payment_type = ttk.Combobox(root, textvariable=options, values=payment_type_lst, width= 2)
payment_type.grid(row=13, column=1, ipadx=60, ipady=1)

state_label = Label(root, text="STATE", padx=0, pady=0)
state_label.grid(row=5, column=2)
state = Entry(root, border=2, borderwidth=2, highlightthickness=10)
state.grid(row=5, column=3)

zip_label = Label(root, text="ZIP", padx=0, pady=0)
zip_label.grid(row=6, column=2)
zip = Entry(root, border=2, borderwidth=2, highlightthickness=10)
zip.grid(row=6, column=3)

sex_var =StringVar()
sex_var.set("male")
sex_label = LabelFrame(root, text='Sex', padx=5, pady=0, border=2, borderwidth=5)
sex_label.grid(row=4, column=3, padx=1, pady=1)
sex1 = Radiobutton(sex_label, text='Male', variable=sex_var, padx=10, pady=2, border=10, borderwidth=10, value= 'male')
sex1.deselect()
sex1.grid(row=0, column=0, padx=1, pady=1)
sex2 = Radiobutton(sex_label, text='Female', variable=sex_var, padx=10, pady=2, border=10, borderwidth=10, value='female')
sex2.deselect()
sex2.grid(row=0, column=1, padx=1, pady=1)

discount_var = StringVar()
discount_var.set('High Volume Discount')
high_discount = Checkbutton(root, text='High Volumn Discount', variable=discount_var, onvalue='High Volume Discount', offvalue='Low Volume Discount')
high_discount.deselect()
high_discount.grid(row=7, column=3)
low_discount = Checkbutton(root, text='Low Volumn Discount', variable=discount_var, onvalue='Low Volume Discount', offvalue='High Volume Discount' )
low_discount.deselect()
low_discount.grid(row=8, column=3)


status_var =StringVar()
status_var.set("Corp_member")
status_label = LabelFrame(root, text='Status', padx=5, pady=0, border=2, borderwidth=5)
status_label.grid(row=10, column=3, padx=1, pady=1)
status1 = Radiobutton(status_label, text='Corp member', variable=sex_var, padx=10, pady=2, border=10, borderwidth=10, value= 'male')
status1.deselect()
status1.grid(row=0, column=0, padx=1, pady=1)
status2 = Radiobutton(status_label, text='Non_Corp member', variable=sex_var, padx=10, pady=2, border=10, borderwidth=10, value='female')
status2.deselect()
status2.grid(row=1, column=0, padx=1, pady=1)

conn = sqlite3.connect('New_Horizon_student_Database.db')
c = conn.cursor()
# c.execute("""CREATE TABLE NEW_HORIZON(
#           student_id integer NOT NULL,
#           student_name text NOT NULL,
#           street text NOT NULL,
#           apartment text NOT NULL,
#           city text NOT NULL,
#           phone_no integer NOT NULL,
#           country text NOT NULL,
#           email text NOT NULL,
#           course text NOT NULL,
#           amount integer NOT NULL,
#           payment_type text NOT NULL,
#           sex,
#           state text NOT NULL,
#           zip integer NOT NULL,
#           Discount,
#           status
#           )""")


conn.commit()


def update():
    conn = sqlite3.connect('New_Horizon_student_Database.db')
    c = conn.cursor()

    c.execute("INSERT INTO NEW_HORIZON VALUES (:student_id, :name, :street, :apartment, :city, :phone_no, :country, :email, :course, :amount, :payment_type, :sex, :state, :zip, :Discount, :status)",
            {
                'student_id': student_id.get(),
                'name': name.get(),
                'street': street.get(),
                'apartment': apartment.get(),
                'city': city.get(),
                'phone_no': phone_no.get(),
                'country': country.get(),
                'email': email.get(),
                'course': course.get(),
                'amount': course_amount.get(),
                'payment_type': payment_type.get(),
                "sex": sex_var.get(),
                'state': state.get(),
                'zip': zip.get(),
                "Discount": discount_var.get(),
                'status': status_var.get(),
               
            }
            )

    conn.commit()
    conn.close()  
    #Clear the text boxes
    student_id.delete(0, 'end')
    name.delete(0, 'end')
    street.delete(0, 'end')
    apartment.delete(0, 'end')
    city.delete(0, 'end')
    phone_no.delete(0, 'end')
    country.delete(0, 'end')
    email.delete(0, 'end')
    course.delete(0, 'end')
    course_amount.delete(0, 'end')
    payment_type.delete(0, 'end')
    sex_var.set("male")
    state.delete(0, 'end')
    zip.delete(0, 'end')
    status_var.set("corp_member")
    discount_var.set("'High Volume Discount'")
    messagebox.showinfo("Information for User", "THANK YOU FOR CHOOSING NEW HORIZON")
    
    
    


button_update = Button(root, text= 'Submit Details', padx=10, pady=5, border=10, borderwidth=5, command=update)
button_update.grid(row=12, column=3, columnspan=4)


root.mainloop()