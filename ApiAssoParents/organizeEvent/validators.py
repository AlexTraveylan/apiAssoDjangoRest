from django.core.exceptions import ValidationError
import re

def validate_password(password: str):
    if len(password) < 4:
        raise ValidationError(f"{password} est trop court, il doit contenir minimum 4 caractères.")

def validate_username(username: str):
    if not bool(re.match(r'^[a-zA-Z]{2}', username)):
        raise ValidationError(f"{username} n'est pas un nom possible")

