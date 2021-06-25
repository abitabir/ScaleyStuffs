#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>


#define handle_error(msg) \
           do { perror(msg); exit(EXIT_FAILURE); } while (0)


int sum = 0; /* this data is shared by the thread(s) */
void *increment(void *param); /* threads call this function */
void *decrement(void *param);

int main(int argc, char *argv[])
{
    pthread_t id, tid, tid1; /* the thread identifier */
    pthread_attr_t attr, attr1; /* used to set thread attributes */
    int return_status;
    char *another_arg = "10";
    int policy; 
    size_t size = PTHREAD_STACK_MIN + 0x10000; //0x1000 = (int) 4096 bytes.
    size_t size1;
    void *stackbase, *returnbase; //this variable is to store stack base address pointer

/* set the default attributes of the thread */
if(argc < 2){ printf("Invalid input arguments"); exit(0);}
pthread_attr_init(&attr);
pthread_attr_init(&attr1);
//stackbase =  (void *) malloc(size); 
/* Before calling setstack make sure you have called mallock to get the stack size reserved */
//return_status = pthread_attr_setstack(&attr, stackbase, size); 
//return_status = pthread_attr_getstack (&attr, &returnbase, &size);
//printf("stack returnbase %zu \n ", (unsigned long) returnbase);
//return_status = pthread_attr_setdetachstate (&attr,PTHREAD_CREATE_DETACHED); 
return_status =  pthread_attr_setscope(&attr, PTHREAD_SCOPE_SYSTEM);
return_status  = pthread_attr_setschedpolicy (&attr, SCHED_FIFO); 
return_status  = pthread_attr_getschedpolicy (&attr, &policy); 
return_status =  pthread_attr_setstacksize(&attr, size); //set size to small than default size
return_status =  pthread_attr_getstacksize(&attr, &size);
//printf("stack size %zu \n ", size);
return_status = pthread_attr_getstacksize(&attr1, &size1);
//printf("stack size1 %zu \n ", size1);
//printf("Policy %d\n", policy);
pthread_setconcurrency(3);
return_status = pthread_getconcurrency();
//printf("getcurrency %d\n", return_status);
/* create the thread */
return_status = pthread_create(&tid, &attr, increment, argv[1]);
if(return_status != 0){ handle_error("First thread creation failed");}

return_status = pthread_create(&tid1, &attr, increment, argv[1]);
if(return_status != 0){ handle_error("Second thread creation failed");}

//return_status = pthread_create(&tid1, &attr, decrement, argv[1]);
//if(return_status != 0){ handle_error("Second thread creation failed");}
/* wait for the thread to exit, blocks the calling thread until the specified thread terminates. */

return_status = pthread_join(tid, NULL); 
if(return_status != 0){ handle_error("Thread join failed");}
return_status = pthread_join(tid1, NULL); 
if(return_status != 0){ handle_error("Thread join failed");}
//printf("sum = %d ",sum);
}
/* The thread will execute in this function */
void *increment(void *param)
{
int i, upper = atoi(param);
for (i = 1; i <= upper; i++){
sum += 1;
//printf("%d %d \n", i, sum);
}
pthread_exit(0);
}

void *decrement(void *param)
{
int i, upper = atoi(param);
//sum = 0;
for (i = 1; i <= upper; i++)
sum -= 1;
pthread_exit(0);
}