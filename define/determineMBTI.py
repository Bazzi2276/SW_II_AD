class DetermineMBTI:

    def __init__(self):
        self.sum1 = 0   #E,I
        self.sum2 = 0   #N,S
        self.sum3 = 0   #T,F
        self.sum4 = 0   #P,J
        self.mbti = ""

    def mbtiSum(self, index, amount):
        if(index % 4 == 0):
            self.sum1 += amount
        elif(index % 4 == 1):
            self.sum2 += amount
        elif(index % 4 == 2):
            self.sum3 += amount
        else:
            self.sum4 += amount


    def mbtiCalc(self):
        if(self.sum1 > 26):
            self.mbti += "E"
        else:
            self.mbti += "I"

        if(self.sum2 > 26):
            self.mbti += "N"
        else:
            self.mbti +="S"

        if(self.sum3 > 26):
            self.mbti += "T"
        else:
            self.mbti += "F"

        if(self.sum4 > 26):
            self.mbti += "J"
        else:
            self.mbti += "P"

        return self.mbti



