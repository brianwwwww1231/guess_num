# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入去猜
# 猜對的話就印出 “終於猜對了”
# 猜錯的話要告訴他，你猜得比答案大還是小

import random

ans = random.randint(1,10)

i = 3 # i = 剩餘嘗試次數

while i > 0:
	i = i - 1
	guess = input('請猜一個數字： ')
	if guess.isdigit():
		guess = int(guess)
		if guess == ans:
			print('終於猜對了')
			break
		elif guess > ans:
			print('答案是 1 到' , guess , '之間')
			if i > 0:
				print('還剩下', i ,'次機會' )
			else:
				print('失敗次數過多，遊戲結束！')
				print('答案是：', ans )
		else:
			print('答案是', guess , '到 10 之間')
			if i > 0:
				print('還剩下', i ,'次機會' )
			else:
				print('失敗次數過多，遊戲結束！')
				print('答案是：', ans )
	else:
		if i > 0:
			print('輸入錯誤！請輸入數字')
			print('還剩下', i ,'次機會' )
		else:
			print('存心找碴？？？ 遊戲結束！')