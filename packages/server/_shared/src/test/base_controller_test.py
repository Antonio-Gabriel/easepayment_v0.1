from unittest import TestCase


class TestControllerBase(TestCase):
    def base_controller(self):

        result = 1 + 2
        print("test")

        self.assertLess(result, 1)
