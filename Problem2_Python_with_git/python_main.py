#Quiz program

class Quiz:
    def __init__(self, question, options, answer):
        self.question = ""
        self.options = ["", "", "", ""]
        self.answer = 1






class Quizgame:
    def __init__(self):
        self.time = 0









def main():
    print("=================================")
    print("=======LEGENDARY_QUIZ_GAME=======")
    print("=================================")

game_going = True

while game_going:
    print("=하실 행동을 선택해 주세요. (숫자키 1~5)=")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 퀴즈 점수 확인")
    print("5. 퀴즈 종료")
    print("================================")

    try:
        choice = int(input("선택: ").strip())

        if choice == 1:
            print("퀴즈를 시작합니다!")


        elif choice == 2:
            print("새로운 퀴즈를 추가합니다.")

        elif choice == 3:
            print("퀴즈 목록을 확인합니다.")

        elif choice == 4:
            print("점수를 확인합니다.")

        elif choice == 5:
            print("퀴즈 게임을 종료합니다.")
            break
        else:
            raise ValueError



    except ValueError:
        print("\n 잘못된 입력입니다.")
        print("\n 알맞은 입력을 다시 해 주세요.")
        continue

    except (KeyboardInterrupt, EOFError):

        print("\n 비정상적 종료시도가 감지되었습니다.")
        print("\n 프로그램을 안전하게 종료합니다.")
        break




if __name__ == "__main__":
    main()