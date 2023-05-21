from datetime import datetime


users = [ 
        {"Oleksandr": datetime(day=29, month=5, year=2001)},
        {"Alex": datetime(day=17, month=5, year=2002)},
        {"Kate": datetime(day=18, month=2, year=2003)},
        {"Bill": datetime(day=21, month=5, year=2004)},
        {"Jill": datetime(day=22, month=5, year=2005)},
        {"Kim": datetime(day=19, month=5, year=2006)},
        {"Jan": datetime(day=19, month=5, year=2007)},
        {"Tom": datetime(day=18, month=5, year=1990)}
]


def get_birthdays_per_week(users):

    Monday_lst = []
    Tuesday_lst = []
    Wednesday_lst = []
    Thursday_lst = []
    Friday_lst = []

    for dict_dirthday in users:
        for name, birthday in dict_dirthday.items():
            
            date_now = datetime(day=18, month=5, year=2023).date()
            # date_now = datetime.now().date()

            birthday = birthday.replace(year=date_now.year)

            if birthday.day >= date_now.day and birthday.day <= date_now.day + 6 and birthday.month == date_now.month:

                if birthday.weekday() in [5, 6, 0]:
                    Monday_lst.append(name)
                elif birthday.weekday() == 1:
                    Tuesday_lst.append(name)
                elif birthday.weekday() == 2:
                    Wednesday_lst.append(name)
                elif birthday.weekday() == 3:
                    Thursday_lst.append(name)
                elif birthday.weekday() == 4:
                    Friday_lst.append(name)

    if len(Monday_lst) != 0:
        Monday_str = ", ".join(Monday_lst)
        print(f"Monday: {Monday_str}")
    if len(Tuesday_lst) != 0:
        Tuesday_str = ", ".join(Tuesday_lst)
        print(f"Tuesday: {Tuesday_str}")
    if len(Wednesday_lst) != 0:
        Wednesday_str = ", ".join(Wednesday_lst)
        print(f"Wednesday: {Wednesday_str}")
    if len(Thursday_lst) != 0:
        Thursday_str = ", ".join(Thursday_lst)
        print(f"Thursday: {Thursday_str}")
    if len(Friday_lst) != 0:
        Friday_str = ", ".join(Friday_lst)
        print(f"Friday: {Friday_str}")
    

get_birthdays_per_week(users)