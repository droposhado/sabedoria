from flask import current_app


def convert(total_minutes):
    """convert minutes to hours"""

    total_minutes = int(total_minutes)
    # Get hours with floor division
    hours = total_minutes // 60

    # Get additional minutes with modulus
    # minutes = total_minutes % 60

    # Create time as a string
    # if minutes != 0:
    #    time = float("{}.{}".format(hours, minutes))
    # else:
    #    time = float("{}.0".format(hours))

    current_app.logger.debug(f"{total_minutes} min converted in {hours} hours")

    return hours
