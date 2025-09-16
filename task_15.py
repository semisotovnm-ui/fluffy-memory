print('Введите номер месяца и год')
month=int(input())
year=int(input())
if year < 1000 or year > 9999:
    print('выбери другой год')
else:   
    days31=[1,3,5,7,8,10,12]
    days30=[4,6,9,11]
    if month in days31:
        print(31)
    elif month in days30:
        print(30)
    else:
        if (year%4==0 or year%400==0) and year%100!=0:
            print(29)

        else:
            print(28)