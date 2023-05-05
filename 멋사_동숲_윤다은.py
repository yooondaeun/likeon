import time
import random

print("""
  ___          _                    _   _____                         _               
 / _ \        (_)                  | | /  __ \                       (_)              
/ /_\ \ _ __   _  _ __ ___    __ _ | | | /  \/ _ __   ___   ___  ___  _  _ __    __ _ 
|  _  || '_ \ | || '_ ` _ \  / _` || | | |    | '__| / _ \ / __|/ __|| || '_ \  / _` |
| | | || | | || || | | | | || (_| || | | \__/\| |   | (_) |\__ \\__ \| || | | || (_| |
\_| |_/|_| |_||_||_| |_| |_| \__,_||_|  \____/|_|    \___/ |___/|___/|_||_| |_| \__, |
                                                                                 __/ |
                                                                                |___/ 
""")
print("~ 모여봐요 멋사의 숲 ~\n")

name = input("이름을 입력해주세요! ")
island = input("섬의 이름을 입력해주세요!")

print(name + "님 반가워요! " + island + "섬에 오신것을 환영합니다-!")
time.sleep(1)

animal = {'릴리안': 0, '탁호': 0, '미첼': 0, '리처드': 0}
my_bell = 3000
my_pocket = []
store = {'가습기': 1400, '강아지 인형': 2400, '강의실 책상': 2500, '몬스테라': 1700}

action_boolean = 1

