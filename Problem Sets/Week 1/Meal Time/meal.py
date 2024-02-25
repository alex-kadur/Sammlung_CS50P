# prompt user for time
# outputs whether breakfast time, lunch time, or dinner time
# breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00
# if not time for a meal, don’t output anything


def main():
    input_time = input("What time is it? ")
    if (convert(input_time)) >= 7 and (convert(input_time)) <= 8:
        print("breakfast time")
    elif (convert(input_time)) >= 12 and (convert(input_time)) <= 13:
        print("lunch time")
    elif (convert(input_time)) >= 18 and (convert(input_time)) <= 19:
        print("dinner time")


# convert time str to corresponding number of hours as a float
# add support for 12-hour times, input time as #:## a.m. and ##:## a.m. or #:## p.m. and ##:## p.m
# add support for 24-hour times, input time as #:## or ##:##


def convert(time):
    if time.find("a.m.") != -1 or time.find("p.m.") != -1:
        return convert_12(time)
    else:
        hours, minutes = time.split(":")
        return float(hours) + float(minutes) / 60


def convert_12(time):
    time_12, suffix = time.split(" ")
    if suffix == "p.m.":
        hours, minutes = time_12.split(":")
        return float(hours) + float(minutes) / 60 + 12
    else:
        hours, minutes = time_12.split(":")
        return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
