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

