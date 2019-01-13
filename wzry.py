from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#建立窗口
root = Tk()
root.title("王者荣耀")
root.iconbitmap(r'icon.ico')
root.geometry('360x640+50+100')
root.resizable(False,False)
root.configure(background='#D8BFD8')

#设置风格
style=ttk.Style()
style.configure('TFrame',background='#921118', foreground='#fbda73')
style.configure('TButton',background='#921118', font=('微软雅黑',12))
style.configure('TLabel',background='#921118', foreground='#fbda73', font=('微软雅黑',15))
style.configure('TRadiobutton',background='#921118', foreground='#fbda73', font=('微软雅黑',15))
style.configure('Header.TLabel', foreground='#fbda73', font=('微软雅黑', 15, 'bold'))

#切换页面
def raise_frame(frame):
    frame.tkraise()

f0 = ttk.Frame(root)
f1 = ttk.Frame(root)
f2 = ttk.Frame(root)
f3 = ttk.Frame(root)
f4 = ttk.Frame(root)
f5 = ttk.Frame(root)

for frame in (f0, f1, f2, f3, f4, f5):
    frame.grid(row=0, column=0, sticky='news')
    frame.grid_propagate(0)  #force a widget to be a certain size, regardless of the size of its contents. 
    frame.config(borderwidth=5, relief="solid", width=360, height=640)

#答案反馈
def grade():
    score=0
    correct_answers=[3, 4, 3, 4, 3]
    user_answers=[v1.get(), v2.get(), v3.get(), v4.get(), v5.get()]
    for a, b in zip(user_answers, correct_answers):
        if a==b:
            score=score+1
        else:
            score=score+0
        
    if score==len(correct_answers):
        messagebox.showinfo(title="答案", message="恭喜！你正确回答了所有的问题，春节限定皮肤奖励已发出，赶紧登录你的帐号领取吧。")
    else:
        messagebox.showinfo(title="答案", message="很遗憾，你只答对了"+str(len(correct_answers))+"道题目中的"+str(score)+"道题，明天再来试试吧。")

#第0页
pic1=PhotoImage(file="startpic.png")
ttk.Label(f0,image=pic1).grid(row=0, column=0, columnspan=2)
button1=ttk.Button(f0, text='开始答题', command=lambda:raise_frame(f1))
button1.place(x=180, y=600, anchor="center")

#第1页
pf=ttk.Frame(f1)
pf.pack(pady=5)
logo1=PhotoImage(file="lbqh.png")
ttk.Label(pf,image=logo1).pack()

tf=ttk.Frame(f1)
tf.pack(side=LEFT, anchor='nw')

label1=ttk.Label(tf, text="1. 鲁班七号是哪种类型的英雄？")
label1.grid(row=0, column=0, columnspan=2, padx=10)

label2=ttk.Label(tf)
label2.grid(row=1, column=0, columnspan=2)  #插入一空行

v1= IntVar()
ttk.Radiobutton(tf, text="法师", variable=v1, value=1).grid(row=2, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="刺客", variable=v1, value=2).grid(row=3, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="射手", variable=v1, value=3).grid(row=4, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="小学生", variable=v1, value=4).grid(row=5, column=0,columnspan=2, padx=35, sticky="w")

button1=ttk.Button(f1, text='返回', command=lambda:raise_frame(f0))
button1.place(x=120, y=600, anchor="center")
button2=ttk.Button(f1, text='下一题', command=lambda:raise_frame(f2))
button2.place(x=240, y=600, anchor="center")

#第2页
pf=ttk.Frame(f2)
pf.pack(pady=5)
logo2=PhotoImage(file="ssx.png")
ttk.Label(pf,image=logo2).grid(row=0, column=0, columnspan=2, padx=10)

tf=ttk.Frame(f2)
tf.pack(side=LEFT, anchor='nw')

label1=ttk.Label(tf, text='''2. "大小姐驾到，通通闪开！"大小姐\n是指以下哪个英雄？''')
label1.grid(row=0, column=0, columnspan=2, padx=10)

label2=ttk.Label(tf)
label2.grid(row=1, column=0, columnspan=2)  #插入一空行

v2= IntVar()
ttk.Radiobutton(tf, text="虞姬", variable=v2, value=1).grid(row=2, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="花木兰", variable=v2, value=2).grid(row=3, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="韩懿莹", variable=v2, value=3).grid(row=4, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="孙尚香", variable=v2, value=4).grid(row=5, column=0,columnspan=2, padx=35, sticky="w")

