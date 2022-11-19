from datetime import datetime


def get_week_number(datetime_obj):
    num = datetime_obj.strftime("%U")
    return f"Week number: {num}."
