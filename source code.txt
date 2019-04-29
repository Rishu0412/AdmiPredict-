import pandas as pd  # for Dataset
import matplotlib.pyplot as plt # for visualization
import seaborn as sns # for visualization
import tkinter as tk # for GUI
from tkinter import *

master = tk.Tk()
master.title("Input Window") # Title of window
master.configure(background = "#1A5276") # Background color
master.iconbitmap('iconfinder_Analytics.ico') # Window Logo
master.resizable(width = False, height = False)  # to fix size of window 
              
df = pd.read_csv('Admission Prediction 11.csv') # path of CSV file
a = df.head(n=15)

"""
Spliting of Data to Train in Logistic Regression
"""

X = df[['GRE Score','TOEFL Score','University Rating','SOP','CGPA','Research']]
y = df['Chance of Admission']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 101)  #training method
# Test_size will give '20%' of data to test file.

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
       #l= tk.Label(master, text="Chance of Admission :",width=25,height = 4,bg = "#1A5276",fg = "WHITE",font = "Candara").grid(row=8)
   
       if (prediction1 == 1):
           prd = "YES"
           
       elif(prediction1 == 0):
           prd = "NO"
           
       else:
           prd = '\0'
        
       p= tk.Label(master, text="Chance of Admission :" + str(prd),width=25,height = 4,bg = "#1A5276",fg = "WHITE",font = "Candara").grid(row=8, column=0)

       plt.xlabel('Y Test')
       plt.ylabel('Predicted Y')
       
    else:
       p= tk.Label(master, text="The candidate is not eligible.",width=25,height = 4, bg = "#1A5276",fg = "WHITE",font = "Candara").grid(row=8, column=0)

       
gre=tk.StringVar()
toefl=tk.StringVar()
ur=tk.StringVar()
sop=tk.StringVar()
cgpa=tk.StringVar()
rs=tk.StringVar()

l1= tk.Label(master, text="GRE Score",width=22,height = 3,bg = "#1A5276" ,fg = "WHITE",font = "Candara").grid(row=0)
l2= tk.Label(master, text="TOEFL Score",width=22,height = 3,bg = "#1A5276",fg = "WHITE",font = "Candara").grid(row=1)
l3= tk.Label(master, text="University Rating",width=22,height = 3,bg = "#1A5276",fg = "WHITE",font = "Candara").grid(row=2)
l4= tk.Label(master, text="SOP Rating",width=22,height = 3,bg = "#1A5276",fg = "WHITE",font = "Candara").grid(row=3)
l5= tk.Label(master, text="CGPA",width=22,height = 3,bg = "#1A5276",fg = "WHITE",font = "Candara").grid(row=4)
l6= tk.Label(master, text="Research",width=22,height = 3,bg = "#1A5276",fg = "WHITE",font = "Candara").grid(row=5)

e1 = tk.Entry(master, textvariable = gre,width=27).grid(row=0, column=1)
e2 = tk.Entry(master, textvariable = toefl,width=27).grid(row=1, column=1)
e3 = tk.Entry(master, textvariable = ur,width=27).grid(row=2, column=1)
e4 = tk.Entry(master, textvariable = sop,width=27).grid(row=3, column=1)
e5 = tk.Entry(master, textvariable = cgpa,width=27).grid(row=4, column=1)
e6 = tk.Entry(master, textvariable = rs,width=27).grid(row=5, column=1)

