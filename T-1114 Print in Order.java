/*
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
*/
import java.util.concurrent.*;

class Foo {
    private Semaphore s12 = new Semaphore(0 /* permits */);
    private Semaphore s23 = new Semaphore(0 /* permits */);
    
    public Foo() {
        
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        
        s12.release();
    }

    public void second(Runnable printSecond) throws InterruptedException {
        s12.acquire();
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        
        s23.release();
    }

    public void third(Runnable printThird) throws InterruptedException {
        s23.acquire();
        
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
