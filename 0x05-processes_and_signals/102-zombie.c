#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

/**
 * infinite_while - create infinite loop
 * Return: 0
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates Zombie processes
 * Return: 0
 */

int main(void)
{
	int i = 0;

	while (i < 5)
	{
		int pid, ppid;

		pid = getpid();
		ppid = getppid();

		if (fork() == 0)
			return (0);

		printf("Zombie process created, %d: %d\n", ppid, pid);

		i++;
	}

	infinite_while();

	return (1);
}
