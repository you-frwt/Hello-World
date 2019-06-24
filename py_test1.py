import random
import datetime
import sys	# コマンドライン引数

############################################################
### 変数・型（リスト・辞書・タブル・セット型など）
############################################################

##### 算術演算子 #####
a = 7
b = 3
print(a / b)    # 算数的な割り算
print(a // b)   # 整数除算(C言語の「/」の意味)
print(a ** b)   # 「**」はべき乗

##### じゃんけんプログラム #####
data = ['グー', 'チョキ', 'パー']	# []はリスト型を示す
print('じゃんけん … %s !!' % random.choice(data))
print(data[0])
print(data[-1])		# 添え字-1は配列の最後を示す(マイナスは右からの取り出し)
print(len(data))	# リストのlenはリストの要素数
print('------')		# 改行

##### 文字列 #####
moji = 'Tokyo,Japan'
print(moji)
print(moji[0])
print(moji[2])
print(len(moji))
print(moji[6:11])		# [開始idx：終了idx](開始idx～終了idx-1までの文字を取り出す)
print(moji.split(','))
print(moji.split('o'))
print(moji.index('y'))
print(moji.index('o'))
oomoji = moji.upper()	# 大文字変換
print(oomoji)
print('------')		# 改行

##### 日付と時刻 #####
day = datetime.date(2020,5,20)
print(day)
print(datetime.date.today())
print(datetime.datetime.now())

##### 何日生きたか計算するプログラム #####
today		= datetime.date.today()
birthday	= datetime.date(1975,5,20)
life		= today - birthday
print('あなたが生まれてから%d日目です。' % life.days)
print('------')		# 改行

##### リスト型 #####
list_1 = [0, 1, 2, 3]
list_2 = [2, 1.72, 'test']	# 整数/小数/文字列の混在もOK
list_1.append(4)			# appendは末尾に追加
list_1.insert(1,5)			# insert(インデックス, 要素)
print(list_1)
print(list_2)
list_1.pop(1)
print(list_1)

list_mix = list_1 + list_2	# リスト同士の足し算(連結)
print(list_mix)

list_3 = [5,2,8,1,7,3,6]
list_3.sort()
print(list_3)

list_enpty = []
print(list_enpty)
list_enpty.append('apple')
list_enpty.append('orange')
print(list_enpty)
print('------')		# 改行

##### リストの内包表記(集合や辞書も使える) #####
fizz = [x for x in range(1,10)]     # 内包表記(リストの中に制御文が埋め込める)
print(fizz)
fizz = [x for x in range(1,10) if x % 3 != 0]   # 内包表記の中にif文も書ける
print(fizz)


##### 辞書型 #####
country_code = {1:'America', 39:'Italia', 86:'China'}
print(country_code[39])
print(39 in country_code)
country_code[81] = 'Japan'
print(country_code)

for key in country_code:    # for文に辞書を使うと、キーの一覧が取り出せる
    print( key, country_code[key])

for key, val in country_code.items():   # items()はキーと値のペアをタプルで取り出せる
    print( key, val)
    
country_code.pop(81)	# 値の削除
print(country_code)

print('------')		# 改行

##### タプル型(要素の追加・削除ができないリスト) #####
tuple_1 = (1,2,3,'100yen')
print(tuple_1)
print(tuple_1[3])
print('------')		# 改行

##### セット型(単純なデータの集まり(集合ともいう)、順不同、同じ値は2つ以上入らない) #####
set_test = set()
print(set_test)
set_test.add(1)
set_test.add(2)
set_test.add(3)
print(set_test)
set_test.add(3)
print(set_test)
print('------')		# 改行

##### 単語並べ替えプログラム #####
list_input = sys.argv[1:]	# スライスを使って要素1～取得
list_input.sort()
print(list_input)


