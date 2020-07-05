/*
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
*/
import java.util.concurrent.*;

class FooBar {
    private int n;
    
    private Semaphore fooSemphore = new Semaphore(1 /* permits */);
    private Semaphore barSemphore = new Semaphore(0 /* permits */);

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            fooSemphore.acquire();
            
            // printFoo.run() outputs "foo". Do not change or remove this line.
            printFoo.run();
            
            barSemphore.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            barSemphore.acquire();
            
            // printBar.run() outputs "bar". Do not change or remove this line.
            printBar.run();
            
            fooSemphore.release();
        }
    }
}
