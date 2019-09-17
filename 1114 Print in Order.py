'''
1114. Print in Order
https://leetcode.com/problems/print-in-order/

Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}

The same instance of Foo will be passed to three different threads.
Thread A will call first(), thread B will call second(), and thread C will call third().
Design a mechanism and modify the program to ensure that second() is executed after first(),
and third() is executed after second().
'''
from threading import Barrier

class Foo:
    def __init__(self):
        self.b12 = Barrier(2)
        self.b23 = Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.b12.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b12.wait()
        printSecond()
        self.b23.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b23.wait()
        printThird()
