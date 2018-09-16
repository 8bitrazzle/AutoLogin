from tkinter import *
from selenium import webdriver
import tkinter as tk


def donothing():
    print("heckin wacko")


class Buttons:

    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.rowconfigure(0, weight=1, minsize=60)
        frame.columnconfigure(0, minsize=60)
        frame.configure(background="#274863")

        #myfont = Font(family="Times New Roman", size=12)

        photo = PhotoImage(file="source.gif", format="gif -index 50")
        label = Label(frame, image=photo)
        label.image = photo
        label.grid(rowspan=2, columnspan=5)
        label.configure(background="#274863")

        self.ivymain = tk.Button(frame, text="Ivy Tech Login", width=12, font='times', bg="#383a39", fg="#FEFEFC", command=self.ivymain)
        self.ivymain.grid(row=10, column=0, padx=1, pady=20)

        self.ivylearn = tk.Button(frame, text="Ivy Learn Login", width=12, font='times', bg="#383a39", fg="#FEFEFC", command=self.ivylearn)
        self.ivylearn.grid(row=10, column=1, padx=1, pady=1)

        self.mathlab = tk.Button(frame, text="Netacad Login", width=12, font='times', bg="#383a39", fg="#FEFEFC", command=self.mathlab)
        self.mathlab.grid(row=10, column=2, padx=1, pady=1)

        self.quitbutton = tk.Button(frame, text="---- Quit ----", width=12, bg="#383a39", fg="#FEFEFC", font='times', command=frame.quit)
        self.quitbutton.grid(row=10, column=3, padx=1, pady=1)

    def ivymain(self):
        driver = webdriver.Chrome()
        driver.get('Web URL')
        clicky = driver.find_element_by_css_selector('#CSS-Selector')
        clicky.click()  
        username = driver.find_element_by_css_selector('#CSS_Selector_for_username_box')
        username.send_keys('USERNAME')
        password = driver.find_element_by_css_selector('#CSS_Selector_for_password_box')
        password.send_keys('PASSWORD')
        login = driver.find_element_by_css_selector('#CSS_Selector_for_login_button')
        login.click()

    def ivylearn(self):
        driver = webdriver.Chrome()
        driver.get('Web URL')
        username = driver.find_element_by_css_selector('#uCSS_Selector_for_username_box')
        username.send_keys('bwerts@ivytech.edu')
        password = driver.find_element_by_css_selector('#CSS_Selector_for_password_box')
        password.send_keys('PASSWORD')
        login = driver.find_element_by_css_selector('#sCSS_Selector_for_login_button')
        login.click()

    def mathlab(self):
        driver = webdriver.Chrome()
        driver.get('Web URL')
        username = driver.find_element_by_css_selector('#CSS_Selector_for_username_box')
        username.send_keys('USERNAME')
        password = driver.find_element_by_css_selector('#CSS_Selector_for_password_box')
        password.send_keys('PASSWORD')
        login = driver.find_element_by_css_selector('#CSS_Selector_for_login_button')
        login.click()


class dropdowns:

    def __init__(self, master):
        menu = Menu(master)
        master.config(menu=menu)

        subMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=subMenu)
        subMenu.add_command(label="New Project", command=donothing)
        subMenu.add_command(label="New", command=donothing)
        subMenu.add_separator()
        subMenu.add_command(label="Settings", command=donothing)
        subMenu.add_command(label="Exit", command=root.quit)

        edit = Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=edit)
        edit.add_command(label="Undo", command=donothing)
        edit.add_command(label="Redo", command=donothing)
        edit.add_separator()

root = Tk()

root.title("HECKIN NEW GUI")

dropdowns(root)
Buttons(root)

root.mainloop()
