import unittest
from determineMBTI import DetermineMBTI

class TestdetermineMBTI(unittest.TestCase):

    def setUp(self):
        self.mbti_ISTJ = DetermineMBTI()    #0,0,48,48
        self.mbti_ISFJ = DetermineMBTI()  # 0,0,0,48
        self.mbti_ESTJ = DetermineMBTI()  # 48,0,48,48
        self.mbti_ESFJ = DetermineMBTI()  # 48,0,0,48
        self.mbti_ISTP = DetermineMBTI()  # 0,0,48,0
        self.mbti_ISFP = DetermineMBTI()  # 0,0,0,0
        self.mbti_ESFP = DetermineMBTI()  # 48,0,0,0
        self.mbti_ESTP = DetermineMBTI()  # 48,0,48,0
        self.mbti_INFJ = DetermineMBTI()  # 0,48,0,48
        self.mbti_INFP = DetermineMBTI()  # 0,48,0,0
        self.mbti_ENFP = DetermineMBTI()  # 48,48,0,0
        self.mbti_ENFJ = DetermineMBTI()  # 48,48,0,48
        self.mbti_INTJ = DetermineMBTI()  # 0,48,48,48
        self.mbti_INTP = DetermineMBTI()  # 0,48,48,0
        self.mbti_ENTP = DetermineMBTI()  # 48,48,48,0
        self.mbti_ENTJ = DetermineMBTI()  # 48,48,48,48

        for i in range(48):
            if i % 4 == 0:
                self.mbti_ISTJ.mbtiSum(i, 0)
                self.mbti_ISFJ.mbtiSum(i, 0)
                self.mbti_ESTJ.mbtiSum(i, 4)
                self.mbti_ESFJ.mbtiSum(i, 4)
                self.mbti_ISTP.mbtiSum(i, 0)
                self.mbti_ISFP.mbtiSum(i, 0)
                self.mbti_ESFP.mbtiSum(i, 4)
                self.mbti_ESTP.mbtiSum(i, 4)
                self.mbti_INFJ.mbtiSum(i, 0)
                self.mbti_INFP.mbtiSum(i, 0)
                self.mbti_ENFP.mbtiSum(i, 4)
                self.mbti_ENFJ.mbtiSum(i, 4)
                self.mbti_INTJ.mbtiSum(i, 0)
                self.mbti_INTP.mbtiSum(i, 0)
                self.mbti_ENTP.mbtiSum(i, 4)
                self.mbti_ENTJ.mbtiSum(i, 4)
            elif i % 4 == 1:
                self.mbti_ISTJ.mbtiSum(i, 0)
                self.mbti_ISFJ.mbtiSum(i, 0)
                self.mbti_ESTJ.mbtiSum(i, 0)
                self.mbti_ESFJ.mbtiSum(i, 0)
                self.mbti_ISTP.mbtiSum(i, 0)
                self.mbti_ISFP.mbtiSum(i, 0)
                self.mbti_ESFP.mbtiSum(i, 0)
                self.mbti_ESTP.mbtiSum(i, 0)
                self.mbti_INFJ.mbtiSum(i, 4)
                self.mbti_INFP.mbtiSum(i, 4)
                self.mbti_ENFP.mbtiSum(i, 4)
                self.mbti_ENFJ.mbtiSum(i, 4)
                self.mbti_INTJ.mbtiSum(i, 4)
                self.mbti_INTP.mbtiSum(i, 4)
                self.mbti_ENTP.mbtiSum(i, 4)
                self.mbti_ENTJ.mbtiSum(i, 4)
            elif i % 4 == 2:
                self.mbti_ISTJ.mbtiSum(i, 4)
                self.mbti_ISFJ.mbtiSum(i, 0)
                self.mbti_ESTJ.mbtiSum(i, 4)
                self.mbti_ESFJ.mbtiSum(i, 0)
                self.mbti_ISTP.mbtiSum(i, 4)
                self.mbti_ISFP.mbtiSum(i, 0)
                self.mbti_ESFP.mbtiSum(i, 0)
                self.mbti_ESTP.mbtiSum(i, 4)
                self.mbti_INFJ.mbtiSum(i, 0)
                self.mbti_INFP.mbtiSum(i, 0)
                self.mbti_ENFP.mbtiSum(i, 0)
                self.mbti_ENFJ.mbtiSum(i, 0)
                self.mbti_INTJ.mbtiSum(i, 4)
                self.mbti_INTP.mbtiSum(i, 4)
                self.mbti_ENTP.mbtiSum(i, 4)
                self.mbti_ENTJ.mbtiSum(i, 4)
            else:
                self.mbti_ISTJ.mbtiSum(i, 4)
                self.mbti_ISFJ.mbtiSum(i, 4)
                self.mbti_ESTJ.mbtiSum(i, 4)
                self.mbti_ESFJ.mbtiSum(i, 4)
                self.mbti_ISTP.mbtiSum(i, 0)
                self.mbti_ISFP.mbtiSum(i, 0)
                self.mbti_ESFP.mbtiSum(i, 0)
                self.mbti_ESTP.mbtiSum(i, 0)
                self.mbti_INFJ.mbtiSum(i, 4)
                self.mbti_INFP.mbtiSum(i, 0)
                self.mbti_ENFP.mbtiSum(i, 0)
                self.mbti_ENFJ.mbtiSum(i, 4)
                self.mbti_INTJ.mbtiSum(i, 4)
                self.mbti_INTP.mbtiSum(i, 0)
                self.mbti_ENTP.mbtiSum(i, 0)
                self.mbti_ENTJ.mbtiSum(i, 4)

    def test_mbtiSum(self):
        #1.ISTJ test
        self.assertLessEqual(self.mbti_ISTJ.sum1, 24)
        self.assertLessEqual(self.mbti_ISTJ.sum2, 24)
        self.assertGreater(self.mbti_ISTJ.sum3, 24)
        self.assertGreater(self.mbti_ISTJ.sum4, 24)

        #2.ISFJ test
        self.assertLessEqual(self.mbti_ISFJ.sum1, 24)
        self.assertLessEqual(self.mbti_ISFJ.sum2, 24)
        self.assertLessEqual(self.mbti_ISFJ.sum3, 24)
        self.assertGreater(self.mbti_ISFJ.sum4, 24)

        #3.ESTJ test # 48,0,48,48
        self.assertGreater(self.mbti_ESTJ.sum1, 24)
        self.assertLessEqual(self.mbti_ESTJ.sum2, 24)
        self.assertGreater(self.mbti_ESTJ.sum3, 24)
        self.assertGreater(self.mbti_ESTJ.sum4, 24)

        #4.ESFJ test  # 48,0,0,48
        self.assertGreater(self.mbti_ESFJ.sum1, 24)
        self.assertLessEqual(self.mbti_ESFJ.sum2,24)
        self.assertLessEqual(self.mbti_ESFJ.sum3, 24)
        self.assertGreater(self.mbti_ESFJ.sum4, 24)

        #5.ISTP test  # 0,0,48,0
        self.assertLessEqual(self.mbti_ISTP.sum1, 24)
        self.assertLessEqual(self.mbti_ISTP.sum2, 24)
        self.assertGreater(self.mbti_ISTP.sum3, 24)
        self.assertLessEqual(self.mbti_ISTP.sum4, 24)

        #6.ISFP test  # 0,0,0,0
        self.assertLessEqual(self.mbti_ISFP.sum1, 24)
        self.assertLessEqual(self.mbti_ISFP.sum2, 24)
        self.assertLessEqual(self.mbti_ISFP.sum3, 24)
        self.assertLessEqual(self.mbti_ISFP.sum4, 24)

        #7.ESFP test  # 48,0,0,0
        self.assertGreater(self.mbti_ESFP.sum1, 24)
        self.assertLessEqual(self.mbti_ESFP.sum2,24)
        self.assertLessEqual(self.mbti_ESFP.sum3, 24)
        self.assertLessEqual(self.mbti_ESFP.sum4, 24)

        #8.ESTP test # 48,0,48,0
        self.assertGreater(self.mbti_ESTP.sum1, 24)
        self.assertLessEqual(self.mbti_ESTP.sum2, 24)
        self.assertGreater(self.mbti_ESTP.sum3, 24)
        self.assertLessEqual(self.mbti_ESTP.sum4, 24)

        #9.INFJ  # 0,48,0,48
        self.assertLessEqual(self.mbti_INFJ.sum1, 24)
        self.assertGreater(self.mbti_INFJ.sum2, 24)
        self.assertLessEqual(self.mbti_INFJ.sum3, 24)
        self.assertGreater(self.mbti_INFJ.sum4, 24)

        #10.INFP # 0,48,0,0
        self.assertLessEqual(self.mbti_INFP.sum1, 24)
        self.assertGreater(self.mbti_INFP.sum2, 24)
        self.assertLessEqual(self.mbti_INFP.sum3, 24)
        self.assertLessEqual(self.mbti_INFP.sum4, 24)

        #11.ENFP # 48,48,0,0
        self.assertGreater(self.mbti_ENFP.sum1, 24)
        self.assertGreater(self.mbti_ENFP.sum2, 24)
        self.assertLessEqual(self.mbti_ENFP.sum3, 24)
        self.assertLessEqual(self.mbti_ENFP.sum4, 24)

        #12.ENFJ # 48,48,0,48
        self.assertGreater(self.mbti_ENFJ.sum1, 24)
        self.assertGreater(self.mbti_ENFJ.sum2, 24)
        self.assertLessEqual(self.mbti_ENFJ.sum3, 24)
        self.assertGreater(self.mbti_ENFJ.sum4, 24)

        #13.INTJ # 0,48,48,48
        self.assertLessEqual(self.mbti_INTJ.sum1, 24)
        self.assertGreater(self.mbti_INTJ.sum2, 24)
        self.assertGreater(self.mbti_INTJ.sum3, 24)
        self.assertGreater(self.mbti_INTJ.sum4, 24)

        #14.INTP # 0,48,48,0
        self.assertLessEqual(self.mbti_INTP.sum1, 24)
        self.assertGreater(self.mbti_INTP.sum2, 24)
        self.assertGreater(self.mbti_INTP.sum3, 24)
        self.assertLessEqual(self.mbti_INTP.sum4, 24)

        #15.ENTP # 48,48,48,0
        self.assertGreater(self.mbti_ENTP.sum1, 24)
        self.assertGreater(self.mbti_ENTP.sum2, 24)
        self.assertGreater(self.mbti_ENTP.sum3, 24)
        self.assertLessEqual(self.mbti_ENTP.sum4, 24)

        #16.ENTJ # 48,48,48,48
        self.assertGreater(self.mbti_ENTJ.sum1, 24)
        self.assertGreater(self.mbti_ENTJ.sum2, 24)
        self.assertGreater(self.mbti_ENTJ.sum3, 24)
        self.assertGreater(self.mbti_ENTJ.sum4, 24)



    def test_mbtiCalc(self):
                
        self.assertEqual(self.mbti_ISFP.mbtiCalc(), "ISFP")
        self.assertEqual(self.mbti_ISTJ.mbtiCalc(), "ISTJ")
        self.assertEqual(self.mbti_ISFJ.mbtiCalc(), "ISFJ")
        self.assertEqual(self.mbti_ESTJ.mbtiCalc(), "ESTJ")
        self.assertEqual(self.mbti_ESFJ.mbtiCalc(), "ESFJ")
        self.assertEqual(self.mbti_ISTP.mbtiCalc(), "ISTP")
        self.assertEqual(self.mbti_ESFP.mbtiCalc(), "ESFP")
        self.assertEqual(self.mbti_ESTP.mbtiCalc(), "ESTP")
        self.assertEqual(self.mbti_INFJ.mbtiCalc(), "INFJ")
        self.assertEqual(self.mbti_INFP.mbtiCalc(), "INFP")
        self.assertEqual(self.mbti_ENFP.mbtiCalc(), "ENFP")
        self.assertEqual(self.mbti_ENFJ.mbtiCalc(), "ENFJ")
        self.assertEqual(self.mbti_INTJ.mbtiCalc(), "INTJ")
        self.assertEqual(self.mbti_INTP.mbtiCalc(), "INTP")
        self.assertEqual(self.mbti_ENTP.mbtiCalc(), "ENTP")
        self.assertEqual(self.mbti_ENTJ.mbtiCalc(), "ENTJ")


if __name__ == '__main__':
    unittest.main()