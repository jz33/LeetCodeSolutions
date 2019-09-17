'''
1115. Print FooBar Alternately
https://leetcode.com/problems/print-foobar-alternately/

Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads.
Thread A will call foo() while thread B will call bar().
Modify the given program to output "foobar" n times.
'''
from threading import Barrier

class FooBar:
    def __init__(self, n):
        self.n = n
        self.b = Barrier(2)

    def foo(self, printFoo):
        for i in range(self.n):
            printFoo()
            self.b.wait()

    def bar(self, printBar):
        for i in range(self.n):
            self.b.wait()
            printBar()
