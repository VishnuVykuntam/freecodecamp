def add_time(start, duration, day=None):
    return_string=''
    initial_time=start.split()
    # print(initial_time)
    initial_hrs=initial_time[0].split(':')
    initial_hr=int(initial_hrs[0])
    initial_min=int(initial_hrs[1])
    # print(initial_hrs)
    if initial_time[1]=='PM':
        initial_hr+=12
    duration_hrs=duration.split(':')
    duration_hr=int(duration_hrs[0])
    duration_min=int(duration_hrs[1])
    # print(duration_hrs)
    final_hr=initial_hr+duration_hr
    final_min=initial_min+duration_min
    if final_min>=60:
        final_hr+=1
        final_min-=60
    if final_min<10:
        final_min=f'0{final_min}'
    else:
        
        final_min=f'{final_min}'
    num_days=final_hr//24
    # print(num_days)
    final_hr=final_hr%24
    
    if final_hr>=12:
        final_hr-=12
        period='PM'
    else:
        period='AM'
    if final_hr==0:
        final_hr='12'
    else:
        final_hr=f'{final_hr}'
    return_string=final_hr+':'+final_min+f' {period}'
    # print(return_string)
    # print(final_hr,':',final_min,' ',period,)
    if day:
        day_name=day.lower()
        list_days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
        if day_name in list_days:
            day_type=list_days.index(day_name)
        day_type+=num_days
        day_type%=7
        final_day_name=list(list_days[day_type])
        final_day_name[0]=final_day_name[0].upper()
        final_day_name=''.join(final_day_name)
        return_string+=f', {final_day_name}'
    if num_days>0:
        if num_days==1:
            num_of_days_to_display=' (next day)'
        else:
            num_of_days_to_display=f' ({num_days} days later)'
        # print(num_of_days_to_display)
        return_string+=num_of_days_to_display
    # print(return_string)/
    return return_string






    # return new_time
print(add_time('3:30 PM', '2:12'))