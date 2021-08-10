# This Project made By Rohit Kumar ray
#Code COntributed By Rohit Kumar Ray


from tkinter import* 
from tkinter import messagebox 

root = Tk()
root.geometry('380x500')
root.resizable(False,False)
root.title('HCF and LCM Calculater')

l1 = Label(root ,  text='1st Number',font=20)
l1.grid(row=0,column=0 , padx=20,pady=20)
l2 = Label(root ,  text='2nd Number',font=20)
l2.grid(row=1,column=0)

e1 = Entry(root, font= 20 )
e1.grid(row=0,column=1 , pady=20)
e2 = Entry(root, font= 20 )
e2.grid(row=1,column=1)

def hcfandlcm():
    try:

        v1 = e1.get()
        v2 = e2.get()

        v1 = int(v1)
        v2 = int(v2)

        l5 = Label(root ,  text=f' Your no is {v1} and {v2} ',font=30)
        l5.place(x=50 , y = 200)

        for i in range(1,v1):
            if v1%i==0 and v2%i==0:
                hcf = i
                
        l3 = Label(root ,  text=f'The HCF is {hcf}',font=40)
        l3.place(x=70 , y = 250)

        pro= v1*v2
        lcm = pro/hcf
        lcm = int(lcm)

        l4 = Label(root ,text=f'The LCM is {lcm}',font=40)
        l4.place(x=70, y=300)

        e1.delete(0, END)
        e2.delete(0, END)
    except Exception as e:
        messagebox.showinfo('ROHIT KUMAR' , 'Please Entre Integers')
        e1.delete(0, END)
        e2.delete(0, END)
        
b1 = Button(root , text='Enter' , font=20 ,bg='bisque4',padx=20, command=hcfandlcm )
b1.place(x=120 , y= 120 )

b2 = Button(root , text='Exit' , font=20 ,bg='bisque4',padx=20, command = exit )
b2.place(x=120 , y= 400)

root.mainloop()