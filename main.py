import re  # regular expressions
from datetime import datetime



def main():
    global day_intext, month_intext, year_intext, date_intext,date_intext_str,year,month,day,out,hour,minute\
        ,find_delayed_hour,find_delayed_minute,find_delayed_year, find_delayed_month,find_delayed_day,day_week,n,\
        string_month,day_for_string_month,string_year, sum_minutes,sum_hours,sum_days,sum_months,sum_years, counter

    string_month=''
    day_for_string_month=''
    string_year=''
    day_week=''
    receive = input('Введите событие:')
    all_objects = receive.split()  # деление на подсторки
    print(all_objects)
                                                                                                                        #словари------------------------------------------------------------------------------------------------------------
    Mondays=['в понедельник','каждый понедельник' , 'понедельник' ,'Понедельник' , 'по понедельникам' ,'понедельник']
    Tuesdays=['во вторник' , 'каждый вторник' , 'вторник' , 'Вторник' , 'по вторникам']
    Wendsdays=['в среду' , 'каждую среду' , 'среда' , 'Среда' , 'по средам' , 'среду']
    Thursdays=['в четверг' , 'каждый четверг' , 'четверг' , 'Четверг' , 'по четвергам']
    Fridays=['в пятницу' , 'каждую пятницу' , 'пятница' , 'Пятница' , 'по пятницам']
    Saturdays=['в субботу' , 'каждую субботу' , 'суббота' , 'Суббота' , 'по субботам']
    Sundays=['в воскресенье' , 'каждое воскресенье' , 'воскресенье' , 'Воскресенье' , 'по воскресеньям']
    WEEK=[Mondays,Tuesdays,Wendsdays,Thursdays,Fridays,Saturdays,Sundays]

    Septembers=['сентябрь' , 'сентября']
    Octobers=['октябрь' , 'октября']
    Novembers=['ноябрь' , 'ноября']
    Decembers=['декабрь' , 'декабря']
    Januarys=['январь' , 'января']
    Februarys=['февраль' , 'февраля']
    Marchs=['март' , 'марта']
    Aprils=['апрель' , 'апреля']
    Mays=['май' , 'мая']
    Junes=['июнь' , 'июня']
    Julys=['июль' , 'июля']
    Augusts=['август' , 'августа']
    MONTHS=[Septembers,Octobers,Novembers,Decembers,Januarys,Februarys,Marchs,Aprils,Mays,Junes,Julys,Augusts]

    minutes_for_dalay=['минуту' , 'минуты','минут']
    hours_for_delay=[ 'час' , 'часа' ,'часов']
    days_for_dalay=['дня','день','дней']
    months_for_delay=['месяц','месяца','месяцев']
    years_for_delay=['год','года','лет']

    cherez=['Через','через']
    every=['каждый','каждый','каждое','каждое','Каждый','Каждое','каждую','каждые','Каждую','Каждые']


    Mornings=['утро','утром','Утром']
    Afternoon=['день','днем','днём','Днем','Днём']
    Evening=['вечер','вечером','Вечером']
    Night=['ночь','ночью','Ночью']
                                                                                                                        #-------------------------------------------------------------------------------------------------------------------



    current_date = datetime.now()                                                                                       #текущие: month day year hour minute                                    обработка лет месяцев дней
    current_date_string = current_date.strftime('%m/%d/%y %H:%M:%S')                                                    #hour и minute далее
    print("Текущие значения:",current_date_string)
    month_current=current_date_string[1]
    day_current = current_date_string[3:5]
    year_current=current_date_string[6:8]


    try:
        match = re.search(r'\d{2}.\d{2}.\d{4}', receive)                                                                # находим день месяц год из сообщения  в формате даты
        date_intext = datetime.strptime(match.group(), '%d.%m.%Y').date()
    except  (AttributeError,ValueError):
        print('Нет даты в формате dd.mm.yyyy или ошибка ввода даты')
        year=int(year_current)+2000
        month=int(month_current)
        day=int(day_current)
    else:
        date_intext_str=str(date_intext)
        print ("Значения из сообщения:",date_intext_str)
        year_intext=date_intext_str[:4]
        month_intext=date_intext_str[5:7]
        day_intext=date_intext_str[8:10]
        year=int(year_intext)
        month=int(month_intext)
        day=int(day_intext)
        print(year_intext)
        print(month_intext)
        print(day_intext)

    #if 'в' in all_objects:
    #    print(all_objects.index('в'))
    #    for _ in range (2):
    #        all_objects.pop(all_objects.index('в'))
    #    receive=' '.join(all_objects)
                                                                                                                        #обработка часов и минут
    hour_current = int(current_date_string[9:11])
    minute_current = int(current_date_string[12:14])
    try:
        Time = re.findall(r'[0-2]\d:[0-5]\d+', receive)                                                                     #поиск времени в формате dd:dd
        Time_str=Time[0]
        hour_intext = int(Time_str[:2:])
        minute_intext = int(Time_str[3:5:])
        if hour_intext>24 or minute_intext>60:
            raise ValueError
    except (IndexError,ValueError):
        hour = int(current_date_string[9:11])
        minute= int(current_date_string[12:14])
    else:
        if Time:
            if hour_intext < hour_current:
                day = day + 1
                hour = hour_intext
                minute=minute_intext
            elif hour_intext == hour_current:
                hour = hour_intext
                if minute_intext < minute_current:
                    day = day + 1
                    minute = minute_intext
                elif minute_intext > minute_current:
                    minute=minute_intext
                elif minute_intext == minute_current:
                    minute=minute_intext
            else:                                                                                                               # иначе см 15 строка
                hour=hour_intext
                minute=minute_intext
        else:
            hour = int(current_date_string[9:11])
            minute = int(current_date_string[12:14])


    for h in  range (len(all_objects)):
        if all_objects[h]=='каждое' and all_objects[h+1].isdigit() and all_objects[h+2]=='число' :
            print(day)
            if int(all_objects[h+1])<day:
                day = int(all_objects[h + 1])
                month+=1
            else:
                day = int(all_objects[h + 1])
                for i in range(3):
                    del all_objects[h]

            receive=' '.join(all_objects)
            status='Success'
            print("Message:{", "'STATUS':", status, ",", "'PARAMS': {'repeat_always:'", day,'число', "}", "'DATE':{'year':",
                  year, ",", "'month':", month, ",", "'day':", day, ",", "'hour':", hour, ",", "'minute':", minute,
                  "}", ",", "'TEXT':", receive, "}", sep='')
            exit()

    for q in range (len(all_objects)):
        if all_objects[q] in Mornings:
            print(q)
            hour=str(hour)
            hour='06'
            minute=str(minute)
            minute='00'
            all_objects.pop(all_objects.index(all_objects[q]))
            receive=' '.join(all_objects)
    print(receive)

    day_week_current=datetime.isoweekday(datetime.now())
    day_week_compare=0
    print(day_week_current)


    for j in range (len(all_objects)):
        if all_objects[j] in Mondays:
            day_week='Monday'
            day_week_compare=1
        elif all_objects[j] in Tuesdays:
            day_week='Tuesday'
            day_week_compare=2
        elif all_objects[j] in Wendsdays:
            day_week='Wendsday'
            day_week_compare=3
        elif all_objects[j] in Thursdays:
            day_week = 'Thursday'
            day_week_compare = 4
        elif all_objects[j] in Fridays:
            day_week = 'Friday'
            day_week_compare = 5
        elif all_objects[j] in Saturdays:
            day_week = 'Saturday'
            day_week_compare = 6
        elif all_objects[j] in Sundays:
            day_week = 'Sunday'
            day_week_compare = 7


    if day_week:
        if len(all_objects)==3:
            for _ in range(2):
                del all_objects[-2]
        else:
            for _ in range(2):
                del all_objects[-1]
        receive = ' '.join(all_objects)
        for i in range (len(all_objects)):
            if all_objects[i]=='каждый' or all_objects[i]=='каждую' or all_objects[i]=='каждое' :
                status='Success'
                print("Message:{", "'STATUS':", status, ",", "'PARAMS': {'repeat_always:'", day_week, "}", "'DATE':{'year':",
                      year, ",", "'month':", month, ",", "'day':", day, ",", "'hour':", hour, ",", "'minute':", minute,
                      "}", ",", "'TEXT':", receive, "}", sep='')
                exit()
    for i in range (len(all_objects)):
        if all_objects[i-1]=='по' and all_objects[i]=='выходным':
            day_week = 'Saturday'
            day_week_compare = 6
            for o in range(2):
                del all_objects[i]
            receive = ' '.join(all_objects)
            print(receive)

    print(receive)
    print(day_week)
    print(day_week_compare)
    if day_week_compare:
        if day_week_compare>day_week_current:
            #day=str(day)
            #day=day_week
            day=int(day_current)+(day_week_compare-day_week_current)
            print(day)
        elif day_week_compare<day_week_current:
            day=int(day_current)+(day_week_compare-day_week_current+7)
            print(day)
    try:
        for i in range (len(all_objects)):
            if all_objects[i]=='следующей' or all_objects[i]=='следующем' :
                if all_objects[i]=='следующей' :
                    del all_objects[i]
                elif all_objects[i]=='следующем' :
                    del all_objects[i]
                for j in range (len(all_objects)):
                    if all_objects[j]=='неделе' :
                        day+=6
                        print(day)
                        if day>30:
                            day-=30
                            month+=1
                        del  all_objects [j]

                    elif all_objects[j]=='месяце' :
                        month+=1
                        del all_objects[j]

                    elif all_objects[j]=='году' :
                        year+=1
                        del all_objects[j]

                    receive=' '.join(all_objects)
    except IndexError:
        pass
    for u in range (len(all_objects)):

        if all_objects[u]=='сегодня' :
            del all_objects[u]
            print(all_objects)
            receive = " ".join(all_objects)

        elif all_objects[u]== 'завтра' :
            day+=1
            del all_objects[u]
            print(all_objects)
            receive = " ".join(all_objects)

        elif all_objects[u]=='послезавтра' :
            day+=2
            del all_objects[u]
            print(all_objects)
            receive = " ".join(all_objects)
        break

    match_find_delay_minute = re.findall('минут', receive)
    match_find_delay_hour = re.findall('час', receive)

    def repeat(day):
        if 'каждый' in all_objects:
            index1 = all_objects.index('каждый')
        elif 'Каждый' in all_objects:
            index1 = all_objects.index('Каждый')
        elif 'каждые' in all_objects:
            index1 = all_objects.index('каждые')
        elif 'Каждые' in all_objects:
            index1 = all_objects.index('Каждые')
        elif 'каждую' in all_objects:
            index1 = all_objects.index('каждую')
        elif 'Каждую' in all_objects:
            index1 = all_objects.index('Каждую')
        elif 'каждое' in all_objects:
            index1 = all_objects.index('каждое')
        elif 'Каждое' in all_objects:
            index1 = all_objects.index('Каждое')
        else:
            raise ValueError('Can not')
        if all_objects[index1] in every and all_objects[index1 + 1].isdigit() and all_objects[
            index1 + 2] in minutes_for_dalay:
            find_delayed_minute = int(all_objects[index1 + 1])
            sum_minutes = find_delayed_minute + minute
            find_delayed_hour = 0
            sum_hours = find_delayed_hour + hour
            print(sum_minutes)
            while sum_minutes > 60:
                sum_minutes -= 60
                sum_hours += 1
            else:
                print('Каждые', find_delayed_hour, 'час', 'каждые', find_delayed_minute, 'минут')


        elif all_objects[index1] in every and all_objects[index1 + 1].isdigit() and all_objects[index1 + 2] in hours_for_delay:
            find_delayed_minute = 0
            sum_minutes = find_delayed_minute + minute
            find_delayed_hour = int(all_objects[index1 + 1])
            sum_hours = hour + find_delayed_hour
            while sum_hours > 24:
                sum_hours -= 24
                day += 1
            else:
                print('каждые', find_delayed_hour, 'часов', 'каждые', find_delayed_minute, 'минут')


        elif all_objects[index1] in every and all_objects[index1 + 1] in hours_for_delay:
            find_delayed_minute = 0
            sum_minutes = find_delayed_minute + minute
            find_delayed_hour = 1
            sum_hours = hour + find_delayed_hour
            while sum_hours > 24:
                sum_hours -= 24
                day += 1
            else:
                print('Каждый', find_delayed_hour, 'часов', 'каждый', find_delayed_minute, 'минут')
                rem_list1 = [all_objects[index1], all_objects[index1 + 1]]
                rem = ' '.join(rem_list1)
                for _ in range(2):
                    del all_objects[index1]
                print(all_objects)
                receive = " ".join(all_objects)
                print(receive)
                status = 'SUCCESS'
                receive = re.sub('\w [0-2]\d:[0-5]\d', '', receive)
                print("Message:{", "'STATUS':", status, ",", "'PARAMS': {'repeat_always:'", rem, "}", "'DATE':{'year':",
                      year, ",", "'month':", month, ",", "'day':", day, ",", "'hour':", hour, ",", "'minute':", minute,
                      "}", ",", "'TEXT':", receive, "}", sep='')
                exit()

        rem_list=[all_objects[index1],all_objects[index1+1],all_objects[index1+2]]
        rem=' '.join(rem_list)

        for _ in range(3):
            del all_objects[index1]
        print(all_objects)
        receive = " ".join(all_objects)
        print(receive)
        status='SUCCESS'

        print("Message:{","'STATUS':",status,",", "'PARAMS': {'repeat_always:'",rem ,"}" ,"'DATE':{'year':",year,",","'month':",month,",","'day':",day,",","'hour':",hour,",","'minute':",minute,"}",",","'TEXT':", receive,"}",sep='')
        exit()
    if  (match_find_delay_minute or match_find_delay_hour) :

        try:

            if 'через' in all_objects:
                index = all_objects.index('через')
                print(index)
            elif 'Через' in all_objects:
                index = all_objects.index('Через')
            else:
                for i in range(len(every)):
                    if every[i]in all_objects:
                        repeat(day)
                #raise ValueError('Try again')
                    else:
                        pass

            if (all_objects[index] == 'Через' or all_objects[index] == 'через') and all_objects[index + 1].isdigit() and all_objects[index + 2] in minutes_for_dalay:
                    find_delayed_minute = int(all_objects[index + 1])
                    sum_minutes=find_delayed_minute+minute
                    find_delayed_hour = 0
                    sum_hours=find_delayed_hour+hour
                    day_plus=0
                    print(sum_minutes)
                    while sum_minutes> 59:
                        sum_minutes-= 60
                        sum_hours += 1
                    while sum_hours>23:
                        sum_hours-=24
                        day_plus+=1
                    else:
                        print('Через', find_delayed_hour, 'час', 'через', sum_minutes, 'минут')



            elif (all_objects[index] == 'Через' or all_objects[index] == 'через') and all_objects[index + 1].isdigit() and all_objects[index + 2] in hours_for_delay:
                        find_delayed_minute = 0
                        sum_minutes=find_delayed_minute+minute
                        find_delayed_hour = int(all_objects[index + 1])
                        sum_hours=hour+find_delayed_hour
                        day_plus=0
                        while sum_hours > 23:
                            sum_hours -= 24
                            day_plus += 1
                        else:
                            print('Через', find_delayed_hour, 'часов', 'через', find_delayed_minute, 'минут')

            elif (all_objects[index] == 'Через' or all_objects[index] == 'через') and all_objects[index + 1] in hours_for_delay:
                        find_delayed_minute = 0
                        sum_minutes=find_delayed_minute+minute
                        find_delayed_hour = 1
                        sum_hours=hour+find_delayed_hour
                        day_plus=0
                        while sum_hours > 23:
                            sum_hours -= 24
                            day_plus += 1
                        else:
                            print('Через', find_delayed_hour, 'часов', 'через', find_delayed_minute, 'минут')

            elif (all_objects[index] == 'Через' or all_objects[index] == 'через') and all_objects[index + 1].isdigit() and all_objects[index + 2] in hours_for_delay and all_objects[index + 3].isdigit() and all_objects[index + 4] in minutes_for_dalay:
                find_delayed_hour = int(all_objects[index + 1])
                sum_hours = hour + find_delayed_hour
                find_delayed_minute = int(all_objects[index + 3])
                sum_minutes = find_delayed_minute + minute
                day_plus=0
                while sum_minutes > 59:
                    sum_minutes -= 60
                    sum_hours += 1
                while sum_hours > 23:
                    sum_hours -= 24
                    day_plus += 1
                print('Через', find_delayed_hour, 'час', 'через', find_delayed_minute, 'минут')

        except AttributeError:
            print('Необходимо ввести в формате: Через (число) часов (число) минут ИЛИ Через (число) часов ИЛИ Через (число) минут')

        else:
            minute=sum_minutes
            hour=sum_hours
            day+=day_plus
            #if len(all_objects)-index>2:
            for _ in range(3):
                del all_objects[index]
            print(all_objects)
            receive=" ".join(all_objects)
            #elif len(all_objects)-index>5:
             #   for _ in range(6):
              #      del all_objects[index]
               # print(all_objects)
                #receive=" ".join(all_objects)

    match_find_delay_day = re.search('ден', receive) or re.search('дн', receive)
    match_find_delay_month = re.search('месяц', receive)
    match_find_delay_year = re.search('год', receive) or re.search('лет', receive)

    def repeat1(year, month, day):
        if 'каждый' in all_objects:
            index1 = all_objects.index('каждый')
        elif 'Каждый' in all_objects:
            index1 = all_objects.index('Каждый')
        elif 'каждые' in all_objects:
            index1 = all_objects.index('каждые')
        elif 'Каждые' in all_objects:
            index1 = all_objects.index('Каждые')
        elif 'каждую' in all_objects:
            index1 = all_objects.index('каждую')
        elif 'Каждую' in all_objects:
            index1 = all_objects.index('Каждую')
        elif 'каждое' in all_objects:
            index1 = all_objects.index('каждое')
        elif 'Каждое' in all_objects:
            index1 = all_objects.index('Каждое')
        else:
            raise ValueError('Can not')


        if all_objects[index1] in every and all_objects[index1 + 1].isdigit() and \
                all_objects[index1 + 2] in days_for_dalay:
            find_delayed_year = 0
            sum_years = find_delayed_year + int(year_current)
            find_delayed_month = 0
            sum_months = find_delayed_month + int(month_current)
            find_delayed_day = int(all_objects[index1 + 1])
            sum_days = find_delayed_day + int(day_current)
            while sum_days > 30:
                sum_days -= 30
                sum_months += 1
            print('Каждые', find_delayed_year, 'лет', 'каждый', find_delayed_month, 'месяцев', 'каждый',find_delayed_day,'дня')

        if all_objects[index1] in every and all_objects[
            index1 + 1].isdigit() and all_objects[index1 + 2] in months_for_delay:
            find_delayed_year = 0
            sum_years = find_delayed_year + int(year_current)
            find_delayed_month = int(all_objects[index1 + 1])
            sum_months = find_delayed_month + int(month_current)
            find_delayed_day = 0
            sum_days = find_delayed_day + int(day_current)
            while sum_months > 12:
                sum_months -= 12
                sum_years += 1
            print('Каждый', find_delayed_year, 'лет', 'Каждый', find_delayed_month, 'месяцев', 'каждый',
                  find_delayed_day, 'дней')

        if all_objects[index1] in every and all_objects[
            index1 + 1].isdigit() and all_objects[index1 + 2] in years_for_delay:
            find_delayed_year = int(all_objects[index1 + 1])
            sum_years = find_delayed_year + int(year_current)
            find_delayed_month = 0
            sum_months = find_delayed_month + int(month_current)
            find_delayed_day = 0
            sum_days = find_delayed_day + int(day_current)
            print('Каждый', find_delayed_year, 'лет', 'каждый', find_delayed_month, 'месяцев', 'каждый',
                  find_delayed_day,
                  'дней')


        rem_list = [all_objects[index1], all_objects[index1 + 1], all_objects[index1 + 2]]
        rem = ' '.join(rem_list)

        for _ in range(3):
            del all_objects[index1]
        print(all_objects)
        receive = " ".join(all_objects)
        print(receive)
        status = 'SUCCESS'
        print("Message:{", "'STATUS':", status, ",", "'PARAMS': {'repeat_always:'", rem, "}", "'DATE':{'year':",
              year,
              ",", "'month':", month, ",", "'day':", day, ",", "'hour':", hour, ",", "'minute':", minute, "}",
              ",",
              "'TEXT':", receive, "}", sep='')
        exit()

    if (match_find_delay_day or match_find_delay_month or match_find_delay_year):
        try:
            if 'через' in all_objects:
                index = all_objects.index('через')
            elif 'Через' in all_objects:
                index = all_objects.index('Через')
            else:
                for i in range(len(every)):
                    if every[i] in all_objects:
                        repeat1(year, month, day)
                    else:
                        pass
            # raise ValueError ('Try again')

            if (all_objects[index] == 'Через' or all_objects[index] == 'через') and all_objects[
                index + 1].isdigit() and all_objects[index + 2] in days_for_dalay:
                find_delayed_year = 0
                sum_years = find_delayed_year + int(year_current)
                find_delayed_month = 0
                sum_months = find_delayed_month + int(month_current)
                find_delayed_day = int(all_objects[index + 1])
                sum_days = find_delayed_day + int(day_current)
                while sum_days > 30:
                    sum_days -= 30
                    sum_months += 1
                print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев', 'через',
                      find_delayed_day, 'дня')

            if (all_objects[index] == 'Через' or all_objects[index] == 'через') and all_objects[
                index + 1].isdigit() and all_objects[index + 2] in months_for_delay:
                find_delayed_year = 0
                sum_years = find_delayed_year + int(year_current)
                find_delayed_month = int(all_objects[index + 1])
                sum_months = find_delayed_month + int(month_current)
                find_delayed_day = 0
                sum_days = find_delayed_day + int(day_current)
                while sum_months > 12:
                    sum_months -= 12
                    sum_years += 1
                print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев', 'через',
                      find_delayed_day, 'дней')

            if (all_objects[index] == 'Через' or all_objects[index] == 'через') and all_objects[
                index + 1].isdigit() and all_objects[index + 2] in years_for_delay:
                find_delayed_year = int(all_objects[index + 1])
                sum_years = find_delayed_year + int(year_current)
                find_delayed_month = 0
                sum_months = find_delayed_month + int(month_current)
                find_delayed_day = 0
                sum_days = find_delayed_day + int(day_current)
                print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев', 'через',
                      find_delayed_day,
                      'дней')

            if match_find_delay_day and match_find_delay_month and match_find_delay_year:
                if (all_objects[index] == 'Через' or all_objects[index] == 'через') and all_objects[
                    index + 1].isdigit() and (
                        all_objects[index + 2] == 'год' or all_objects[index + 2] == 'года' or
                        all_objects[index + 2] == 'лет') and all_objects[index + 3].isdigit() and (
                        all_objects[index + 4] == 'месяц'
                        or all_objects[index + 4] == 'месяца' or all_objects[index + 4] == 'месяцев') and \
                        all_objects[index + 5].isdigit() and (all_objects[index + 6] == 'день' or
                                                              all_objects[index + 6] == 'дня' or all_objects[
                                                                  index + 6] == 'дней'):
                    find_delayed_year = all_objects[index + 1]
                    sum_years = find_delayed_year + int(year_current)
                    find_delayed_month = all_objects[index + 3]
                    sum_months = find_delayed_month + int(month_current)
                    find_delayed_day = all_objects[index + 5]
                    sum_days = find_delayed_day + int(day_current)
                    while sum_days > 30:
                        sum_days -= 30
                        sum_months += 1
                    while sum_months > 12:
                        sum_months -= 12
                        sum_years += 1
                    print('Через', find_delayed_year, 'лет', 'через', find_delayed_month, 'месяцев', 'через',
                          find_delayed_day,
                          'дней')


        except IndexError:
            print('Необходимо ввести в формате: Через (число) лет (число) месяцев (число) дней ')


        else:
            day = sum_days
            month = sum_months
            year = sum_years
            # if find_delayed_day:
            #    day=day+int(find_delayed_day)
            # else:
            #    day=day_current
            # if find_delayed_month:
            #    month=month+int(find_delayed_month)
            # else:
            #    month=month_current
            # if find_delayed_year:
            #    year = year + int(find_delayed_year)
            # else:
            #    year=year_current
            # if find_delayed_year and  find_delayed_month and  find_delayed_day:
            #    year = year + int(find_delayed_year)
            #    month = month + int(find_delayed_month)
            #    day = day + int(find_delayed_day)
            print(year)
            print(month)
            print(day)

            if len(all_objects) - index > 2:
                for _ in range(3):
                    del all_objects[index]
                print(all_objects)
                receive = " ".join(all_objects)
            elif len(all_objects) - index > 6:
                for _ in range(6):
                    del all_objects[index]
                print(all_objects)
                receive = " ".join(all_objects)
                # конец обработки лет месяцев дней

    #delayed_action(find_delayed_hour, find_delayed_minute)




    for i in range(len(all_objects)):
        if (all_objects[i].isdigit() and int(all_objects[i])<32) and all_objects[i+1].isalpha() :
            day_for_string_month=all_objects[i]
            try:
                if (all_objects[i+2].isdigit() and int(all_objects[i+2])>2000): #and all_objects[i+3]=='года':
                    string_year=int(all_objects[i+2])
                    print(string_year)
            except IndexError:
                pass
            for j in range (len(MONTHS)):
                if all_objects[i+1] in MONTHS[j]:
                    print(MONTHS[j]) # поиск месяца
                    if MONTHS[j] == Januarys:
                        string_month = '01'
                        n = 31
                    elif MONTHS[j] == Februarys:
                        string_month = '02'
                        n = 28
                    elif MONTHS[j] == Marchs:
                        string_month = '03'
                        n = 31
                    elif MONTHS[j] == Aprils:
                        string_month = '04'
                        n = 30
                    elif MONTHS[j] == Mays:
                        string_month = '05'
                        n = 31
                    elif MONTHS[j] == Junes:
                        string_month = '06'
                        n = 30
                    elif MONTHS[j] == Julys:
                        string_month = '07'
                        n = 31
                    elif MONTHS[j] == Augusts:
                        string_month = '08'
                        n = 31
                    elif MONTHS[j] == Septembers:
                        string_month = '09'
                        n = 30
                    elif MONTHS[j] == Octobers:
                        string_month = '10'
                        n = 31
                    elif MONTHS[j] == Novembers:
                        string_month = '11'
                        n = 30
                    elif MONTHS[j] == Decembers:
                        string_month = '12'
                        n = 31
                    else:
                        string_month = ''
                    print(string_month)
                    print(day_for_string_month)
                    print(string_year)
            if int(day_for_string_month)>n:
                print('Try again')
                main()
                #exit()

                        # while flag==1:
           #     print('Try again')
                #continue



    #print(string_month)
    #print(day_for_string_month)




            #long_delayed_action(find_delayed_year, find_delayed_month,find_delayed_day,Year,Month,Day,Hour,Minute)


    out_1 = re.sub('\w [0-2]\d:[0-5]\d', '', receive)                                                                      #удаление времени формата dd:dd из сообщения
    out_2=re.sub('\d{2}.\d{2}.\d{4}', '', out_1)                                                                        #удаление даты
    out_2_str=str(out_2)
    out=out_2_str
    print(year)
    print(minute)
    print(hour)
    print(out)
    print(day)
    if year!=None and minute!=None and hour!=None and out!='':                                                                                #самый конец
        status='SUCCESS'
        day_out=''
        month_out=''

        if day_week:
            day_out=day
            month_out=month
            print("Message:{", "'STATUS':", status, ",", "Params:{",day_week,"}","'DATE':{'year':", year, ",", "'month':", month_out, ",",
                  "'day':", day_out, ",", "'hour':", hour, ",", "'minute':", minute, "}", ",", "'TEXT':", out, "}",
                  sep='')
            exit()

        '''elif day:
            day_out=day
            month_out=month'''


        if string_month and day_for_string_month:
            day_out=day_for_string_month
            month_out=string_month

            out_3 = out_2_str.split()
            #out_3.remove(day_for_string_month)
            for _ in range (2):
                out_3.pop(all_objects.index(day_for_string_month))

            if string_year:
                year=string_year
                #for _ in range(2):
                out_3.pop(all_objects.index(day_for_string_month))
            else:
                pass
            out_3_str = str(' '.join(out_3))
            out = out_3_str
        else :
            day_out=day
            month_out=month

        print("Message:{","'STATUS':",status,",","'DATE':{'year':",year,",","'month':",month_out,",","'day':",day_out,",","'hour':",hour,",","'minute':",minute,"}",",","'TEXT':", out,"}",sep='')

    else:
        status='FAILURE'
        print('Ошибка',status) #См 189

if __name__ == '__main__':
    main()


