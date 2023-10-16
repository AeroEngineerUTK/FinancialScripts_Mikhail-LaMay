'''
Author: Mikhail LaMay

Desc: Script To Calculate Remaining Car Payment Information To Help Determine Best Course Of Action For Repayment

Important Variables/Definitions:
    Amortization Schedule:
        The schedule on which interest is paid off on a loan. Each month a portion is paid towards the loan principal as well as the interest.
    Annual Interest Rate (APR):
        This percentage represents the complete interest and fees that you will be expected to pay over the course of a year for the amount borrowed.
    loanAmount:
        The amount of money that you borrow from a lender in order to purchase your vehicle.
    loanTerm:
        This refers to the period of time that you will make repayments to your lender.
    principleBalance:
        The amount of money that you have borrowed to fund your vehicle that you have to pay back.

'''

# Define Libraries
import datetime
import numpy_financial as npf
import math

# Define Variables
dummyData_Active =  True
print(" ", end="\n")


# Function To Calculate Monthtly Loan Payment
def myMonPayment(loanAmount, APR, loanTerm):
    # Calculate Montly Payments
    monthlyPayment = ( (APR/12) * loanAmount * ((1 + (APR/12))**(loanTerm*12) ))/(( (1 + (APR/12))**(loanTerm*12)) - 1)

    return monthlyPayment

if dummyData_Active:
    loanTerm = (int(60))/12
    loanAmount = float(29000)
    APR = (float(6.39))/100
else:
    loanTerm = (int(input("What's Your Current Loan Term (M)? ")))/12
    loanAmount = float(input("What's Your Original Loan Amount ($)? "))
    APR = (float(input("What's Your Current (APR) Annual Interest Rate (%)? ")))/100

print("Monthly Payment: " + "$" + str(myMonPayment(loanAmount, APR, loanTerm)), end="\n\n")

#########################################################################################

# Function To Calculate Monthly Interest
def myMonInterest(loanAmount, APR):
    
    # Calcualte Monthly Interest
    monInterest = (loanAmount * APR) * (1/12)

    return monInterest

print("Monthly Interest: " + "$" + str(myMonInterest(loanAmount, APR)), end="\n\n")

#########################################################################################

# Function To Calculate Remaining Months Left On Loan
def remainLoanTime(PayoffDate):

    # Parse currentDate Information
    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')
    year1, month1, day1 = map(int, currentDate.split("-"))
    date1 = datetime.date(year1, month1, day1)

    # Parse desiredPayoffDate Information
    year2, month2, day2 = map(int, PayoffDate.split("-"))
    date2 = datetime.date(year2, month2, day2)

    # Calculate Remaining Payment Term
    remainingPayoffTerm = date2 - date1

    return remainingPayoffTerm

if dummyData_Active:
    PayoffDate = "2024-06-30"
else:
    PayoffDate = input("Enter Your Desired Payoff Date (YYYY-MM-DD format)? ")

print("Loan Time Remaining: " + str(remainLoanTime(PayoffDate)), end="\n\n")

#########################################################################################

# Function To Calculate Annual Payment Regarding Interest
annual_pay = npf.pmt(APR,loanTerm,-loanAmount)

# Ensure loanTerm IS "int", NOT "float" For Table Builder
rndloanTerm = math.floor(loanTerm)

# Print Table Header
print('{}{:>10}{:>10}{:>10}'.format('Year', 'Interest','Retired', 'Balance'))

# Generate Data For Table
for yr in range(1,rndloanTerm + 1):
    interest_to_pay = APR * loanAmount
    retired_prin = annual_pay - interest_to_pay
    loanAmount = loanAmount - retired_prin
    print('{:>4}{:>10.2f}{:>10.2f}{:>10.2f}'
          .format(yr, interest_to_pay, retired_prin, loanAmount))
    
#########################################################################################
