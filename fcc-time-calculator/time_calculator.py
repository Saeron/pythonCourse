class Week_days():

    list_days = ['Monday', 'Tuesday', 'Wednesday',
                 'Thursday', 'Friday', 'Saturday', 'Sunday']
    actual_day = -1
    id_days = 6


    def __init__(self, day):
        if day != '':
            self.actual_day = self.__search_day(day.lower().capitalize())
        else:
            self.actual_day = -1

    def __search_day(self, day):
        for i in range(0, len(self.list_days)):
            if self.list_days[i] == day:
                return i
        return -1

    def add_day(self):
        if self.actual_day != -1:
            if self.actual_day < self.id_days:
                self.actual_day = self.actual_day + 1
            else:
                self.actual_day = 0

    def get_day(self):
        if self.actual_day != -1:
            return ', ' + self.list_days[self.actual_day]
        return ''


class Extra():
    days = 0

    def add_day(self):
        self.days+= 1
    
    def get_days(self):
        if self.days <= 0:
            return ''
        elif self.days == 1:
            return ' (next day)'
        else:
            return ' ('+str(self.days)+' days later)'



def add_time(start, duration, day=''):

    split_start = start.split()
    time = split_start[0]
    am_pm = split_start[1]

    hours = time.split(':')[0]
    minutes = time.split(':')[1]

    add_hours = duration.split(':')[0]
    add_minutes = duration.split(':')[1]

    new_time = ''
    extra_info = Extra()
    the_day = ''

    my_day = Week_days(day)

    extra_hours = 0
    mins_to_add = int(minutes) + int(add_minutes)

    if mins_to_add > 60:
        (extra_hours, mins_to_add) = divmod(mins_to_add, 60)

    final_hour = int(hours) + int(add_hours) + extra_hours
    # aqui mientras final hour sea mayot igual a 12 hacer estp:
    while final_hour > 12 or (final_hour == 12 and mins_to_add > 0):
        if final_hour >=12 and am_pm == 'AM':
            am_pm = 'PM'
        elif final_hour >=12:
            am_pm = 'AM'
            my_day.add_day()
            extra_info.add_day()
        final_hour = final_hour - 12

    if final_hour == 0:
        final_hour = 12

    mins_to_add = str(mins_to_add)
    if len(mins_to_add) < 2:
        mins_to_add = '0' + mins_to_add
    final_mins = mins_to_add

    the_day = my_day.get_day()
    new_time = str(final_hour)+':' + mins_to_add + \
        ' '+am_pm + the_day + extra_info.get_days()

    return new_time
