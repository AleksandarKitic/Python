import random
import tkinter as tk
import matplotlib.pyplot as plt
import datetime


class Application1:
    def bricks(self):
        root = tk.Tk()
        root.configure(background='#D3D3D3')
        root.geometry('900x600')
        root.title('Works platform')

        user1 = Login_User()
        user1_reg = RegistrationUser()

        tk.Button(root, text='Login', bg='#D3D3D3', fg='red', command=user1.login_user1).grid(row=0, column=1,
                                                                                              sticky=tk.W, pady=6)
        tk.Button(root, text='Register', bg='#D3D3D3', fg='black', command=user1_reg.reg_user1).grid(row=0, column=2,
                                                                                              sticky=tk.W, pady=6)
        root.mainloop()


class RegistrationUser:
    def reg_user1(self):
        master_reg = tk.Tk()
        master_reg.geometry('300x280')
        master_reg.title('Registration')

        tk.Label(master_reg, text='Username:').grid(row=0)
        tk.Label(master_reg, text='Password').grid(row=1)

        username_reg = tk.Entry(master_reg)
        password_reg = tk.Entry(master_reg, show='*')
        username_reg.grid(row=0, column=1)
        password_reg.grid(row=1, column=1)

        def checkreg():
            user_reg = []

            usern = username_reg.get()
            passw = password_reg.get()

            user_reg.append(usern)
            user_reg.append(passw)
            print(f'Your registration is done!')

            nex = Application()
            nex.softapp()

        tk.Button(master_reg, text='Quit', bg='#D3D3D3', fg='black', command=master_reg.destroy).grid(row=3, column=1,
                                                                                              sticky=tk.W, pady=4)
        tk.Button(master_reg, text='Register', bg='#D3D3D3', fg='red', command=checkreg).grid(row=3, column=2,
                                                                                           sticky=tk.W, pady=4)

class Login_User:
    def login_user1(self):
        master = tk.Tk()
        master.geometry('300x280')
        master.title('Login')

        tk.Label(master, text='Username:').grid(row=0)
        tk.Label(master, text='Password:').grid(row=1)

        username = tk.Entry(master)
        password = tk.Entry(master, show='*')
        username.grid(row=0, column=1)
        password.grid(row=1, column=1)

        def checkinguser():
            usern = username.get()
            passw = password.get()

            correct_username = 'Admin'
            correct_password = 'Admin'

            if usern == correct_username and passw == correct_password:
                print('You are login!')
                user2 = Application()
                user2.softapp()
            elif usern != correct_username and passw != correct_password:
                print('ERROR! Username and password is incorrect!')
            else:
                print('ERROR! Insert the username and password!')

        tk.Button(master, text='Quit', bg='#D3D3D3', fg='black', command=master.destroy).grid(row=3, column=1,
                                                                                              sticky=tk.W, pady=4)
        tk.Button(master, text='Login', bg='#D3D3D3', fg='red', command=checkinguser).grid(row=3, column=2,
                                                                                           sticky=tk.W, pady=4)


