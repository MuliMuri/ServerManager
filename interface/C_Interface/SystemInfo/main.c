#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	unsigned int deax, debx, decx, dedx;
	char* a = malloc(0xC+1);
	memset(a, 0, 0xC+1);

	if (!a)
	{
		return -1;
	}
	
	__asm {
		mov eax, 1;
		cpuid;
		mov deax, eax;
		mov debx, ebx;
		mov dedx, edx;
		mov decx, ecx;
	}
	
	memcpy(a, (char*)&debx, 0x4);
	memcpy(a+0x4, (char*)&dedx, 0x4);
	memcpy(a+0x8, (char*)&decx, 0x4);



	printf("%08X-%08X-%08X-%08X\r\n", deax, debx, decx, dedx);
	return 0;
}
