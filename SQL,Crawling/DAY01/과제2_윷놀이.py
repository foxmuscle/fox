'''흥부와 놀부가 윷놀이를 하는데, 각자 4개의 윷가락을 교대로 던져서 20점 이상의 점수가 먼저 나오는
사람이 승리를 한다. 윷가락을 던져 나온 점수가 "윷(4점)"이나 "모(5점)"가 나오는 경우, 동일한 사람
이 한 번 더 던질 수 있다. 아래 주어진 메소드를 구현하고 필요한 기능들은 추가로 구현하여 프로그
램을 작성하시오.'''


'''구현 내용
 윷가락은 4개의 값을 저장할 수 있도록 sticks=	[0,	0,	0,	0] 형태로 구현
 윷을 던질 때 마다 랜덤하게 0,	1	사이의 값을 생성해서 sticks[]에 저장하고 점수를 계산
          함(예:	sticks[i]	=	random.randint(0,	1))
 한 명의 점수가 먼저 20점 이상이면 게임은 바로 종료
 ‘모’나 ‘윷’이 나온 경우, 이미 총 점수가 20점 이상이면 한 번 더 던지지 않음
 경기 시작은 어느 누구나 상관없음
 게임이 종료되면 승패 결과를 화면에 출력하고 프로그램 종료'''




import random

def yutnori():
    sticks = [random.randint(0, 1) for _ in range(4)]
    count = sticks.count(1)
    score = 0
    #   도 개 걸 윳 모  점수
    if count ==4 :
        score = 5
    elif count == 0 :
       score = 4  
    elif count == 3:
        score = 3 
    elif count == 2:
        score = 2  
    else:
        score = 1 


    return score

def yutnori_game() :
    #점수 더할 곳 
    #흥부
    player1_score =0
    #놀부
    player2_score = 0
    player_turn = 1

  #20점 이상 될때까지  반복
    while player1_score < 20 and player2_score < 20:
        if player_turn == 1:
            print("흥부의 차례입니다.")
            score =yutnori()
            player1_score += score
            print(f"흥부의 점수: {score} (총 {player1_score}점)")
            if score >= 4 and player1_score < 20:
                continue              
            player_turn = 2 
                #놀부 차례
        else:
            print("놀부의 차례입니다.")
            score = yutnori()
            player2_score += score
            print(f"놀부의 점수: {score} (총 {player2_score}점)")
            if score >= 4 and player2_score < 20:
                continue  
            # 모 윷 한번 더 던져
            player_turn = 1  

    if player1_score >= 20:
        print("흥부가 승리했습니다!!!")
    else:
        print("놀부가 승리했습니다!!!")

if __name__ == "__main__":
    yutnori_game()