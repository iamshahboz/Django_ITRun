

from django.core.exceptions import ValidationError 
from decimal import Decimal


#this is for book model

def validate_string(value):
    if not isinstance(value, str):
        raise ValidationError('Title must be string')
    
def validate_decimal(value):
    if not isinstance(value, Decimal):
        raise ValidationError('Value must be decimal')
    
def validate_integer(value):
    if not isinstance(value, int):
        raise ValidationError('Value must be integer')
    

    
