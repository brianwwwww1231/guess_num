# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入去猜
# 猜對的話就印出 “終於猜對了”
# 猜錯的話要告訴他，你猜得比答案大還是小

# i += 1 是 i = i + 1的快寫法

import random

x = 3 # 起迄值嘗試次數
while x > 0:
	x = x - 1
	start = input('請決定隨機數字開始值： ')
	end = input('請決定隨機數字結束值： ')
	if start.isdigit() and end.isdigit():
		start = int(start)
		end = int(end)
		# start 跟 end的input存取的值是「字串」
		# random.randint(x, y)是沒有辦法讀取「字串的」
		# 所以要做casting
		break
	else:
		print('請輸入數值！')
		print('還剩下', x ,'次機會！')
	if x == 0:
		print('只是想來找碴吧？遊戲結束！！！！')
		quit() # 退出程式

ans = random.randint(start,end) 

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
			print('答案介於', start, '到' , guess , '之間')
			if i > 0:
				print('還剩下', i ,'次機會' )
			else:
				print('失敗次數過多，遊戲結束！')
				print('答案是：', ans )
		else:
			print('答案介於', guess , '到', end, '之間')
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