## Week 6

In this week, we are still working towards learning concepts which will help us to solve problems described in  LAB1 and this week learning outcome are mapped with lecture 6 (threads) and some concepts from lecture 7, 8 (CPU scheduling) and 9 (Synchronisation). 

We have three programs. Lets start with first simple_threads.c  in LAB1_week6 repo and take 10-15s mins to analyse this program.

Compile and execute the program, and investigate what you found.

`gcc simple_threads.c -o simple_threads`

If you get error like "undefined reference to `pthread_create`" then compile with flag -lpthread.

`gcc simple_threads.c -o simple_threads -lpthread`

`./simple_threads  10`

Please note this program takes a command line arument, for example,  10 as specified in the above line. The argument  is just a value of counter, so you change the number if you like.

This program creates two new threads in the main program, observe following.

1. Observe what output you found printed on the command terminal.

2. Understand what this program is doing? Did you observe threads are sharing a global variable?

3. Try running few times and notice difference in your printed output.

4. Comment this line in the  increment function - printf("counter: %d, sum: %d \n", i, sum);  (line 45) and compile program again and execute again, with different command line arguments, such as 10, then 100, 1000, 10000, 100000. See what sum value is printed on the screen. Repeat execution few times and find if you see any difference in the sum?

5. How many threads do you think this simple_threads executable have? Find out by uncommenting sleep(100); in both increment and decrement function and compile and execute for any value of command argument. Open another terminal and see running threads by`ps -M <pid>` on macOS or `ps -T -p <pid>` on Linux.  You can use <PID>printed on terminal by the main program.

6. Uncomment `printf("Main Thread: %d\n", pthread_self() );' in the main program (line 21), in increment function  and decrement, both //printf("Child-1 PID: %d\n", getpid());

   //printf("Main Thread: %d\n", pthread_self() );

   and compile and execute the program to see what did you  observe as an output.

So this give you a bit of idea how to create and manage threads. There are hundreds of thread management  functions described in  `pthread.h`, so have a look on those.

I have created another `threads_attribute.c` for you all, lets quickly have a look on how to use these features so we have a better understanding of threads.
If you get lots of warning in compilation, than compile with 
`gcc threads_attribute.c -o threads_attribute -lpthread -D_GNU_SO `

For using compiler  concurrency optimization, we can use `omp.h`, see the `simple_openmp.c` to see how pragma are defined.

Now you have two tasks to do.

1. Go back to your reader.c and writer.c program from last and modify that program using threads and see you can improve some better interactive message communication? 
2. Work on your Matrix multiplication program and apply all your shared processes and threads understanding to reduce matric multiplication execution time.

Next week, we will be working on `simple_threads.c` again to synchronise it better by applying some of the synchronisation tools.



