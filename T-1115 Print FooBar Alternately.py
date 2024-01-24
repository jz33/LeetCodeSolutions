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

The same instance of FooBar will be passed to two different threads:

    thread A will call foo(), while
    thread B will call bar().

Modify the given program to output "foobar" n times.


Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously.
One of them calls foo(), while the other calls bar().
"foobar" is being output 1 time.

Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times.

Constraints:
    1 <= n <= 1000
'''
from threading import Event, Barrier

class FooBar:
    '''
    Use Event.
    Real TikTok question: https://www.1point3acres.com/bbs/thread-1039412-1-1.html
    '''
    def __init__(self, n):
        self.n = n
        self.e12 = Event()
        self.e21 = Event()
        self.e21.set()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.e21.wait()
            self.e21.clear()
            printFoo()
            self.e12.set()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.e12.wait()
            self.e12.clear()
            printBar()
            self.e21.set()


class FooBar2:
    '''
    Use Barrier
    '''
    def __init__(self, n):
        self.n = n
        self.b = Barrier(2)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            printFoo()
            self.b.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.b.wait()
            printBar()