def analysis():
    
    root = Tk()
    root.configure(background = "#1A5276") # Background color          
    root.title("ANALYSIS OF DATASET") # Title of window
    root.iconbitmap('iconfinder_Graph-Magnifier.ico') # Window Logo

    def Img():
    
        r = Toplevel()
        r.configure(background = "#1A5276")
        r.title("HEATMAP")
     
        text = Label(r, text="THE BELOW GIVEN HEATMAP WILL TELL US ABOUT CORRELATION BETWEEN ALL COLUMNS:-\n\n• The 3 most important features for Admission: CGPA, GRE & TOEFL SCORE.\n• The 3 least important features for Admission: Research and SOP.",bg = "#1A5276" ,fg = "WHITE",font = "Candara")
        text.pack()

        canvas = Canvas(r, height=680, width=680)
        canvas.pack()
        my_image = PhotoImage(file='Figure_0.png', master= master)
        canvas.create_image(0, 0, anchor=NW, image=my_image)
        r.mainloop()
    
    def Img1():
    
        r1 = Toplevel()
        r1.configure(background = "#1A5276")
        r1.title("Research Experience Analysis") 
    
        text1 = Label(r1, text = 'Having Research or not:\n\n•  The majority of the candidates in the dataset have research experience.\n•  Therefore, the Research will be an unimportant feature for the Chance of Admission.\n',bg = "#1A5276" ,fg = "WHITE",font = "Candara")
        text1.pack()

        canvas1 = Canvas(r1, height=480, width=625)
        canvas1.pack()
        my_image1 = PhotoImage(file='Figure_1.png', master= master)
        canvas1.create_image(0, 0, anchor=NW, image=my_image1)
        r1.mainloop()

    def Img2():
    
        r2 = Toplevel()
        r2.configure(background = "#1A5276")
        r2.title("TOEFL Score Analysis")
    
    
        text2 = Label(r2, text = 'TOEFL Score:\n\n • The lowest TOEFL score is 92 and the highest Toefl score is 120. The average is 107.41.\n',bg = "#1A5276" ,fg = "WHITE",font = "Candara")
        text2.pack()

        canvas2 = Canvas(r2, height=480, width=630)
        canvas2.pack()
        my_image2 = PhotoImage(file='Figure_2.png', master = master)
        canvas2.create_image(0, 0, anchor=NW, image=my_image2)
        r2.mainloop()    

    def Img3():
    
        r3 = Toplevel()
        r3.configure(background = "#1A5276")
        r3.title("GRE Score Analysis")
    
    
        text3 = Label(r3, text = 'GRE Score:\n\n • This histogram shows the frequency for GRE scores.\n• There is a density between 310 and 330. Being above this range would be a good feature for a candidate to stand out.\n',bg = "#1A5276" ,fg = "WHITE",font = "Candara")
        text3.pack()

        canvas3 = Canvas(r3, height=600, width=630)
        canvas3.pack()
        my_image3 = PhotoImage(file='Figure_3.png', master = master)
        canvas3.create_image(0, 0, anchor=NW, image=my_image3)
        r3.mainloop()    

    def Img4():
    
        r4 = Toplevel()
        r4.configure(background = "#1A5276")
        r4.title("CGPA Score Analysis_1")
    
    
        text4 = Label(r4, text = 'CGPA Scores for University Ratings:\n\n• As the quality of the university increases, the CGPA score increases.\n',bg = "#1A5276" ,fg = "WHITE",font = "Candara")
        text4.pack()

        canvas4 = Canvas(r4, height=480, width=600)
        canvas4.pack()
        my_image4 = PhotoImage(file='Figure_4.png', master = master)
        canvas4.create_image(0, 0, anchor=NW, image=my_image4)
        r4.mainloop()    
    
    def Img5():
    
        r5 = Toplevel()
        r5.configure(background = "#1A5276")
        r5.title("CGPA Score Analysis_2")
    
    
        text5 = Label(r5, text = '• Candidates with high GRE scores usually have a high CGPA score.\n',bg = "#1A5276" ,fg = "WHITE",font = "Candara")
        text5.pack()

        canvas5 = Canvas(r5, height=450, width=575)
        canvas5.pack()
        my_image5 = PhotoImage(file='Figure_5.png', master = master)
        canvas5.create_image(0, 0, anchor=NW, image=my_image5)
        r5.mainloop()    

    def Img6():
    
        r6 = Toplevel()
        r6.configure(background = "#1A5276")
        r6.title("University Rating Analysis")
    
        text6 = Label(r6, text = '• Candidates who graduate from good universities are more fortunate to be accepted.\n',bg = "#1A5276" ,fg = "WHITE",font = "Candara")
        text6.pack()

        canvas6 = Canvas(r6, height=450, width=980)
        canvas6.pack()
        my_image6 = PhotoImage(file='Figure_7.png', master = master)
        canvas6.create_image(0, 0, anchor=NW, image=my_image6)
        r6.mainloop()   
    
    def Img7():
    
        r7 = Toplevel()
        r7.configure(background = "#1A5276")
        r7.title("SOP vs CGPA")
    
        text7 = Label(r7, text = '• Candidates with high CGPA scores usually have a high SOP score.\n',bg = "#1A5276" ,fg = "WHITE",font = "Candara")
        text7.pack()

        canvas7 = Canvas(r7, height=480, width=600)
        canvas7.pack()
        my_image7 = PhotoImage(file='Figure_8.png', master = master)
        canvas7.create_image(0, 0, anchor=NW, image=my_image7)
        r7.mainloop()    

    def Img8():
    
        r8 = Toplevel()
        r8.configure(background = "#1A5276") 
        r8.title("SOP vs GRE Score")
                     
        text8 = Label(r8, text = '• Candidates with high CGPA scores usually have a high SOP score.\n',bg = "#1A5276" ,fg = "WHITE",font = "Candara")
        text8.pack()
    
        canvas8 = Canvas(r8, height=480, width=600)
        canvas8.pack()
        my_image8 = PhotoImage(file='Figure_9.png', master = master)
        canvas8.create_image(0, 0, anchor=NW, image=my_image8)
        r8.mainloop()    

        
    btn = Button(root, text = "Correlation Between All Columns",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B", command = Img)
    btn.grid(row = 0, column = 0)
    
    btn1 = Button(root, text = "Research Experience Analysis",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B", command = Img1)
    btn1.grid(row = 1, column = 1)

    btn2 = Button(root, text = "TOEFL Score Analysis",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B", command = Img2)
    btn2.grid(row = 2, column = 0)

    btn3 = Button(root, text = "GRE Score Analysis", width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B",command = Img3)
    btn3.grid(row = 3, column = 1)

    btn4 = Button(root, text = "CGPA Score Analysis_1",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B", command = Img4)
    btn4.grid(row = 4, column = 0)

    btn5 = Button(root, text = "CGPA Score Analysis_2",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B", command = Img5)
    btn5.grid(row = 5, column = 1)

    btn6 = Button(root, text = "University Rating Analysis",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B", command = Img6)
    btn6.grid(row = 6, column = 0)

    btn7 = Button(root, text = "SOP vs CGPA",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B", command = Img7)
    btn7.grid(row = 7, column = 1)

    btn8 = Button(root, text = "SOP vs GRE Score",width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B", command = Img8)
    btn8.grid(row = 8, column = 0)

    root.mainloop()

    

btn = tk.Button(master, text = 'Predict', width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B" , command = predict).grid(row = 6, column = 1)
btn1 = tk.Button(master, text = 'Analyse', width=32,height = 3,font = "Copperplate_Gothic", fg = "WHITE",bg = "#C0392B" , command = analysis).grid(row = 6, column = 0)

master.mainloop()
