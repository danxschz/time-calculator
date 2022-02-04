# Time Calculator -- Scientific Computing with Python Project #2

## Main function
def add_time(start, duration, day = "empty"):
    starthour = int(start.split(":")[0])
    startminute = int(start.split(":")[1].split()[0])
    period = start.split()[1]
    durationhour = int(duration.split(":")[0])
    durationminute = int(duration.split(":")[1])

    # Calculate result minute
    newminute = startminute + durationminute
    if newminute >= 60:
        newminute = newminute - 60
        extrahour = 1
    else:
        extrahour = 0
    newminute = f"{newminute:02}"

    # Calculate result hour
    cycles = int((starthour + durationhour + extrahour) / 12)
    newhour = starthour + durationhour + extrahour - (12*cycles)
    if newhour == 0:
        newhour = 12
    newhour = str(newhour)

    # Calculate result period (AM or PM)
    if period == "AM":
        if (cycles % 2) == 0:
            newperiod = period
        else:
            newperiod = "PM"
    if period == "PM":
        if (cycles % 2) == 0:
            newperiod = period
        else:
            newperiod = "AM"

    # Calculate how many days later
    if period == "AM":
        n = int(cycles / 2) # n refers to days passed
    if period == "PM":
        if cycles == 1:
            n = 1
        else:
            n = round(cycles / 2)
    if n == 1:
        dayslater = "(next day)"
    if n > 1:
        dayslater = f"({n} days later)"

    # Calculate day of the week
    weekdict = {"monday" : 1, "tuesday" : 2, "wednesday" : 3, "thursday" : 4,
            "friday" : 5, "saturday" : 6, "sunday" : 7}
    day = day.lower()
    if day in weekdict:
        daynumber = weekdict[day]
        daynumber += n
        if daynumber > 7:
            weeks = int(daynumber/7)
            daynumber -= (7 * weeks)
            if daynumber == 0:
                daynumber = 7
        weeklist = ["Blank", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        newday = weeklist[daynumber]

    # Assemble new time
    if day == "empty" or day not in weekdict:
        if n >= 1:
            new_time = f"{newhour}:{newminute} {newperiod} {dayslater}"
        else:
            new_time = f"{newhour}:{newminute} {newperiod}"
    else:
        if n >= 1:
            new_time = f"{newhour}:{newminute} {newperiod}, {newday} {dayslater}"
        else:
            new_time = f"{newhour}:{newminute} {newperiod}, {newday}"
    return new_time
