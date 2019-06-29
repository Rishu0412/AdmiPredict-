# AdmiPredict-
"AdmiPredict" - Admission Prediction

This Project will predict chances of Admission of a Graduate student in a particular university for Masters (MBA & MS). It will also help in shortlisting universities on the basis of their profiles (GRE Score, TOEFL Scores, Undergraduate CGPA, Research Experience, Statement of Purpose). It will help students and their parents in shortlisting universities for MS & MBA in the USA on the basis of their profiles. The predicted output gives them a fair idea about their chances of admission in a particular university. 

METHODOLOGY

[I] DATASET SELECTION
Firstly, we search for dataset from different sources (like – Kaggle.com, UCI Repository, Microsoft Azure Cloud, USA_analytics.com & more) and download 100’s of datasets. Then we check whether the give attributes in dataset are relevant for prediction or not, dataset is latest or not, topic and size of dataset is workable or not. After sorting dataset on these basis, we got some datasets. Finally, we check that all the data entries are not NULL. Then we modify datasets according to the needs of different Machine Learning Algorithms (like: - Logistic Regression, Linear Regression, Decision tree Regression, Random forest). We chose this dataset which contained Graduate Admissions Data, we further researched for its attributes.

[II] ALGORITHM COMPARISION
We searched for Machine Learning algorithms that can be used in this scenario. We found 4 algorithms which fits best for this scenario. 
(i)	Logistic Regression
(ii)	Linear Regression
(iii)	Random Forest
(iv)	Decision Tree

[III] ANALYSIS

DATASET
This dataset is created for prediction of post graduate admissions. 
Features in the dataset:
•	GRE Scores (290 to 340)
•	TOEFL Scores (92 to 120)
•	University Rating (1 to 5)
•	Statement of Purpose (1 to 5)
•	Undergraduate CGPA (6.8 to 9.92)
•	Research Experience (0 or 1)
•	Chance of Admission (0 or 1)

READING THE DATASET 

A FIRST LOOK AT THE DATASET
Basic Information about Dataset
Some important information:
•	There are 7 columns: GRE Score, TOEFL Score, University Rating, SOP, CGPA, Research, Chance of Admit
•	There are no null records. It's good.
•	There are 500 samples in total.
 
DATA VISUALISATION TO UNDERSTAND THE DATASET
1] Having Research or not:
•	The majority of the candidates in the dataset have research experience.
•	Therefore, the Research will be an unimportant feature for the Chance of Admit. The correlation between Chance of Admit and Research was already lower than other correlation values.

2] TOEFL Score:
•	The lowest TOEFL score is 92 and the highest TOEFL score is 120. The average is 107.41.

3] GRE Score:
•	This histogram shows the frequency for GRE scores.
•	There is a density between 310 and 330. Being above this range would be a good feature for a candidate to stand out.

4] CGPA Scores for University Ratings:
•	As the quality of the university increases, the CGPA score increases.
•	Candidates with high GRE scores usually have a high CGPA score.       
•	Candidates who graduate from good universities are more fortunate to be accepted.
•	Candidates with high CGPA scores usually have a high SOP score.      
•	Candidates with high GRE scores usually have a high SOP score.


[IV] ALGORITHM SELECTION

We made predictions using several Machine Learning Algorithms (like: - Logistic Regression, Linear Regression, Decision tree Regression, Random forest). Now, we need to select which one is best among these algorithms for this case. We use Confusion Matrix to find the accuracy of each algorithm. And then, we compared these accuracies and select the algorithm with highest accuracy. Logistic Regression has highest accuracy of 84% followed by Random Forest with 78% accuracy.

[V] PREDICTION

1] IMPORTING LIBRARIES

2] READING THE DATASET
•	The function returns a pandas.DataFrame that you can immediately start summarizing and plotting. 
•	This displays the shape(rows, columns) of the data:
 
3] SPLITTING OF DATA
 
4] TRAINING MODEL

[VI] GUI
We developed GUI using TKINTER as its easier to use. Initially, we made different GUI’s for PREDICTION and ANALYSIS just to make it easy to develop.We have used several tkinter features such as label, button,entry etc. Later on we improvised it by adding Logo,Background color and other features. 

1] GUI FOR PREDICTION
First we create Input window where end user will entry the Inputs (GRE Score, TOEFL Score, CGPA, Research, SOP Rating & University Rating) and click on “PREDICT” button to check his Chance of Admission.

2] GUI FOR ANALYSIS
We create interface with buttons (options) where end user can see the relation between the different variables through Visualization (like: Heatmap, Bar Chart etc).

