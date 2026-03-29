# input
input_time = input("")

# hàm cắt hh:mm:sss
def split_time(input_time):
    try:
        time_list = input_time.split(":")
        hour, minute, second = int(time_list[0]), int(time_list[1]), int(time_list[2])
        return hour, minute, second # tuple
    except:
        print("Invalid time format")
        return None
    
# hàm kiểm tra hợp lệ
def validate_time(hour, minute, second):
    if hour == None or minute == None or second == None:
        return "Không hợp lệ"
    # kiểm tra giờ (0 -> 23)
    if hour < 0 or hour > 23
        return "Không hợp lệ"
    # kiểm tra phút (0 -> 59)
    if minute < 0 or hour > 59
        return "Không hợp lệ"
    # kiểm tra giây (0 -> 59)
    if second < 0 or hour > 59
        return "Không hợp lệ"


    return "Hợp lệ" # những trường hợp khác đều hợp lệ

# output
print(validate_time(*split_time(input_time)))
