import unittest
from random import choice
from lab import Rocket


class TestMyLab(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Виконується лише раз")
        cls.name = choice(["Falcon 9", "Falcon 1"])
        cls.mass = 549054
        cls.size = 70

    def setUp(self) -> None:
        print("\nЗапускаємо тест і конфігуримо його")
        self.obj = Rocket(self.name, self.mass, self.size)

    def tearDown(self) -> None:
        del self.obj

    def test_my_obj_attributes(self):
        print(f"Тестуємо -> {self.obj.name}")
        self.assertEqual(self.obj.name, self.name)
        self.assertEqual(self.obj.mass, self.mass)
        self.assertEqual(self.obj.size, self.size)

    def test_instance(self):
        self.assertIsInstance(self.obj, Rocket)
        for class_type in [str, float, int]:
            self.assertNotIsInstance(self.obj, class_type)

    def testConvertPoundsFalcone(self):
        print(f"Тестуємо -> {self.obj.name}")
        result = self.obj.convert_to_pounds()
        self.assertAlmostEqual(result, self.obj.mass * 2.20462262, 2)
        self.assertIsInstance(result, float)

    def testConvertFeet(self):
        result = self.obj.convert_to_feet()
        self.assertAlmostEqual(result, self.size * 3.2808399)
        self.assertIsInstance(result, float)

    def test_mass_less_zero(self):
        with self.assertRaises(AssertionError):
            Rocket("Atlas V", -1, 58.3)

    def test_object_created(self):
        for name, mass, size in [("a", 1, 1), ("b", 2, 2)]:
            self.assertIsInstance(Rocket(name, mass, size), Rocket)

    def test_method_crash_on_start(self):
        self.assertIn(self.obj.crash_on_start(), [False, True])


if __name__ == '__main__':
    unittest.main(verbosity=2)