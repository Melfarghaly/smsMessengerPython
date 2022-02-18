import tkinter as tk
import requests
from sendMessage import Messenger
from  rozewail import Rozewail

root = tk.Tk()
root.geometry("600x400")
# declaring string variable
# for storing name and password
center_id_var = tk.StringVar()
airmore_ip = tk.StringVar()

def submit():
    center_id_enterd = center_id_var.get()
    airmore_ip_enered = airmore_ip.get()
   
    #center_id_var.set("")
   # airmore_ip.set("")
    students= Rozewail.get_unsent_msg(center_id_enterd)
    msg_count=str(students['messages_count'])
    msg_count_text="سيتم ارسال رسائل الي  :"+msg_count
    tk.Label(root, text=msg_count_text).grid(row=3, column=1) 
    #start sending messagess =====================
    sms=students['data']
    row_idx=4
    for row in sms:
        mm=Messenger.sendMessage(airmore_ip_enered,row['phone'],row['message']) 
        tk.Label(root, text=row['student_name']).grid(row=int(row_idx), column=1)
        tk.Label(root, text=row['phone']).grid(row=int(row_idx), column=2)
        tk.Label(root, text=row['message']).grid(row=int(row_idx), column=3)
        row_idx+=1
      
    
    tk.Label(root, text="sending done").grid(row=3, column=1) 




# creating a label for
# name using widget Label
group_label = tk.Label(root, text='center id', font=('calibre', 10, 'bold'))
group_entry = tk.Entry(root, textvariable=center_id_var, font=('calibre', 10, 'normal'))
sms_label = tk.Label(root, text='airmore ip ', font=('calibre', 10, 'bold'))
sms_entry = tk.Entry(root, textvariable=airmore_ip, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Submit', command=submit)
group_label.grid(row=0, column=1)
group_entry.grid(row=0, column=2)
sms_label.grid(row=1, column=1)
sms_entry.grid(row=1, column=2)
sub_btn.grid(row=2, column=2)

#parameters={
 #  'group_id':
#}
#response = requests.get(api_url,params=parameters)
#phone_numbers=response.json()
root.mainloop()