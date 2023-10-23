from .models import Post
import re
from django.core.exceptions import ValidationError
from .validators import validate_symbols, validate_no_profanity

def validate_post():
    #1. 모든 포스트 데이터 가져오기 
    posts = Post.objects.all()

    # 각 포스트의 유효성 검사 및 삭제 처리 결과를 저장할 리스트
    errors = []

    for post in posts:
        # 금지어 검사
        try:
            validate_no_profanity(post.title)
        except ValidationError as e:
            errors.append(f"{post.id}번 글에서 유효성 검사 오류 발생: {e.message}")

            # 금지어를 삭제합니다.
            banned_words = e.message.split()
            sanitized_content = post.content
            for banned_word in banned_words:
                sanitized_content = sanitized_content.replace(banned_word, '')

            # 데이터 수정 및 저장
            post.content = sanitized_content
            post.save()
        
        try:
            validate_no_profanity(post.content)
        except ValidationError as e:
            errors.append(f"{post.id}번 글에서 유효성 검사 오류 발생: {e.message}")
            sanitized_content = post.content
            banned_words = [
                word for word in e.message.split() if word in post.content
            ]
            for banned_word in banned_words:
                sanitized_content = sanitized_content.replace(banned_word, '')

            # 데이터 수정 및 저장
            post.content = sanitized_content
            post.save()


        # 특수 문자 검사
        try:
            validate_symbols(post.title)
        except ValidationError as e:
            errors.append(f"{post.id}번 글에서 유효성 검사 오류 발생: {e.message}")

            # 특수 문자를 삭제합니다.
            special_chars = re.findall(r'[!@#$%^&*(),.?":{}|<>]', e.message)
            sanitized_content = post.content
            for char in special_chars:
                sanitized_content = sanitized_content.replace(char, '')

            # 데이터 수정 및 저장
            post.content = sanitized_content
            post.save()
        
        try:
            validate_symbols(post.content)
        except ValidationError as e:
            errors.append(f"{post.id}번 글에서 유효성 검사 오류 발생: {e.message}")

            # 특수 문자를 삭제합니다.
            special_chars = re.findall(r'[!@#$%^&*(),.?":{}|<>]', e.message)
            sanitized_content = post.content
            for char in special_chars:
                sanitized_content = sanitized_content.replace(char, '')

            # 데이터 수정 및 저장
            post.content = sanitized_content
            post.save()



        if post.dt_modified < post.dt_created:
            errors.append(f"{post.id}번 글의 수정일이 생성일보다 과거입니다.")
            post.save()

    # 모든 오류 메시지 출력
    for error in errors:
        print(error)