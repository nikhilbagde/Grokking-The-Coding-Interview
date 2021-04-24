import unittest

from app.mainApp import ListNode
from app.mainApp import MainApp


class TestMainApp(unittest.TestCase):

    def setUp(self):
        self._mainAppInstance = MainApp()
        self._arguments = list()

        node_3 = ListNode(3)
        node_2 = ListNode(2)
        node_0 = ListNode(0)
        node_neg4 = ListNode(-4)

        node_3.next = node_2
        node_2.next = node_0
        node_0.next = node_neg4
        node_neg4.next = node_2

        self._arguments.append({
            'head': node_3,
            'expectedResult': True
        })

        node_1 = ListNode(1)
        node_2 = ListNode(2)

        node_1.next = node_2
        node_2.next = node_1

        self._arguments.append({
            'head': node_1,
            'expectedResult': True
        })

        self._arguments.append({
            'head': ListNode(1),
            'expectedResult': False
        })

        self._arguments.append({
            'head': None,
            'expectedResult': False
        })

        node_1 = ListNode(1)
        node_2 = ListNode(2)

        node_1.next = node_2

        self._arguments.append({
            'head': node_1,
            'expectedResult': False
        })

    def test_run(self):
        for argument in self._arguments:
            actual_result = self._mainAppInstance.run(argument['head'])
            self.assertEqual(argument['expectedResult'], actual_result)