# 4가지 반복하기
while action_boolean:
    print("\n어떤 것을 해볼까요?")
    answer_action = input("0. 종료 1. 상점가기 2. 주민 찾아가기 3. 나무 흔들기 4. 정보 확인하기 ")
    
    # 0. 게임 종료
    if answer_action == "0":
        print("게임을 종료합니다. 또 만나요~")


    # 1. 상점가기를 선택한경우
    elif answer_action == "1":
        print("\n반갑다구리~ ")

        print("동숲 상점에는 이런 물건들이 있다구리! ")
        print("1. 가습기: 1400벨")
        print("2. 강아지 인형: 2400벨")
        print("3. 강의실 책상: 2500벨")
        print("4. 몬스테라: 1700벨")

        answer_store = input("\n물건을 골라봐구리~ ")
        #1-1. 가습기 선택
        if answer_store == "1":
            if my_bell >= store['가습기']:
                my_bell = my_bell - store['가습기']
                my_pocket.append('가습기')
                print("가습기를 구매하였습니다.")
                print("남은 벨: " + str(my_bell))
            else:
                print("벨이 부족합니다.")
        #강아지 인형 선택
        if answer_store == "2":
            if my_bell >= store['강아지 인형']:
                my_bell = my_bell - store['강아지 인형']
                my_pocket.append('강아지 인형')
                print(" 구매하였습니다.")
                print("남은 벨: " + str(my_bell))
            else:
                print("벨이 부족합니다.")
        #강의실 책상 선택
        if answer_store == "3":
            if my_bell >= store['강의실 책상']:
                my_bell = my_bell - store['강의실 책상']
                my_pocket.append('강의실 책상')
                print(" 구매하였습니다.")
                print("남은 벨: " + str(my_bell))
            else:
                print("벨이 부족합니다.")
        #몬스테라 선택
        if answer_store == "4":
            if my_bell >= store['몬스테라']:
                my_bell = my_bell - store['몬스테라']
                my_pocket.append('몬스테라')
                print(" 구매하였습니다.")
                print("남은 벨: " + str(my_bell))
            else:
                print("벨이 부족합니다.")


    # 2. 주민 찾아가기를 선택한 경우
    elif answer_action == "2":
        time.sleep(0.5)
        print("우리마을에 있는 주민이다구리! ")
        print("1.릴리안 2.탁호 3.미첼 4.리처드")

        answer_animal = input("어떤 주민을 찾아가겠습니까?")
        if answer_animal == "1":
            print("릴리안에게 무엇을 할까?")
        elif answer_animal == "2":
            print("탁호에게 무엇을 할까?")
        elif answer_animal == "3":
            print("미첼에게 무엇을 할까?")
        elif answer_animal == "4":
            print("리처드에게 무엇을 할까?")

        answer_animal_action= int(input("1. 말걸기 2. 선물하기 3. 때리기 "))
        time.sleep(0.6)

        # 2-1. 말걸기를 선택한경우
        if answer_animal_action == 1:
            #릴리안 말버릇: 그렇지 뭐
            if answer_animal == "1": 
                animal["릴리안"] += 1
                print("어머" + name + "왔구나~ 반가워!")
                print("어제는 어찌나 벚꽃이 이쁘던지 기분이 참 좋더라니까")
                print(name + "도 놀러다녀오는 건 어때? 그렇지 뭐")
                print("릴리안 친밀도 +1")
            #탁호 말버릇: 약히
            elif answer_animal == "2":
                animal["탁호"] += 1
                print("안녀엉~ " + name + "아~ 반가워어~")
                print("오늘 저녁은 뭘 먹을지 너무 고민이 돼~ 약히")
                print("탁호 친밀도 +1")
            #미첼 말버릇: 동글
            elif answer_animal == "3":
                animal["미첼"] += 1
                print(name + "아~! 반가워! 오늘 날씨 되게 좋지않아?")
                print("마구마구 산책을 하고 싶어져 동글")
                print("미첼 친밀도 +1")
            #리처드 말버릇: 그래유
            elif answer_animal == "4":
                animal["리처드"] += 1
                print(name+ "야아~")
                print("나무를 흔들었더니 100벨이 나왔어어~")
                print(name+"도 한 번 흔들어봐아~ 그래유")
                print("리처드 친밀도 +1")

        # 2-2. 선물하기를 선택한 경우
        elif answer_animal_action == 2:
            print("주민에게 선물을 합니다. 어떤 선물을 할까요?")
            print("1. 가습기 2.강아지 인형 3.강의실 책상 4.몬스테라")
            answer_gift = input("선물을 입력해주세요: ")
            #릴리안
            if answer_animal == "1":     
                #if my_pocket[answer_gift] >= 1 :
                    #my_pocket[answer_gift] -= 1
                    animal["릴리안"] += 5
                    print("어머! " + name + "아 선물 고마워~ 그렇지 뭐")
                    print("릴리안 친밀도 +5")
                #else:
                    #print("선물이 부족합니다.")
            #탁호
            elif answer_animal == "2":
                #if my_pocket[answer_gift] >= 1 :
                    #my_pocket[answer_gift] -= 1
                    animal["탁호"] += 5
                    print(name + "아~ 선물 고마워~ 약히")
                    print("탁호 친밀도 +5")
                #else:
                    #print("선물이 부족합니다.")
            #미첼
            elif answer_animal == "3":
                #if my_pocket[answer_gift] >= 1 :
                    #my_pocket[answer_gift] -= 1
                    animal["미첼"] += 5
                    print(name + "아~! 선물 고마워 동글")
                    print("미첼 친밀도 +5")
                #else:
                    #print("선물이 부족합니다.")
            #리처드
            elif answer_animal == "4":
                #if my_pocket[answer_gift] >= 1 :
                    #my_pocket[answer_gift] -= 1
                    animal["리처드"] += 5
                    print(name+ "야아~ 선물 고마워~ 그래유")
                    print("리처드 친밀도 +5")
                #else:
                    #print("선물이 부족합니다.")



        # 2-3. 때리기를 선택한 경우
        elif answer_animal_action == 3:
            print("주민을 때립니다. 어떤 주민을 때리겠습니까?")
            print("1. 릴리안 2. 탁호 3. 미첼 4. 리처드")
            answer_animal = input("주민을 입력해주세요: ")
            #릴리안
            if answer_animal == "1":
                animal["릴리안"] -= 1
                print("뭐 하는 거야!"+ name +"!")
                print("릴리안 친밀도 -1")
            #탁호
            elif answer_animal == "2":
                animal["탁호"] -= 1
                print("뭐 하는 거야!"+ name +"!")
                print("탁호 친밀도 -1")
            #미첼
            elif answer_animal == "3":
                animal["미첼"] -= 1
                print("뭐 하는 거야!"+ name +"!")
                print("미첼 친밀도 -1")
            #리처드
            elif answer_animal == "4":
                animal["리처드"] -= 1
                print("뭐 하는 거야!"+ name +"!")
                print("리처드 친밀도 -1")

        else:
            print("잘못된 입력입니다. 다시 입력 해주세요")




    # 3. 나무 흔들기를 선택한 경우
    elif answer_action == "3":
        print("나무를 흔듭니다.")
        time.sleep(1)
        result = random.choice(["100벨" , "사과", "벌"])

        # 100벨이 떨어질경우
        if result == "100벨":
            print("앗, ", result, "이 떨어졌다!")
            my_bell += 100
            time.sleep(1)
            print("100벨을 얻었습니다!")
            print("남은벨: " + str(my_bell))

        # 사과가 떨어질경우
        elif result == "사과":
            print("앗, ", result, "가 떨어졌다!")
            time.sleep(1)
            my_pocket.append("사과")
            print("사과를 얻었습니다!")

        # 벌이 나타날경우
        elif result == "벌":
            print("응...?")
            time.sleep(1)
            print("벌이 나타났습니다!")
            time.sleep(1)
            print("아야.. 벌에게 물렸어")
            time.sleep(1)




    # 4. 정보보기를 선택한 경우
    elif answer_action == "4":
        print("\n내 정보")
        time.sleep(0.6)

        # 이름 출력
        print("이름: " , name)
        time.sleep(0.6)

        # 남은 벨 출력
        print("남은 벨: " , my_bell)

        # 주머니 출력
        if len(my_pocket) ==0:
            print("내 주머니 : 비어있습니다.")
        else:
            print("주머니: " , my_pocket )
        time.sleep(0.6)

        # 주민 친밀도 출력
        print("주민 친밀도: " )
        i = 1
        for key, value in animal.items():
            print(str(i) + ". " + str(key) + ": " + str(value))
            i += 1
            time.sleep(0.6)
        time.sleep(1)
        
        
        
    # 잘못된 입력을 했을경우
    else:
        print("잘못된 입력입니다.")
