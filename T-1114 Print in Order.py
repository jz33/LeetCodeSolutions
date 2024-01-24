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
from threading import Barrier, Event
class Foo:
    '''
    Method 1: use Event
    '''
    def __init__(self):
        self.e12 = Event()
        self.e23 = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

        self.e12.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.e12.wait()

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

        self.e23.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.e23.wait()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()

class Foo2:
    '''
    Method 2: use barrier.
    All parties of the barrier should call wait then the party can proceed 
    '''
    def __init__(self):
        self.b12 = Barrier(2)
        self.b23 = Barrier(2)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        
        self.b12.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.b12.wait()

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        
        self.b23.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.b23.wait()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
