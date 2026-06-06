# Overview

{With this program i tried to learn to build an application where I analize a csv file with Utah mortgage information from 2022. I used Pandas and Python to query the dataset and gather information to answer two questions}

{https://www.kaggle.com/datasets/richcordova/utah-hmda-data-2018-2022?resource=download this is information of mortgage data in utah. I used the 2022 file it includes loan acceptance for age groups and income groups.}

{The number one purpose was to learn to use Python with Pandas and to use methods and functions to filter and add data.}

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video]https://youtu.be/r1kviPz2vrk

# Data Analysis Results

{Question 1:
    Which applicant age groups have the highest average loan amounts?
    
Question 2:
    How do approved and denied mortgage applications compare?
        
    QUESTION 1
============================================================
               average_loan_amount  ...  number_of_applications
applicant_age                       ...                        
25-34                795780.471273  ...                   50162
8888                 636708.522951  ...                   17799
>74                  464835.954676  ...                    5913
35-44                334383.278495  ...                   59265
45-54                331472.639113  ...                   43310
55-64                327626.512342  ...                   26697
<25                  297463.917526  ...                    8730
65-74                281892.852353  ...                   14914

[8 rows x 3 columns]

The applicant age group with the highest average loan amount is 25-34, with an average loan amount of $795,780.47.

============================================================
QUESTION 2
============================================================
      Application Status  ...  Number of Applications
0  Approved / Originated  ...                  132611
1                 Denied  ...                   29059.}

# Development Environment

{I used Pandas which is a Python Library for working with and analyzing data}

{Python and Pandas.}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* YOUTUBE https://www.youtube.com/watch?v=EXIgjIBu4EU
* Kaggle https://www.kaggle.com/datasets/richcordova/utah-hmda-data-2018-2022?resource=download
* https://pandas.pydata.org/docs/user_guide/10min.html#min

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* I can add more ways to analyze the data 
* I can generate more questions and find answers to those questions