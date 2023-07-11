class BodyCondition:
    # イニシャライザはインスタンス作成時に1回だけ呼ばれる
    def __init__(self, arg_weight, arg_height):
        self.weight = arg_weight
        self.height = arg_height
    
    def bmi_calc(self):
        m_height = self.height / 100
        bmi = self.weight / m_height / m_height
        print(bmi)
        
        
bc = BodyCondition(55, 150)
bc.bmi_calc()