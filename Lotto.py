import random

class Lotto():
    """
    [Lotto Class]
    Author : 송재관
    Role : ex) 로또 번호를 입력받아서 출력하는 기말고사 과제
    """
    def __init__(self) -> None:
        self.name = input("이름을 입력해 주세요.")
        self.code = int(input("학번을 입력해주세요."))
        self.info()


    def info(self):
        print(f"{self.code} 학번 {self.name} 레포트 입니다.")

    @classmethod    
    def guess_lotto(self):
        count = 1
        print("로또번호를 선택하세요.")
        guess_lotto = []
        # 로또 번호 validation 
        while True:
            guess_num = int(input(f"{count}번 "))
            if guess_num in guess_lotto:
                print("중복된 숫자는 입력하지 마세요.")
                continue

            elif not(0 < guess_num <46):
                print("범위에 맞는 숫자를 입력해 주세요.")
                continue
            
            elif 0 < guess_num <46:
                guess_lotto.append(guess_num)
                count += 1

            elif len(guess_lotto) == 5:
                break
        print(f"귀하의 선택은 {', '.join(map(str, guess_lotto))} 입니다.")
        return guess_lotto


        
    @classmethod
    def create_lotto(self):
        lotto = []
        while True:
            num = random.randint(1, 45)
            if num not in lotto:
                lotto.append(num)

            if len(lotto) == 5:
                break
        print(f"이번 차수 로또 당첨번호는 {', '.join(map(str, lotto))} 입니다.")
        return lotto

    def check(self):
        guess = Lotto.guess_lotto()
        real = Lotto.create_lotto() #6개의 로또 당첨번호 생성
        hit = [i for i in guess if i in real]
        score = [0, 0, 3, 2, 1]
        if len(hit) <= 2:
            print("안탑깝게 꽝 되셨네요.")
        else:
            print(f"{', '.join(map(str, hit))} 가 맞아 {score[len(hit)]}등 당첨 되었습니다.")       



jaekwan = Lotto() #인스턴스 생성
jaekwan.check() #등수 확인
