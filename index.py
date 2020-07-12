# 与えられた文字列中にある部分文字列の重複・非重複の回数を求める
# 例）'aa'が文字列'aaa'で2回登場していることを示したい場合
arf = input()
str = input()
count = 0
start = 0
while start < len(str):
    pos = str.find(arf,start)
    if pos != -1:
        start = pos + 1
        count += 1
    else:
        break
print(count)


# 標準入力で入力された2つの値をini型に変換し、2つの変数に代入する
num, init = [int(x) for x in input().split()]

# スライスされたリストのなかでTrueが一度も含まれていない
# スライスは[開始インデックス:対象要素数]
seats = [False, False, False]
init = 1
num = 3
# if True not　in seats[init - 1 : init + num - 1]: # こちらも同じ意味
if not True in seats[init - 1 : init + num - 1]: # Trueが無い時
    # 全てTrueに変換
    seats[init - 1 : init + num - 1] = [True] * num
print(seats)

#標準入力された値から辞書を作成する
num = int(input())
keys = []
values = []
for i in range(num):
    input_line = input().rstrip().split(' ')
    keys.append(int(input_line[1]))
    values.append(input_line[0])
d = dict(zip(keys, values))

# 辞書のキーをソートする、返却値はリスト
# 数字を昇順に並び替えたいときはint型にする必要がある
print(sorted(d)) # returns ['A', 'B', 'C']

# 辞書に代入することでキーと値を追加する
inputs = {}
tmp = input().split()
for i in range(num):
    inputs[tmp[0]] = inputs[tmp[0]] + int(tmp[1])

# 辞書のキーと値を一行ずつ表示する
for (key, value) in inputs.items():
    print(key , value)

# 存在しない云々は存在フラグをつけることで対策できることもある

# アルファベットの何番目かを表示
# 大文字と小文字で返却値が異なるので注意
d = input()
print(ord(d))

# 一番目と二番目のアルファベットの間の範囲に入っているか確認
x = input()
y = input()
c = input()
if ord(c) in range(ord(x), ord(y)):
    print("true")
else:
    print("false")

# 数字を文字型にする
print(str(111)) # returns '111'

# リストで何番目にでてくるか
lis = ['aa', 'bb', 'cc']
print(lis.index('aa')) # returns 0