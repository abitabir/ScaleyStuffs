# Week 7 #

In this week, we are learning proccess synchronisation concepts which will help us to solve problems described in LAB1 and this week learning outcomes are mapped with lecture 6 (threads) and  9 & 10(Synchronisation).

We start with our previous week 6 program, which showed race condition and we include mutex locks to solve the race condition.

In this lab we will learn, how to create and initialise mutex variables and see how different threads can achieve synchronisation through locking and unlocking the mutex variable.

Lets start with `simple_mutex.c` and it will take your 15 mins to download, compile, execute and analyse this program.

`gcc simple_mutex.c -o simple_mutex`

If you get error like "undefined reference to pthread_create" then compile with flag -lpthread.

`gcc simple_mutex.c -o simple_mutex -lpthread`

`./simple_mutex 10`

Please note this program takes a command line argument, for example, 10 as specified in the above line. The argument is just a value of counter, so you change the number if you like.

This program creates two new threads in the main program, please observe following.

1. Observe what output did you find that is printed on the commandline terminal.

2. Understand what this program is doing? Did you observe threads are sharing a global variable in synchronised way?
3. Try running few times and notice difference in your printed output.
Execute program with different command line arguments, such as 10, then 100, 1000, 10000, 100000 and 1000000. See what sum value is printed on the screen. Repeat execution few times and find if you see any difference in the sum?
4. Are you able to resolve the race-condition which you were seeing in the previous LAB program simple_threads.c ?

Now lets start with  `simple_condition_need.c` and it will take your 10 mins to download, compile, execute and analyse this program, start with compiling and executing the program.

`gcc simple_condition_need.c -o simple_condition_need -lpthread`

`./simple_condition_need 10`

please observe following.

1. Observe what output did you find that is printed on the commandline terminal.

2. Understand what this program is doing?

3. Try running few times and notice difference in your printed output.
Execute program with different command line arguments, such as 10, then 100, 1000, 10000, 100000 and 1000000. See what sum value is printed on the screen. Repeat execution few times and find if you see any difference in the sum?

4. Are you able to resolve the race-condition which you were seeing in the previous LAB program simple_threads.c ? Why program is not able to print the correct sum value?

In the next program we look on Condition variables that provide another way for threads to synchronize. While mutexes implement synchronization by controlling thread access to data, condition variables allow threads to synchronize based upon the actual value of data.

Now lets start with  `simple_condition.c` and it will take your 10 mins to download, compile, execute and analyse this program; start with compiling and executing the program.

`gcc simple_condition.c -o simple_condition -lpthread`

`./simple_condition 10`

1. Observe what output did you find that is printed on the commandline terminal.

2. Understand what this program is doing?

3. Try running few times and notice difference in your printed output.
Execute program with different command line arguments, such as 10, then 100, 1000, 10000, 100000 and 1000000. See what sum value is printed on the screen. Repeat execution few times and find if you see any difference in the sum?

4. Are you able to resolve the race-condition which you were seeing in the previous LAB program simple_threads.c ? Is program now able to print the correct sum value?


Now you have two tasks to do. 

Investigate time of all three programs - with parameter 1000000, for example, by running 
`time ./simple_condition 1000000`

and 

`time ./simple_condition 1000000 >> simplecondition.log`

and also by commenting all printf statements in the programs, compile and execute again.

In the rest of time - go back to your reader.c and writer.c program from last and modify that program using threads and see you can improve some better interactive message communication?
Work on your Matrix multiplication program and apply all your shared processes and threads understanding to reduce matric multiplication execution time.
Next week, we will be working on simple_threads.c again to synchronise it better by applying some of the synchronisation tools.


