# 進捗エンゲージを表すもの
# from tqdm import tqdm

# for _x in tqdm(range(10 ** 9)):
#     # passは何も処理をしない時に記述する
#     pass

# zipについて
# 複数の繰り返しオブジェクトから１つずつ順番に要素を取り出し1まとめにする。
# あるいは比較する際に使用する。
sales_2023 = [400239, 560213, 542490, 999999]
sales_2022 = [489828, 400123, 442489] 

for current, previors in zip(sales_2023, sales_2022):
    result = (current / previors - 1) * 100
    print(f'{result:.1f}%')
    
# enumerateについて
# 値が徐々に大きくなる時に使用    
names = ['鈴木', '斉藤', '大河']
for i, n in enumerate(names, start=1):
    print(f'{i}位：{n}')    