class Application:
    def softapp(self):
        root = tk.Tk()
        root.geometry('600x400')
        root.title('User')
        open_class = Diagram()

        def profile_user():
            master = tk.Tk()
            master.title('Profile User')
            master.geometry('600x400')

            tk.Label(master, text='Name User:').grid(row=0)
            tk.Label(master, text='Lastname User:').grid(row=1)
            tk.Label(master, text='Sex:').grid(row=2)
            tk.Label(master, text='Age:').grid(row=3)
            tk.Label(master, text='Country:').grid(row=4)

            name_user = tk.Entry(master)
            lastname_user = tk.Entry(master)
            sex_user = tk.Entry(master)
            age_user = tk.Entry(master)
            country_user = tk.Entry(master)

            name_user.grid(row=0, column=1)
            lastname_user.grid(row=1, column=1)
            sex_user.grid(row=2, column=1)
            age_user.grid(row=3, column=1)
            country_user.grid(row=4, column=1)

            def save_user():
                name_get_user = name_user.get()
                lastname_get_user = lastname_user.get()
                sex_get_user = sex_user.get()
                age_get_user = age_user.get()
                country_get_user = country_user.get()

                master1 = master

                txt_box_user = tk.Text(master1, width=50, height=5)
                txt_box_user.grid(row=15, column=1, columnspan=2)
                txt_box_user.insert('end-1c', f"Name: {name_get_user}\n")
                txt_box_user.insert('end-1c', f"Lastname: {lastname_get_user}\n")
                txt_box_user.insert('end-1c', f"Sex: {sex_get_user}\n")
                txt_box_user.insert('end-1c', f"Age: {age_get_user}\n")
                txt_box_user.insert('end-1c', f"Country: {country_get_user}")

                times_prints = datetime.datetime.now()
                times_prints_pm = datetime.datetime.now()

                print(f"You save the profile.\n Time: {times_prints} {times_prints_pm.strftime('%p')}")

            tk.Button(master, text='Save', fg='red', bg='#D3D3D3', command=save_user).grid(row=5, column=2, sticky=tk.W,
                                                                                                                pady=4)

        tk.Button(root, text='Logout', command=root.destroy, bg='#D3D3D3', fg='red',).grid(row=4, column=0,
                                                                                           sticky=tk.W, pady=4)
        tk.Button(root, text='Profile', command=profile_user, bg='#D3D3D3', fg='red',).grid(row=4, column=1,
                                                                                            sticky=tk.W, pady=4)

        tk.Button(root, text='Diagram', command=open_class.application1, bg='#D3D3D3', fg='black').grid(row=4, column=3,
                                                                                                    sticky=tk.W, pady=4)
        tk.Label(root, text='Name Product:').grid(row=0)
        tk.Label(root, text='Price:').grid(row=1)
        tk.Label(root, text='Date:').grid(row=2)
        tk.Label(root, text='Transport:').grid(row=3)

        name_product = tk.Entry(root)
        price_product = tk.Entry(root)
        date_product = tk.Entry(root)
        transport_product = tk.Entry(root)

        name_product.grid(row=0, column=1)
        price_product.grid(row=1, column=1)
        date_product.grid(row=2, column=1)
        transport_product.grid(row=3, column=1)

        def check_product():
            master = tk.Tk()
            master.geometry('400x200')
            master.title('Message!')
            prod_lists = []

            name_get_product = name_product.get()
            price_get_product = price_product.get()
            date_get_product = date_product.get()
            transport_get_product = transport_product.get()

            all_msg = name_get_product, price_get_product, date_get_product, transport_get_product

            prod_lists.append(all_msg)

            txt_bx = tk.Text(master, width=150, height=20)
            txt_bx.grid(row=0, column=0, columnspan=2)
            txt_bx.insert('end-1c', f"Name: {name_get_product}\n")
            txt_bx.insert('end-1c', f"Price: {price_get_product}\n")
            txt_bx.insert('end-1c', f"Date: {date_get_product}\n")
            txt_bx.insert('end-1c', f"Transport: {transport_get_product}")
            time_y = datetime.datetime.now()
            time_x = datetime.datetime.now()

            print('-' * 30)
            print(f'Your message send at {time_y} {time_x.strftime("%p")}')
            print('-' * 30)
            print(all_msg)
            print('-' * 30)

        tk.Button(root, text='Send', command=check_product, fg='red', bg='#D3D3D3').grid(row=4, column=4, pady=4,
                                                                                       sticky=tk.W)
        root.mainloop()


class Diagram:
    def application1(self):
        root1 = tk.Tk()
        root1.geometry('600x400')
        root1.title('Diagram')

        def line():
            x = []
            y = []
            name_insert = input('Product Name: ')

            for i in range(1, 16):
                p = random.randrange(1, 16)
                x.append(i)
                y.append(p)

            plt.plot(x, y, label='Products Sells', color='green', linestyle='--', linewidth='1', marker='o',
                                                                                                        markersize='4')
            plt.rc('grid', linestyle='--', color='#bbb')
            plt.title(f"{name_insert} Diagram 2021", fontdict={'fontname': 'Courier New', 'fontsize': 20})
            plt.xlabel("Days", fontdict={'fontname': 'Courier New', 'fontsize': 20})
            plt.ylabel("Statistics", fontdict={'fontname': 'Courier New', 'fontsize': 20})
            plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
            plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
            plt.legend()
            plt.grid()
            plt.show()

        def bar():
            x = []
            y = []
            name_insert = input('Product Name: ')

            for n in range(1, 16):
                p = random.randrange(1, 16)
                x.append(n)
                y.append(p)

            plt.bar(x, y, label='Products Sells', align='center', color='green')
            plt.title(f"{name_insert} Diagram 2021", fontdict={'fontname': 'Courier New', 'fontsize': 20})
            plt.xlabel("Days", fontdict={'fontname': 'Courier New', 'fontsize': 20})
            plt.ylabel("Statistics", fontdict={'fontname': 'Courier New', 'fontsize': 20})
            plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
            plt.yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
            plt.legend()
            plt.show()

        tk.Button(root1, text='Line', command=line, bg='#D3D3D3', fg='red').grid(row=1, column=0, pady=4, sticky=tk.W)
        tk.Button(root1, text='Bar', command=bar, bg='#D3D3D3', fg='red').grid(row=1, column=1, pady=4, sticky=tk.W)


a = Application1()
a.bricks()
