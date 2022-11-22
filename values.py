import pickle

class Values:
    
    mbtiList = ["ISTJ", "ISTP", "ISFJ", "ISFP", "INTJ", "INTP", "INFJ", "INFP", "ESTJ", "ESTP", "ESFJ", "ESFP","ENTJ", "ENTP", "ENFJ", "ENFP"]
   
    # 매우 그렇다가 E
    # 매우 그렇다가 N
    # 매우 그렇다가 T
    # 매우 그렇다가 J
    
    suitedMBTI = {
        "INTP": ["ENFJ", "ENTJ"],
        "INFP": ["ENFJ", "ENTJ"],
        "ISTJ": ["ESFP", "ESTP"],
        "ISFJ": ["ESFP", "ESTP"],
        "INFJ": ["ENFP", "ENTP"],
        "ENFP": ["INFJ", "INTJ"],
        "ENFJ": ["INFP", "ISFP"],
        "ENTP": ["INFJ", "INTJ"],
        "ENTJ": ["INFP", "INTP"],
        "ESFP": ["ISFJ", "ISTJ"],
        "ESFJ": ["ISFP", "ISTP"],
        "ESTP": ["ISFJ", "ISTJ"],
        "ISFP": ["ENFJ", "ESFJ", "ESTJ"],
        "INTJ": ["ENFP", "ENTP"],
        "ISTP": ["ESFP", "ESTP"],
        "ESTJ": ["ENTJ", "ISFP", "ISTP"]
        }
    
    celebrityMBTI = {
        "차태현": "ISTJ",
        "최강창민": "ISFJ",
        "김종민": "ISTP",
        "유재석": "ISFP",
        "태연": "INFJ",
        "손나은": "INTJ",
        "선미": "INFP",
        "이장원": "INTP",
        "재현": "ESTP",
        "전소민": "ESFP",
        "데프콘": "ESTJ",
        "혜리": "ESFJ",
        "전소미": "ENFP",
        "제시": "ENTP",
        "유나": "ENFJ",
        "스윙스": "ENTJ"
        }
    
    savedMBTI = {}
    savedNumber = {}
    
    def __init__(self):
        for mbti in self.mbtiList:
            self.savedMBTI[mbti] = {"연예인":set([]), "학생":set([])}  

        for name, mbti in self.celebrityMBTI.items():
            self.savedMBTI[mbti]["연예인"].add(name)
            
        try:
            self.studentMBTI = {}
            with open('studentMBTI.txt', 'rb') as f:
                self.studentMBTI = pickle.load(f)
        except FileNotFoundError as f:
            f = open("studentMBTI.txt", 'w')
            f.close()

        try:
            self.studentNumber = {}
            with open('studentNumber.txt', 'rb') as f:
                self.studentNumber = pickle.load(f)
        except FileNotFoundError as f:
            f = open("studentNumber.txt", 'w')
            f.close()
    
        for name, mbti in self.studentMBTI.items():
            self.savedMBTI[mbti]["학생"].add(name)

        for name, number in self.studentNumber.items():
            self.savedNumber[name] = number

    # 매개변수의 MBTI와 잘 어울리는 MBTI들을 리스트로 리턴함
    def findSuitedMBTI(self, mbti):
        return self.suitedMBTI[mbti]

    # 매개변수의 MBTI와 잘 어울리는 연예인들을 딕셔너리로 리턴함
    def findSuitedCelebrity(self, mbti):
        celebrities = {}
        for mbti in self.suitedMBTI[mbti]:
            for name in self.savedMBTI[mbti]["연예인"]:
                celebrities[name] = mbti

        return celebrities

    # 매개변수의 MBTI와 잘 어울리는 학생들을 딕셔너리로 리턴함
    def findSuitedStudent(self, mbti):
        students = {}
        for mbti in self.suitedMBTI[mbti]:
            for name in self.savedMBTI[mbti]["학생"]:
                students[name] = mbti

        return students

    # 학생의 이름을 매개변수로 받아 학번 리턴
    def findStudentNumber(self, name):
        return self.savedNumber[name]

    # 이름, 학번, MBTI를 받아서 파일로 저장
    def saveStudentInfo(self, name, number, mbti):
        self.studentMBTI[name] = mbti
        with open('studentMBTI.txt', 'wb') as f:
            pickle.dump(self.studentMBTI, f)

        self.studentNumber[name] = number
        with open('studentNumber.txt', 'wb') as f:
            pickle.dump(self.studentNumber, f)
    

# 테스트
if __name__ == '__main__':
    values = Values()

    a = {"전현빈":"ISTJ", "김갑수":"ISFJ", "김철수":"ISTJ"}
    with open('studentMBTI.txt', 'wb') as f:
        pickle.dump(a, f)
    b = {"전현빈":'20223134'}
    with open('studentNumber.txt', 'wb') as f:
        pickle.dump(b, f)
    
    print(values.savedMBTI)
    print(values.savedNumber)
    print()
    print(values.findSuitedCelebrity("ISTJ"))
    print(values.findSuitedStudent("ESFP"))