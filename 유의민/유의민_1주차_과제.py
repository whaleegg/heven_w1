import random
from collections import Counter

class Dicegame:
    def __init__(self):
        self.N = int(input())

        while (self.N <= 10 or self.N >= 50):
            print("조건에 맞지 않습니다. 다시 입력하세요.")
            self.N = int(input())
        
        self.dice_num = [0, 0, 0, 0, 0, 0]



    # random 라이브러리를 활용해서 주사위를 N번 굴려 결과값(각각의 수가 몇번 나왔는지)을 저장하는 함수
    def roll_dice(self):
        dice_results = []

        for i in range(self.N):
            dice = random.randint(1,6)
            dice_results.append(dice)

        self.dice_num = [dice_results.count(num) for num in range(1, 7)]
        
        # print(self.dice_num)
        
        # print(set(self.dice_num))



    # 1. 저장된 결과값들 2. 두번째로 많이 나온 주사위 수 를 print하는 함수
    def print_result(self):
        
        # 1. 결과값(각각의 수가 몇번 나왔는지)을 모두 print하는 코드
        for num, count in enumerate(self.dice_num, start=1):
            print(f'Dice number {num} : {count}')

        # 2. 두번째로 많이 나온 주사위 수를 print하는 코드
        if len(set(self.dice_num)) > 1:
            most_common_count = max(self.dice_num)
            most_common_indices = [i + 1 for i, count in enumerate(self.dice_num) if count == most_common_count]

            # 모든 가장 많이 나온 수의 횟수를 0으로 변경
            for index in most_common_indices:
                self.dice_num[index - 1] = 0

            # 두 번째로 많이 나온 수를 찾아서 출력
            second_most_common_count = max(self.dice_num)
            second_most_common_indices = [i + 1 for i, count in enumerate(self.dice_num) if count == second_most_common_count]
            
            for n, dice in enumerate(second_most_common_indices):
                print(f'Second most common dice numbers: {dice}')



if __name__ == "__main__":
    dice_game = Dicegame()
    dice_game.roll_dice()
    dice_game.print_result()
