from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize = value.size

    if filesize > 41943040:
        raise ValidationError("You cannot upload file more than 40Mb")
    else:
        return value

def validate_title_size(value):
    titlesize = len(value)

    if titlesize > 250:
        raise ValidationError("Title cannot be more then 250 symbols")
    else:
        return value
