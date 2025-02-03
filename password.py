import re

def validate_password(password: str) -> bool:
    """
    비밀번호가 최소 하나의 영문 소문자, 영문 대문자, 숫자 및 기호를 포함하는지 확인합니다.
    """
    if len(password) < 8:
        print("비밀번호는 최소 8자 이상이어야 합니다.")
        return False
    if not re.search(r"[a-z]", password):
        print("비밀번호는 최소 하나의 소문자를 포함해야 합니다.")
        return False
    if not re.search(r"[A-Z]", password):
        print("비밀번호는 최소 하나의 대문자를 포함해야 합니다.")
        return False
    if not re.search(r"\d", password):
        print("비밀번호는 최소 하나의 숫자를 포함해야 합니다.")
        return False
    if not re.search(r"[@$!%*?&#]", password):
        print("비밀번호는 최소 한 개의 특수문자(@$!%*?&#|<>())를 포함해야 합니다.")
        return False
    
    return True

def main():
    while True:
        user_input = input("비밀번호를 입력하세요 (!quit 입력 시 종료): ")
        if user_input == "!quit":
            print("프로그램을 종료합니다.")
            break
        if validate_password(user_input):
            print("유효한 비밀번호입니다.")

if __name__ == "__main__":
    main()