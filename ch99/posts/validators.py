import re
from django.core.exceptions import ValidationError

def validate_symbols(value):
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
        raise ValidationError('특수 문자는 사용할 수 없습니다.', code='special-char-err')
    

def validate_no_profanity(value):
    profanities = [
        '개새끼', '새끼', 'fuck',  '씨발', '좆까', 
        '썅', '미친놈', '미친년', '닥쳐', '미친',
        '꺼져', '잼민', '시발', '조까', '좆', 
        '시발', '거지', '좆같네', 
    ]
    for profanity in profanities:
        if re.search(rf'\b{re.escape(profanity)}\b', value, re.IGNORECASE):
            raise ValidationError(f'"{profanity}"(과)와 같은 비속어는 사용할 수 없습니다.', code='profanity-err')