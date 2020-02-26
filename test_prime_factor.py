from unittest import TestCase
from prime_factor import PrimeFactor

class TestFactor(TestCase):
    def test(self):
        self.assertEquals(True, True)

    def test_0(self):
        self.assertEquals(PrimeFactor.of(0), [])

    def test_1(self):
        self.assertEquals(PrimeFactor.of(1), [])

    def test_2(self):
        self.assertEquals(PrimeFactor.of(2), [2])
    
    def test_3(self):
        self.assertEquals(PrimeFactor.of(3), [3])

    def test_5(self):
        self.assertEquals(PrimeFactor.of(5), [5])  

    def test_4(self):
        self.assertEquals(PrimeFactor.of(4), [2,2])

    def test_9(self):
        self.assertEquals(PrimeFactor.of(9), [3,3])     

    def test_letter(self):
        self.assertEquals(PrimeFactor.of('a'), [])
