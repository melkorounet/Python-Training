workout_schedule = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
rest, chill, go_train = 'Rest', 'Chill out!', 'Go train {}'


def get_workout_motd(day):
    """First title case the passed in day argument
       (so monday or MONDAY both result in Monday).

       Then check if this title cased day is in the given workout_schedule dict.

       If it is retrieve the workout (value), if not raise a KeyError.

       Return the chill variable if it's a rest day (Saturday / Sunday),
       else return the go_train variable with the workout interpolated.

       Examples:
       - if day is Saturday -> return 'Chill out!'
       - if day is Thursday -> return 'Go train Legs'
       - if day is Sunday -> return 'Chill out!'
       - if day is Monday -> return 'Go train Chest+biceps'

       Trivia: /etc/motd is a file on Unix-like systems that contains
       a 'message of the day'"""
    valid_day = []
    for days in workout_schedule: 
        valid_day.append(days)
    if day.lower().capitalize() not in valid_day :
        raise KeyError(day, 'is not a valid day')

    if workout_schedule[day.lower().capitalize()] == rest :
        return chill
    else :
        return go_train.format(workout_schedule[day.lower().capitalize()])

get_workout_motd("sUnDay")