#A person wants to calculate their monthly income, expenses, savings, yearly savings, and savings percentage.

print("===== PERSONAL FINANCE REPORT =====")

#information of the empolyee

a=input("enter the name of empolyee:")
b=int(input("enter the age of empolyee:"))
c=input("enter the city name of person:")


#calculate montly income
salary=int(input("\nenter the salry of the person:"))
freenclacing=int(input("enter the freelacing earning:"))
otherincome=int(input("enter the other income of the empolyee:"))

montly_income=salary+freenclacing+otherincome


#montly expences
rent=int(input("\nrent :"))
electricity_bill=int(input("enter the electricity bill:"))
gas_bill=int(input("enter the gas bill:"))
transport=int(input("enter the transport bill:"))
houseitembill=int(input("grocery bill:"))
iternet=int(input("internet bill:"))
shopping_bill=int(input("enter the shopping bill:"))
other_bill=int(input("extra money spending:"))

montly_expences=rent+electricity_bill+gas_bill+transport+houseitembill+iternet+shopping_bill+other_bill


#montly saving
montly_saving=montly_income-montly_expences


#calculate yearly income
yearly_income=montly_income*12



#calculate yearly expences
yearly_expences=yearly_income*12


#calculate yearly saving
yearly_saving=montly_saving*12



#saving percentage
saving_percentage=yearly_saving*100/yearly_income


#average daily expences
daily_expences=montly_expences/30



#print all things
print("\n===== PERSONAL FINANCE REPORT =====")
print(f'NAME :{a}')
print(f'Age:{b}')
print(f'city:{c}')


print(f'\nthe montly income :{montly_income}')
print(f'the montly expences:{montly_expences}')
print(f'the montly  saving:{montly_saving}')


print(f'\nyearly income:{yearly_income}')
print(f'yearly expences:{yearly_expences}')
print(f'yearly saving:{yearly_saving}')

print(f'\nsaving percentage:{saving_percentage}')
print(f'daily expences:{daily_expences}')