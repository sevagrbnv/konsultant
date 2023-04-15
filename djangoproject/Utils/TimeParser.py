class DateTimeParser:

    def toDict(self, form, string):
        if (form == 'очной'):
            # {times[0]}-{times[1]} {dates[0]}
            times, date = string.split(' ')
            time1, time2 = times.split('-')
            return {'ochnaya': {'time1': time1, 'time2': time2, 'date': date}}
        elif (form == 'заочной'):
            # {times[0]}-{times[1]} {dates[0]}-{dates[1]}
            times, dates = string.date.split(' ')
            time1, time2 = times.split('-')
            date1, date2 = dates.split('-')
            return {'zaochnaya': {'time1': time1, 'time2': time2, 'date1': date1, 'date2': date2}}
        else:
            # {times[0]}-{times[1]} {dates[0]} / {times[2]}-{times[3]} {dates[1]}-{dates[2]}
            och, zaoch = string.date.split(' / ')
            times, date = och.split(' ')
            time1, time2 = times.split('-')

            times, dates = zaoch.split(' ')
            time3, time4 = times.split('-')
            date3, date4 = dates.split('-')

            return {'ochnaya': {'time1': time1, 'time2': time2, 'date': date},
                    'zaochnaya': {'time1': time3, 'time2': time4, 'date1': date3, 'date2': date4}}
