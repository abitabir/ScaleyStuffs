#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define handle_error(msg) \
           do { perror(msg); exit(EXIT_FAILURE); } while (0)
           
int sum = 0; /* this data is shared by the thread(s) */
void *increment(void *param); /* threads call this function */
void *decrement(void *param);
pthread_mutex_t mutexsum;  /* used to create a mutex variable*/

int main(int argc, char *argv[])
{
    pthread_t  tid, tid1; /* the thread identifier */
    pthread_attr_t attr, attr1; /* used to set thread attributes */
    
    int return_status;
    pid_t pid;

    /* set the default attributes of the thread */
    printf("Main PID: %d\n", getpid()); 

    /*printf("Main Thread: %d\n", pthread_self() ); */
    
    pthread_mutex_init(&mutexsum, NULL); /*initialise mutex*/
    printf("mutexsum %zi",mutexsum);
    
    
    if(argc < 2)
    { 
        printf("Invalid input arguments"); exit(0);
    }

    pthread_attr_init(&attr);
        /*If the attributes specified by attr are changed later, the thread's attributes are not affected.*/
        /* create the thread */
    return_status = pthread_create(&tid, &attr, increment, argv[1]);
    
    if(return_status != 0)
    { 
        handle_error("First thread creation failed");
    }

    return_status = pthread_create(&tid1, &attr, decrement, argv[1]);
    if(return_status != 0)
    { 
        handle_error("Second thread creation failed");
    }
    /* wait for the thread to exit, blocks the calling thread until the specified thread terminates. */
    return_status = pthread_join(tid, NULL); 

    if(return_status != 0)
    { 
        handle_error("Thread join failed");
    }
    return_status = pthread_join(tid1, NULL); 

    if(return_status != 0)
    { 
        handle_error("Thread join failed");
    }   
    printf("sum = %d ",sum);
    pthread_mutex_destroy(&mutexsum);
    return 0;
}


/* The thread will execute in this function */
void *increment(void *param)
{
    int i, upper = atoi(param);
    for (i = 1; i <= upper; i++)
    {
        pthread_mutex_lock (&mutexsum);
        sum += 1;
        printf("increment: %d, sum: %d \n", i, sum);
        pthread_mutex_unlock (&mutexsum);
    }
    //printf("Child-1 PID: %d\n", getpid());
    //printf("Main Thread: 0x%.8x %.8x\n", pthread_self() );
    //sleep(100);
    pthread_exit(0);
}

void *decrement(void *param)
{
    int i, upper = atoi(param);
    for (i = 1; i <= upper; i++)
    {
        pthread_mutex_lock (&mutexsum);
        if (sum  > 0) 
        {
            sum -= 1;
        }
        printf("decrement: %d, sum: %d \n", i, sum);
        pthread_mutex_unlock (&mutexsum);
    }
    //printf("Child-2  PID: %d\n", getpid());
    //printf("Main Thread: 0x%.8x %.8x\n", pthread_self() );
    //sleep(100);
    pthread_exit(0);
}