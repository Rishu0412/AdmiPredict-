import pandas as pd  # for Dataset
import matplotlib.pyplot as plt # for visualization
import tkinter as tk # for GUI
from tkinter import *
import numpy as np
master = tk.Tk()
master.title("Input Window") # Title of window
master.iconbitmap('iconfinder_Analytics.ico') # Window Logo
width = master.winfo_screenwidth()
height = master.winfo_screenheight()
master.minsize(width, height) 
master.resizable(width = False, height = False)  # to fix size of window 
              
df = pd.read_csv('Admission Prediction 11.csv') # path of CSV file
#a = df.head(n=15)

"""
Spliting of Data to Train in Logistic Regression
"""

X = df[['GRE Score','TOEFL Score','University Rating','SOP','CGPA','Research']]
y = df['Chance of Admission']

#from sklearn import *
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 101)  #training method
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
lm = LogisticRegression() # Import LogisticRegression
lm.fit(X_train,y_train) # Syntax to fit the our data in LogisticRegression

''' PREDICTION '''

def predict() :
    g = float(gre.get())
    t = float(toefl.get())
    u = float(ur.get())
    s = float(sop.get())
    c = float(cgpa.get())
    r = float(rs.get())
    
    if (g>260 and t>70 and c>6.9):
       prediction = lm.predict(X_test)
       prediction1 = lm.predict([[g,t,u,s,c,r]])
       print("accuracy : {} ".format(accuracy_score(y_test,prediction)*100))
       
       if (prediction1 == 1):
           prd = "YES "
           p= tk.Label(master, text="Chance of Admission :" + str(prd),width=25,height = 4,bg="GREEN",fg = "BLACK",font = "Candara").grid(row=8, column=0)
           
       elif(prediction1 == 0):
           prd = "NO"
           p= tk.Label(master, text="Chance of Admission :" + str(prd),width=25,height = 4,bg="RED",fg = "BLACK",font = "Candara").grid(row=8, column=0)
           
       else:
           prd = '\0'
        
      

       plt.xlabel('Y Test')
       plt.ylabel('Predicted Y')
       
    else:
       p= tk.Label(master, text="The candidate is not eligible.",width=25,height = 4, bg = "YELLOW",fg = "BLACK",font = "Candara").grid(row=8, column=0)

       
gre=tk.StringVar()
toefl=tk.StringVar()
ur=tk.StringVar()
sop=tk.StringVar()
cgpa=tk.StringVar()
rs=tk.StringVar()

l1= tk.Label(master, text="GRE Score",width=22,height = 3,fg = "BLACK",font = "Candara").grid(row=0,column=1)
l2= tk.Label(master, text="TOEFL Score",width=22,height = 3,fg = "BLACK",font = "Candara").grid(row=1,column=1)
l3= tk.Label(master, text="years of experience",width=22,height = 3,fg = "BLACK",font = "Candara").grid(row=2,column=1)
l4= tk.Label(master, text="SOP Rating",width=22,height = 3,fg = "BLACK",font = "Candara").grid(row=3,column=1)
l5= tk.Label(master, text="CGPA",width=22,height = 3,fg = "BLACK",font = "Candara").grid(row=4,column=1)
l6= tk.Label(master, text="Research",width=22,height = 3,fg = "BLACK",font = "Candara").grid(row=5,column=1)

e1 = tk.Entry(master, textvariable = gre,width=27).grid(row=0, column=2)
e2 = tk.Entry(master, textvariable = toefl,width=27).grid(row=1, column=2)
e3 = tk.Entry(master, textvariable = ur,width=27).grid(row=2, column=2)
e4 = tk.Entry(master, textvariable = sop,width=27).grid(row=3, column=2)
e5 = tk.Entry(master, textvariable = cgpa,width=27).grid(row=4, column=2)
e6 = tk.Entry(master, textvariable = rs,width=27).grid(row=5, column=2)

