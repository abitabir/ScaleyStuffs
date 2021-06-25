Week 5: In this week we are learning about inter-process communication using shared memory and pipes in processes. 

Let's start with a shared_memory.c program in LAB1_week5 repo, take 10 mins to do this.

Compile and execute the program, and investigate what you found.

   `gcc shared_memory.c -o shared_memory

   ./shared_memory`
   
  If you get compile error like this 'undefined reference to `shm_unlink`
  then compile with -lrt flag as:
  
  `gcc shared_memory.c -o shared_memory -lrt`
   
   
   1. Observe what output you found printed on the command terminal.
   2. Understand what this program is doing? Did you observe child process able to read parent process data?
   3. What will happen if you move `child_return = fork(); after ftruncate(shm_fd, SIZE);`?
   4. Why do you think `ptr1 = mmap(0, SIZE, PROT_READ, MAP_SHARED, shm_fd, 0); `(line 36) is needed in child process.
   
Now you have understood, how you can create share memory between parent-child processes, now lets have a look on interprocess communication through pipes.

Let's start with a simple_pipe.c program in LAB1_week5 repo, take 10 mins to do this.

Compile and execute the program, and investigate what you found.

   `gcc simple_pipe.c -o simple_pipe`

   `./simple_pipe`
   
   1. Observe what output you found printed on the command terminal.
   2. Understand what this program is doing? Did you observe child process able to read parent process data?
   3. Think about the communication happening through pipe, is it unidirectional/bidirectional? Is it half-duplex or full duplex? Discuss with your group, and report your understanding in the main room.
   4. Think what will happen if another new child process also reads the pipe, create a new child process and report your understanding.
   5. What will happen to pipe if parent process terminates before child process reads the pipe? Find out if this is an ordinary or a named pipe.
   
Now you have understood, how you can create a pipe between parent-child processes, now lets have a look on named pipes.

Let's start with a writer.c  and reader.c program in LAB1_week5 repo, take 10 mins to do this.

Compile and execute the program, and investigate what you found.

`gcc writer.c -o writer`

`gcc reader.c -o reader`

Now open another terminal, and run
`./writer` on one terminal and `.\reader` on another terminal,  (make sure in both terminal you are in right path (repo or directory) so your terminal can find both execuatable files).

1. Observe what output you found printed on the command terminal. Type some message on terminal 1 and 2 and see what you observed.
2. Think about how you can modify the behaviour of the program. 


Now think how you can apply these IPC mechanishms in your matrix multiplication program? What things you need to do first? Discuss with your group members and group mentor.
   

### Useful Reading

POSIX Shared Memory (taken from Silbersharz Book, chapter 3, page - 132). 
Several IPC mechanisms are available for POSIX systems, including shared memory and message passing. Here, we explore the POSIX API for shared
memory. POSIX shared memory is organized using memory-mapped files, which associate the region of shared memory with a file. A process must first create
a shared-memory object using the shm_open() system call, as follows:
```fd = shm_open(name, O_CREAT | O_RDWR, 0666); ```
name:  name of the shared-memory object.

O_CREAT:  Create the object if it doesn't already exist.

O_RDWR:  Object is created for both read and write option.

Permissions: Read/write permissions for the object. 

​						User: Read/Write/Execute

​						Group: Read/Write/Execute

​						All: Read/Write/Execute	

​						**r** = read permission
​						**w** = write permission
​					  **x** = execute permission
​						**-** = no permission



| Number | Permission Type       | Symbol |
| :----- | :-------------------- | :----- |
| 0      | No Permission         | ---    |
| 1      | Execute               | --x    |
| 2      | Write                 | -w-    |
| 3      | Execute + Write       | -wx    |
| 4      | Read                  | r--    |
| 5      | Read + Execute        | r-x    |
| 6      | Read +Write           | rw-    |
| 7      | Read + Write +Execute | rwx    |

So in this lab sessions, we'll learn following concepts. 

(1) How to create a memory area (object).

(2) How to associate it or use within different processes.

(3) How to distroy this memory object when execution ends.

(4) What synchronisation mechanishms are needed  for this shared memory area to be used properly (we will be looking synchronisation in more details later sessions based on week 5 and 6 material.)

(5) How you can use pipe for communicating between two different processes.

We will be using   #include <sys/mman.h> header files or devices into memory. mmap() creates a new mapping in the virtual address space of the calling process. Read about this is here: https://man7.org/linux/man-pages/man2/mmap.2.html, however, we will be looking on virtual memory management in the course a bit later.

Read about mkfifo here: https://man7.org/linux/man-pages/man3/mkfifo.3.html





       
      

