button1=ttk.Button(f2, text='上一题', command=lambda:raise_frame(f1))
button1.place(x=120, y=600, anchor="center")
button2=ttk.Button(f2, text='下一题', command=lambda:raise_frame(f3))
button2.place(x=240, y=600, anchor="center")

#第3页
pf=ttk.Frame(f3)
pf.pack(pady=5)
logo3=PhotoImage(file="wzj.png")
ttk.Label(pf,image=logo3).grid(row=0, column=0, columnspan=2)

tf=ttk.Frame(f3)
tf.pack(side=LEFT, anchor='nw')

label1=ttk.Label(tf, text="3. 以下哪个属于王昭君的皮肤？")
label1.grid(row=0, column=0, columnspan=2, padx=10)

label2=ttk.Label(tf)
label2.grid(row=1, column=0, columnspan=2)  #插入一空行

v3= IntVar()
ttk.Radiobutton(tf, text="黑猫爱糖果", variable=v3, value=1).grid(row=2, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="仲夏夜之梦", variable=v3, value=2).grid(row=3, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="凤凰于飞", variable=v3, value=3).grid(row=4, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="天鹅之梦", variable=v3, value=4).grid(row=5, column=0,columnspan=2, padx=35, sticky="w")

button1=ttk.Button(f3, text='上一题', command=lambda:raise_frame(f2))
button1.place(x=120, y=600, anchor="center")
button2=ttk.Button(f3, text='下一题', command=lambda:raise_frame(f4))
button2.place(x=240, y=600, anchor="center")

#第4页
pf=ttk.Frame(f4)
pf.pack(pady=5)
logo4=PhotoImage(file="lb.png")
ttk.Label(pf,image=logo4).grid(row=0, column=0, columnspan=2)

tf=ttk.Frame(f4)
tf.pack(side=LEFT, anchor='nw')

label1=ttk.Label(tf, wraplength=350, text='''4. 吕布使用的武器叫什么名字？''')
label1.grid(row=0, column=0, columnspan=2, padx=10)

label2=ttk.Label(tf)
label2.grid(row=1, column=0, columnspan=2)  #插入一空行

v4= IntVar()
ttk.Radiobutton(tf, text="无尽战刃", variable=v4, value=1).grid(row=2, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="冰霜长矛", variable=v4, value=2).grid(row=3, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="无敌鲨嘴炮", variable=v4, value=3).grid(row=4, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="方天画戟", variable=v4, value=4).grid(row=5, column=0,columnspan=2, padx=35, sticky="w")

button1=ttk.Button(f4, text='上一题', command=lambda:raise_frame(f3))
button1.place(x=120, y=600, anchor="center")
button2=ttk.Button(f4, text='下一题', command=lambda:raise_frame(f5))
button2.place(x=240, y=600, anchor="center")

#第5页
pf=ttk.Frame(f5)
pf.pack(pady=5)
logo5=PhotoImage(file="ln.png")
ttk.Label(pf,image=logo5).grid(row=0, column=0, columnspan=2)

tf=ttk.Frame(f5)
tf.pack(side=LEFT, anchor='nw')

label1=ttk.Label(tf, text='''5. "我们大家，立刻开始这段感情吧，\n至尊宝！"是露娜哪个皮肤的台词？''')
label1.grid(row=0, column=1, columnspan=2, padx=10)

label2=ttk.Label(tf)
label2.grid(row=1, column=0, columnspan=2)  #插入一空行

v5= IntVar()
ttk.Radiobutton(tf, text="至尊宝", variable=v5, value=1).grid(row=2, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="哥特玫瑰", variable=v5, value=2).grid(row=3, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="紫霞仙子", variable=v5, value=3).grid(row=4, column=0,columnspan=2, padx=35, sticky="w")
ttk.Radiobutton(tf, text="月光之女", variable=v5, value=4).grid(row=5, column=0,columnspan=2, padx=35, sticky="w")

button1=ttk.Button(f5, text='上一题', command=lambda:raise_frame(f4))
button1.place(x=120, y=600, anchor="center")
button2=ttk.Button(f5, text='提交答案', command=grade)
button2.place(x=240, y=600, anchor="center")

#收尾
raise_frame(f0)
root.mainloop()

