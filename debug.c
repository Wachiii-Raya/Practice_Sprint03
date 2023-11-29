#include <string.h>
#include <stdio.h> 
#include <stdlib.h>


#define LED1 5
#define LED2 3
#define LED3 9
#define SERVO 6
#define POT 0
#define HEARTBEAT 10

int	check_header(int *command)
{
	// undefined = x00, potent = x01, servo = x02, heartbeat = x03, led = x04
	if (command[0] == 0x00)
		return 0;
	else if (command[0] == 0x01)
		return (POT);
	else if (command[0] == 0x02)
		return (SERVO);
	else if (command[0] == 0x03)
		return (HEARTBEAT);
	else if (command[0] == 0x04)
	{
		if (command[2] == 0x01)
			return (LED1);
		else if (command[2] == 0x02)
			return (LED2);
		else if (command[2] == 0x03)
			return (LED3);
	}
	else
		return 0;
}


int    main(void)
{
	int buffer[] = {0x04, 0x00, 0x01};
	size_t size = 3;

    int header = check_header(buffer);
    printf("buffer: %d\n", buffer[0]);
    printf("buffer: %d\n", buffer[1]);
    printf("buffer: %d\n", buffer[2]);
    printf("header: %d\n", header);
    return (0);
}