3] FINAL GUI
Finally, we merged both GUI to create our final Interface. Now, end user need not to run both programs seperately just run this python file.

SOFTWARE

1] SPYDER:
An open source cross-platform integrated development environment (IDE) for scientific programming in the Python Language. Spyder integrates with a number of prominent packages in the scientific Python stack, including Numpy, Cython, Pandas, SymPy, Matplotlib, IPython, SciPy and more. Spyder is the abbreviation for scientific python development environment

PLATFORM

1] PYTHON:  
It is an interpreted, high – level, general – purpose programming language. It supports multiple programming paradigms, including procedural, object – oriented, and functional programming. Python also features a comprehensive standard library.

THE MOST WIDELY USED PYTHON LIBRARIES ARE:
•	NUMPY: - The most fundamental package, around which the scientific computation stack is built, is Numpy. It provides an abundance of useful features for operations on n-arrays and matrices in Python. NumPy is the abbreviation for Numerical Python.

•	PANDAS: - Pandas is a Python package designed to do work with “labelled” and “relational” data simple and intuitive. Pandas is a perfect tool for data wrangling. It designed for quick and easy data manipulation, aggregation, and visualization.
•	MATPLOTLIB: - It is a plotting library for the Python programming language and its numerical mathematics extension NumPy. There are also facilities for creating labels, grids, legends, and many other formatting entities with Matplotlib. 

•	SCIKIT – LEARN: -  Scikits are additional packages of SciPy Stack designed for specific functionalities like image processing and machine learning facilitation. The package is built on the top of SciPy and makes heavy use of its math operations.

•	TKINTER: - It is a Python binding to the Tk GUI toolkit. Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

•	SEABORN: - It is mostly focused on the visualization of statistical models; such visualizations include heat maps, those that summarize the data but still depict the overall distributions. Seaborn is based on Matplotlib and highly dependent on that.

•	SCIPY: - It is a library of software for engineering and science. It contains modules for linear algebra, optimization, integration, and statistics. The main functionality of SciPy library is built upon NumPy. It provides efficient numerical routines as numerical integration, optimisation, and many others via its specific submodules.


2] MACHINE LEARNING: 
Machine learning (ML) is a category of algorithm that allows software applications to become more accurate in predicting outcomes without being explicitly programmed. The basic premise of machine learning is to build algorithms that can receive input data and use statistical analysis to predict an output while updating outputs as new data becomes available.  

THE MOST WIDELY USED MACHINE LEARNING ALGORITHMS:

•	LOGISTIC REGRESSION: - It is a classification algorithm. It is used to predict a binary outcome (1 / 0, Yes / No, True / False) given a set of independent variables. It is a statistical analysis method used to predict a data value based on prior observations of a data set. A logistic regression model predicts a dependent data variable by analysing the relationship between one or more existing independent variables. It has become an important tool in the discipline of machine learning. The approach allows an algorithm being used in a machine learning application to classify incoming data based on historical data. It can also play a role in data preparation activities by allowing data sets to be put into specifically predefined buckets during the extract, transform, load (ETL) process in order to stage the information for analysis.

Logistic Regression Equation:
Y = exp(p0+p1X)/(1+exp(p0+p1X))


•	LINEAR REGRESSION: -  Linear regression is useful for finding relationship between two continuous variables. One is predictor or independent variable and other is response or dependent variable. It looks for statistical relationship but not deterministic relationship.

     Linear Regression Equation:
Y(X)=p0 +p1 *X1 +p2 *X2 +........+pn *Xn

•	DECISION TREE REGRESSION: - Decision trees are a simple, but powerful form of multiple variable analysis. They are produced by algorithms that identify various ways of splitting data into branch-like segments. Decision trees partition data into subsets based on categories of input variables, helping you to understand someone’s path of decisions.

•	RANDOM FOREST: - Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operates by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees. Random decision forests correct for decision trees habit of overfitting to their training set.


CONTRIBUTION:

This Project was built with the purpose of helping students and their parents in shortlisting universities with their profiles. The predicted output gives them a fair idea about their chances of Admission in a particular university.

REFERENCES:

We have taken help from following sources in planning this project:
1.	For dataset: https://www.kaggle.com/mohansacharya/graduate-admissions

2.	For GUI: https://www.tutorialspoint.com/python/python_gui_programming.htm          
             https://www.geeksforgeeks.org/python-gui-tkinter/ 

3.	For Error Solving: https://stackoverflow.com/questions/41653369/python-tkinter-event-argument-issue
