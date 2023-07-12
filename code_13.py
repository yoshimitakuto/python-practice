"""
【継承とは？】

基底クラスの性質を（親クラス・スーパークラス）
派生クラスが引き継ぐ（子クラス・サブクラス）

【継承の書き方】
基本：親クラス継承
class HumanClass:
    pass
    
class WizardClass(HumanClass):
    pass    


例1: メソッドの呼び出し
class HumanClass:
    def defend(self):
        print('~~~~')
        
class WizardClass(HumanClass):
    def xxxxxxx(self):
       self.defend() 親クラスのdefendを呼び出す。
       
例2: インスタンスから呼び出し
class HumanClass:
    def defend(self):
        print('~~~~')
        
class WizardClass(HumanClass):
    pass
wc = WizardClass()
wc.defend() 親クラスを継承しているクラスであればインスタンスからも呼び出せる                   

例3: 変数呼び出し（インスタンス作成から変数呼び出しも可能）
class HumanClass:
    def defend(self):
        self.hp = 100
        
class WizardClass(HumanClass):
    def xxxxxxx(self):
       self.hp 変数も呼び出せる


注意: イニシャライザ（派生クラスにイニシャライザを設定していなければ派生クラスのインスタンス生成時に規定クラスのイニシャライザが呼び出される。）
class HumanClass:
    def __init__(self):
        self.hp == 100
        
class WizardClass(HumanClass):
    def __init__(self):
       super().__init__() イニシャライザの場合は「super()」を使用する


オーバーライドの書き方（規定クラスのメソッドを派生クラスで上書き）
class HumanClass:
    def defend(self):
        print('防御しました')
        
class WizardClass(HumanClass):
    def defend(self):
        print('魔法で防御しました')
        
多重継承
class WizardClass:
    pass

class SwordFighterClass:
    pass
    
class MagicSwordFighterClass(
        先に書いたクラスの方が優先される。
        WizardClass, SwordFighterClass): 
      def __init__(self)
          super().__init__()             
"""

class HumanClass:
    def __init__(self):
        print('HumanClassのinit')
        self.hp = 100
        
        
class WizardClass(HumanClass):
    def __init__(self):
        super().__init__()
        self.mp = 50
        
    def output_info(self):
        print(f'現在のHPは{self.hp}で、'
              f'MPは{self.mp}です。')    


wizard = WizardClass()
print(wizard.mp)
wizard.output_info()


# イニシャライザ（先に指定したクラスのメソッドが呼び出される）
class WizardClass2:
    def __init__(self):
        print('WizardClass2のinit')
        
class SwordFighterClass:
    def __init__(self):
        print('SwordFighterClassのinit')
        
class MagicSwordFighterClass(WizardClass2, 
                             SwordFighterClass):
    pass

msf = MagicSwordFighterClass()  




class WizardClass3:
    def __init__(self):
        self.mp2 = 100
        print('WizardClass2のinit')
    
    def cast_spell(self):
        print('呪文を唱える')    
        
class SwordFighterClass2:
    def attack_with_sword(self):
        print('剣で攻撃をする')
        
class MagicSwordFighterClass2(WizardClass3, 
                             SwordFighterClass2):
    pass

msf = MagicSwordFighterClass2()  
msf.cast_spell()
msf.attack_with_sword()
        