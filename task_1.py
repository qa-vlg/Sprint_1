s = '1h 45m,360s,25m,30m 120s,2h 60s' 

total_minutes = 0

for i in s.replace(' ', ',').split(','):
    time_units = i.split()
    for time_unit in time_units:
        if 'h' in time_unit:
            total_minutes += int(time_unit[:-1]) * 60 # to convert hours into minutes: number of hours multiply by 60
        if 'm' in time_unit:
            total_minutes += int(time_unit[:-1]) # if minutes then no conversion needed
        if 's' in time_unit:
            total_minutes += int(time_unit[:-1]) // 60 # to convert seconds into minutes: number of seconds divide by 60, '//' used to avoid floating point

print(total_minutes)