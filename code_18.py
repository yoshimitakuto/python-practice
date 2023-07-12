def total_price_1item(unit_price, quantity = 1):
    total_price = unit_price * quantity
    return total_price

total_price = total_price_1item(120)
print(total_price)
total_price2 = total_price_1item(quantity=20, unit_price=130)
print(total_price2)


# あえてエラー(デフォルト値設定した以降の値もデフォルト値を設定する必要がある)
# def total_price_2item(quantity1 = 1, unit_price1):
#     total_price1 = unit_price1 * quantity1
#     return total_price1

# total_price1 = total_price_2item(120)
# print(total_price1)


# タイプアノテーション
# あくまで注釈として使うものであるため他のstr等の値が入ってもエラーにはならない
def total_price_2item(unit_price1:int, quantity1:int) -> int:
    total_price1 = unit_price1 * quantity1
    return total_price1

total_price1 = total_price_2item(130, 3)
print(total_price1)

# 戻り値で文字列型へ変換して表示するため str であることをタイプアノテーションで記述している
def total_price_3item(unit_price2:int, quantity2:int = 1) -> str:
    total_price3 = unit_price2 * quantity2
    return f'￥{total_price3:,}'

total_price3 = total_price_3item(1300)
print(total_price3)