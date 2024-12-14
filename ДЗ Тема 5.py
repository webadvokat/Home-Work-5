# %%
from datetime import datetime

# %%
The_Moscow_Times_date = "Wednesday, October 2, 2002"
The_Guardian_date = "Friday, 11.10.13"
Daily_News_date = "Thursday, 18 August 1977"

#Преобразование datetime
The_Moscow_Times_dt = datetime.strptime(The_Moscow_Times_date, "%A, %B %d, %Y")
The_Guardian_dt = datetime.strptime(The_Guardian_date, "%A, %d.%m.%y")
Daily_News_dt = datetime.strptime(Daily_News_date, "%A, %d %B %Y")

print("The Moscow Times:", The_Moscow_Times_dt)
print("The Guardian:", The_Guardian_dt)
print("Daily News:", Daily_News_dt)


# %%



