In the week-4 online session, we focus on lecture 4 and 5, process management and IPC and next week session will be focusing on 5 and 6 (IPC and thread scheduling).

   This session will be working on solidifying our knowledge in process creation, and process termination and will discuss many concepts such as zombie and orphan processes in a bit of details. So this should be seen as an extended session of lecture 4 and lecture 5.

   Let's start with a simple_fork.c program in LAB1_week4 repo, take 10 mins to do this.

   Compile and execute the program, and investigate what you found. 
```
   gcc simple_fork.c -o simple_fork

   ./simple_fork
 ```

   1. How many print statements? Did you see print statements are repeated?

   2. If you execute the program again, what do you find? Is the sequence of the print is same or different? Why is the sequence of statements different?

   3. Did you see if ```The parent process of the current process is 1 ```? 

   4. What will happen when you move 

      ```
      printf("The main process %d \n",pid_main);

      printf("The parent process of the current process is %d \n",getppid());
      ```

      before 'return_pid = fork();'

   5. How can you make the first child process created by this statement "return_pid = fork();" a zombie process? 

   ​       A zombie process is a process that has terminated, but whose parent has not yet called wait()(may be parent process is still executing), is known as a zombie process. 

   6. You can restrict what lines will be executed by a child process by including 

     if(return_pid == 0){

      //instructions that you only child process to execute.

      }

      else

      {

      //instructions that you only parent process to execute.

      }

   7. Uncomment  these two lines in the else block,

        // terminated_child_pid = wait(NULL);

         // printf("The terminated child %d \n", terminated_child_pid); 

      and compile and execute again. Do you still find parent of a process is 1 in any printf?

   8. you can use " sleep(1);  " // introduces 1 s delay, you can use this delay to control the active time of child or parent process to understand behaviour better.

   9. If a parent did not invoke wait() and instead terminated, thereby leaving its child processes as orphans. Traditional UNIX systems addressed this scenario by assigning the init process as the new
      parent to orphan processes. (as you see  in our case the orphan process is created when child process showed parent as 1.)

   

   







