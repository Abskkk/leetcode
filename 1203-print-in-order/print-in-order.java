class Foo {
    private AtomicBoolean firstDone = new AtomicBoolean();
    private AtomicBoolean secondDone = new AtomicBoolean();

    public Foo() {
        
    }

    public void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        firstDone.set(true);
    }

    public void second(Runnable printSecond) throws InterruptedException {
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        while (firstDone.get() == false) {}
        printSecond.run();
        secondDone.set(true);
    }

    public void third(Runnable printThird) throws InterruptedException {
        while (secondDone.get() == false) {}
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}