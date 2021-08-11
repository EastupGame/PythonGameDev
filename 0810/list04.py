t_money = 10000
print("현재잔액 : " + str(t_money)) #문자열로 변환후 출력
print("사용하실 금액 입력:")
use_money = input()
t_money = t_money - int(use_money)  #정수로 변환 후 계산
print("현재잔액 : " + str(t_money))

if t_money <= 2000 :
    print("잔액이 부족하니 충전하세요.")
else:
    print("잔액이 충분합니다.")
