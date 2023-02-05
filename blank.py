from tkinter import *

root = Tk()
root.geometry('400x400+1400+200')



# for i in range(5):
#     for x in range(5):
#         my = Button(root, text='89')
#         my.grid(row = i, column = x)


#print a line
# for i in range(5):
#     for x in range(5):
#         print(str(i*x), end="")
#     print('next')


#access dict items
# menu = {"ess":{"wa":50, "cof":18},"cost":1.5}
# print(menu['cost'])

var = StringVar()


def butt(x):
    var.set(x)
    print(x)


one = Button(root, text="a", command = lambda:butt("a")).pack()
one_ = Button(root, text="b", command = lambda:butt("b")).pack()

lab = Label(root, textvariable=var).pack()

root.mainloop()