def analysis():
    
    root = Tk()
    root.configure(background = "#1A5276") # Background color          
    root.title("ANALYSIS OF DATASET") # Title of window
    root.iconbitmap('iconfinder_Graph-Magnifier.ico') # Window Logo

    def Img():
    
        
        plt.plot(df)
        plt.show()
        
    
    def Img1():
    
        

        plt.hist(df['Chance of Admission'],color="#000000")
        label=['Not having Experience','Having Experience']
        index = np.arange(len(label))
        plt.xticks(index, label, fontsize=10)
        plt.show()
        
    def Img2():
    
       
        plt.hist(df['TOEFL Score'],color="#000000")
        label=['Worst','Average','Best']
        index = np.arange(len(label))
        plt.xticks(index,label,  fontsize=10)
        plt.show()
        
    def Img3():
    
        
        plt.hist(df['GRE Score'],color="#000000")
       
        plt.xticks(range(100,200))
       
        plt.show()
       

    def Img4():
    
       
        plt.hist(df['University Rating'],color="#000000")
        plt.xticks(range(0,9))
        plt.yticks(range(0,8))
        plt.xlabel("CGPA")
        plt.ylabel("University Rating")
        plt.show()
        
    def Img5():
    
        
        N = 500
        colors = (0,0,0)
        area = np.pi*3
        x=df['GRE Score']
        y=df['CGPA']
       
        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        plt.title('CGPA For GRE Scores')
        plt.xlabel('GRE')
        plt.ylabel('CGPA')
        plt.show()
       

    def Img6():
        
        
        plt.hist(df['University Rating'],color="#000000")
        plt.xlabel("University Rating")
        plt.ylabel("Candidates")
        plt.title("University Rating Of Candidates with an 75% acceptance chance")
        plt.show()
    def Img7():
        N = 500
        colors = (0,0,0)
        area = np.pi*3
        x=df['CGPA']
        y=df['SOP']
       
        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        plt.title('SOP For CGPA Scores')
        plt.xlabel('CGPA')
        plt.ylabel('SOP')
        plt.show()
    def Img8():
        N = 500
        colors = (0,0,0)
        area = np.pi*3
        x=df['GRE Score']
        y=df['SOP']
       
        plt.scatter(x, y, s=area, c=colors, alpha=0.5)
        plt.title('SOP For GRE Scores')
        plt.xlabel('GRE')
        plt.ylabel('SOP')
        plt.show()
        
    btn = Button(root, text = "Correlation Between All Columns",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000", command = Img)
    btn.grid(row = 0, column = 0)
    
    btn1 = Button(root, text = "Research Experience Analysis",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000", command = Img1)
    btn1.grid(row = 0, column = 1)

    btn2 = Button(root, text = "TOEFL Score Analysis",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000", command = Img2)
    btn2.grid(row = 0, column = 2)

    btn3 = Button(root, text = "GRE Score Analysis", width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000",command = Img3)
    btn3.grid(row = 1, column = 0)

    btn4 = Button(root, text = "CGPA Score Analysis_1",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000", command = Img4)
    btn4.grid(row = 1, column = 1)

    btn5 = Button(root, text = "CGPA Score Analysis_2",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000", command = Img5)
    btn5.grid(row = 1, column = 2)

    btn6 = Button(root, text = "University Rating Analysis",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000", command = Img6)
    btn6.grid(row = 2, column = 0)

    btn7 = Button(root, text = "SOP vs CGPA",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000", command = Img7)
    btn7.grid(row = 2, column = 1)

    btn8 = Button(root, text = "SOP vs GRE Score",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000", command = Img8)
    btn8.grid(row = 2, column = 2)

    root.mainloop()

    
btn = tk.Button(master, text = '', width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE").grid(row = 7, column = 0)
btn = tk.Button(master, text = 'Predict', width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000" , command = predict).grid(row = 7, column = 1)
btn1 = tk.Button(master, text = 'Analyse', width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#000000" , command = analysis).grid(row = 7, column = 2)

master.mainloop()
