import unittest
from values import Values

class TestValues(unittest.TestCase):

    def setUp(self):
        self.v1 = Values()

    def tearDown(self):
        pass

    def testFindSuitedMBTI(self):
        self.assertEqual(self.v1.findSuitedMBTI("ISTJ"), ["ESFP", "ESTP"])

    def testFindSuitedCelebrity(self):
        self.assertEqual(self.v1.findSuitedCelebrity("ISTJ"), {"전소민":"ESFP", "정일훈":"ESTP"})

    def testFindSuitedStudent(self):
        self.assertEqual(self.v1.findSuitedStudent("ISTJ"), {"전현육":"ESTP"})

    def testFindStudentNumber(self):
        self.assertEqual(self.v1.findStudentNumber("전현빈"), "20223134")


if __name__ == '__main__':
    unittest.main()