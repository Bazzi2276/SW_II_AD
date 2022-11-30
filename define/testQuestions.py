import unittest

from questions import Question

class TestQuestions(unittest.TestCase):
    
    def setUp(self):
        self.q1 = Question()

    def tearDown(self):
        pass

    def testGetQuestion(self):
        questions = Question.questions
        for i in range(len(questions)):
            self.assertAlmostEqual(self.q1.getQuestion(), questions[i])        

    def testGetQuestionIdx(self):
        questions = Question.questions
        for i in range(len(questions)):
            self.assertAlmostEqual(self.q1.getQuestionIdx(), i)
            self.q1.getQuestion()

if __name__ == '__main__':
    unittest.main()