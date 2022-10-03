scores = input("5개의 성적을 입력하세요(각 값은 공백으로 분리): ")

scores = scores.split(" ")
for i in range(5):
	scores[i] = int(scores[i])
print(sorted(scores)) 
