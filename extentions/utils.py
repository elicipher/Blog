
from .import jalali



def time_Converter(time):
    mahhaye_shamsi = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند']
    time_to_str = "{},{},{}".format(time.year , time.month , time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)
    for index , mounth in enumerate(mahhaye_shamsi):
        if time_to_list[1] == index+1 :
            time_to_list[1] = mounth
            break

    output = "{} {} {}".format(
        time_to_list[0],
        time_to_list[1],
        time_to_list[2],
        time.hour,
        time.minute,
        
    )
    return output

