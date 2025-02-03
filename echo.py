#사용자 입력을 반복적으로 받아 그대로 출력하는 프로그램

def main():
    while True:
        user_input = input("문장을 입력하세요 (!quit 입력 시 종료): ")
        if user_input == "!quit":
            print("프로그램을 종료합니다.")
            break
        print("입력한 문장:", user_input)

if __name__ == "__main__":
    main()
