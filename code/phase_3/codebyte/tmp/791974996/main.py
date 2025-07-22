def CountingMinutesI(strParam):
    # Split the input string into the two time strings
    time1_str, time2_str = strParam.split('-')

    # Helper function to convert 12-hour time string to total minutes from midnight
    def convert_to_minutes(time_str):
        # Determine if it's AM or PM and remove the indicator
        if 'am' in time_str:
            is_am = True
            time_str = time_str.replace('am', '')
        else:
            is_am = False
            time_str = time_str.replace('pm', '')

        # Split into hour and minute, and convert to integers
        h, m = map(int, time_str.split(':'))

        # Convert to total minutes from midnight (0 to 1439)
        total_minutes = 0
        if is_am:
            if h == 12: # 12:xx AM is 00:xx in 24-hour format
                total_minutes = m
            else: # 1:xx AM to 11:xx AM
                total_minutes = h * 60 + m
        else: # PM
            if h == 12: # 12:xx PM is 12:xx in 24-hour format
                total_minutes = 12 * 60 + m
            else: # 1:xx PM to 11:xx PM, add 12 hours
                total_minutes = (h + 12) * 60 + m

        return total_minutes

    # Convert both time strings to minutes from midnight
    minutes1 = convert_to_minutes(time1_str)
    minutes2 = convert_to_minutes(time2_str)

    # Calculate the difference in minutes
    if minutes2 >= minutes1:
        # Second time is on the same day or the next day but not wrapping around 24h cycle within calculation
        diff_minutes = minutes2 - minutes1
    else:
        # Second time is earlier than the first time, meaning it wraps around midnight
        # Example: 10:00pm - 2:00am. Difference is from 10pm to midnight + midnight to 2am
        diff_minutes = (24 * 60 - minutes1) + minutes2

    return diff_minutes

# keep this function call here
# print(CountingMinutesI(input())) 