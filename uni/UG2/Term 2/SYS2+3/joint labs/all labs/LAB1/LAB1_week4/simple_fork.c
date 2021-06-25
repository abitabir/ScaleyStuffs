#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>


int main()
{
pid_t pid_main;
pid_t pid_child, return_pid, terminated_child_pid;


pid_main = getpid();
return_pid = fork(); //first child created
if (return_pid == -1) {      /* fork() failed */
    perror("fork");
    exit(1);
}
printf("The main process %d \n",pid_main);
printf("The parent process of the current process is %d \n",getppid());
printf("The child return pid %d \n", return_pid);
printf("The current process %d \n",getpid());

if(return_pid == 0)
{
    //printf("I am the child process");
}
else
{
    //printf("I am the main parent process");
    //terminated_child_pid = wait(NULL);
    //printf("The terminated child %d \n", terminated_child_pid); 
}


}
