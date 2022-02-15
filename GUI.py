import tkinter as tk
import requests
from sendMessage import Messenger

root = tk.Tk()
root.geometry("600x400")
# declaring string variable
# for storing name and password
group_var = tk.StringVar()
sms_var = tk.StringVar()

def submit():
    group = group_var.get()
    sms = sms_var.get()
    print("The id is : " + group)
    print("message is : " + sms)
    group_var.set("")
    sms_var.set("")


# creating a label for
# name using widget Label
group_label = tk.Label(root, text='id group', font=('calibre', 10, 'bold'))
group_entry = tk.Entry(root, textvariable=group_var, font=('calibre', 10, 'normal'))
sms_label = tk.Label(root, text='text message', font=('calibre', 10, 'bold'))
sms_entry = tk.Entry(root, textvariable=sms_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Submit', command=submit)
group_label.grid(row=0, column=0)
group_entry.grid(row=0, column=1)
sms_label.grid(row=1, column=0)
sms_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

#parameters={
 #  'group_id':
#}
#response = requests.get(api_url,params=parameters)
#phone_numbers=response.json()
root.mainloop()