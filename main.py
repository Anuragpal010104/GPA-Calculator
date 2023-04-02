import numpy as np
import pandas as pd

branch = input("Enter your branch: cs,it,csb,csai: ")

if(branch == 'cs'):
    df = pd.read_excel('endsem.xlsx', sheet_name='cs')
    data = df['Marks']
    data = pd.to_numeric(data, errors='coerce')
    # print("mean:", np.mean(data))
    # print("standard deviation:", np.std(data))
    avg = np.mean(data)
    med = np.std(data)
    x=float(input("Enter your marks "))
    if(x>(avg + 1.5*med)):
        print("10 GPA")
    elif((avg + 1.5*med)>x>(avg + med)):
        print("9 GPA and above")
    elif((avg + med)>x>=(avg + med/2)):
        print("8 GPA and above")
    elif((avg + med/2)>x>=(avg)):
        print("7 GPA and above")
    elif((avg)>x>=(avg - med/2)):
        print("6 GPA and above")
    elif((avg - med/2)>x>=(avg-med)):
        print("5 GPA and above")
    elif((avg - med/2)>x>=(avg- med *1.5) ):
        print("4 GPA and above")
    else:
        print("BACK MUBARAK!!, PRABHU AAPKO SKHAKTI DE")

elif(branch == 'it'):
    df = pd.read_excel('endsem.xlsx', sheet_name='it')
    data = df['Marks']
    data = pd.to_numeric(data, errors='coerce')
    # print("mean:", np.mean(data))
    # print("standard deviation:", np.std(data))
    avg = np.mean(data)
    med = np.std(data)
    x=float(input("Enter your marks "))
    if(x>(avg + 1.5*med)):
        print("10 GPA")
    elif((avg + 1.5*med)>x>(avg + med)):
        print("9 GPA and above")
    elif((avg + med)>x>=(avg + med/2)):
        print("8 GPA and above")
    elif((avg + med/2)>x>=(avg)):
        print("7 GPA and above")
    elif((avg)>x>=(avg - med/2)):
        print("6 GPA and above")
    elif((avg - med/2)>x>=(avg-med)):
        print("5 GPA and above")
    elif((avg - med/2)>x>=(avg- med *1.5) ):
        print("4 GPA and above")
    else:
        print("BACK MUBARAK!!, PRABHU AAPKO SKHAKTI DE")

elif(branch == 'csb'):
    df = pd.read_excel('endsem.xlsx', sheet_name='csb')
    data = df['Marks']
    data = pd.to_numeric(data, errors='coerce')
    # print("mean:", np.mean(data))
    # print("standard deviation:", np.std(data))
    avg = np.mean(data)
    med = np.std(data)
    x=float(input("Enter your marks "))
    if(x>(avg + 1.5*med)):
        print("10 GPA")
    elif((avg + 1.5*med)>x>(avg + med)):
        print("9 GPA and above")
    elif((avg + med)>x>=(avg + med/2)):
        print("8 GPA and above")
    elif((avg + med/2)>x>=(avg)):
        print("7 GPA and above")
    elif((avg)>x>=(avg - med/2)):
        print("6 GPA and above")
    elif((avg - med/2)>x>=(avg-med)):
        print("5 GPA and above")
    elif((avg - med/2)>x>=(avg- med *1.5) ):
        print("4 GPA and above")
    else:
        print("BACK MUBARAK!!, PRABHU AAPKO SKHAKTI DE")

elif(branch == 'csai'):
    df = pd.read_excel('endsem.xlsx', sheet_name='csai')
    data = df['Marks']
    data = pd.to_numeric(data, errors='coerce')
    # print("mean:", np.mean(data))
    # print("standard deviation:", np.std(data))
    avg = np.mean(data)
    med = np.std(data)
    x=float(input("Enter your marks "))
    if(x>(avg + 1.5*med)):
        print("10 GPA")
    elif((avg + 1.5*med)>x>(avg + med)):
        print("9 GPA and above")
    elif((avg + med)>x>=(avg + med/2)):
        print("8 GPA and above")
    elif((avg + med/2)>x>=(avg)):
        print("7 GPA and above")
    elif((avg)>x>=(avg - med/2)):
        print("6 GPA and above")
    elif((avg - med/2)>x>=(avg-med)):
        print("5 GPA and above")
    elif((avg - med/2)>x>=(avg- med *1.5) ):
        print("4 GPA and above")
    else:
        print("BACK MUBARAK!!, PRABHU AAPKO SKHAKTI DE")

else:
    print("Please enter your branch correctly")