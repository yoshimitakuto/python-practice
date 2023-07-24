import random
import ipywidgets as wid

# ボタン押下処理
def on_click_button(b):
    birthvalue = birthdate.value
    constella = calc_constellation(birthvalue)
    print(f'今日の{constella}の運勢は、{result}')


# 入力された誕生日と星座を判定する処理
def calc_constellation(x):
    constellation = {1:'やぎ座', 2:'みずがめ座', 3:'うお座', 4:'おひつじ座', 5:'おうし座', 6:'ふたご座',
                     7:'かに座', 8:'しし座', 9:'おとめ座', 10:'てんびん座', 11:'さそり座', 12:'いて座'}
    
    if x.date > 22:
        if x.month == 12:
            return constellation(1)
        else:
            return constellation(x.month + 1)
    else:
        return constellation(x.month)
    
# 誕生日入力フォーム
birthdate = wid.DatePicker()

button = wid.Button(description = '占う')
button.on_click(on_click_button)

print('誕生日を入力してください')
print(birthdate)
print(button)


# 結果の処理
fortune = ["超絶ラッキー！", "外にでランニングしよ", "飯食って寝た方がいいよ", "大人しくしときな", "超絶アンラッキー！"]
result = random.choice(fortune)
