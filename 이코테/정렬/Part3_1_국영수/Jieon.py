n=int(input())
score_dic=[]
for _ in range(n):
    name,kor,eng,math=map(str,input().split())
    score_dic.append({'name':name, 'kor':int(kor), 'eng':int(eng), 'math':int(math)})

answer=sorted(score_dic,key=lambda x: (-x['kor'],x['eng'],-x['math'],x['name']))
for i in range(n):
    print(answer[i]['name'])

#답지안봄
#딕셔너리를 이용했더니 코드가 보기 편하고, 구현하기도 좋았다.
#파이썬을 쓰는 이유를 너무 잘 알겠다..ㅋㅋ 구현하기 너무 좋은 언어인 듯. java나 c를 썼다면? 끔찍