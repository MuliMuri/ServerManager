#pragma once
#ifndef HARDWARE_H
#define HARDWARE_H

typedef struct _CPUInfo
{
	unsigned int info_selector;

	char cpu_series[12];

}CPUUInfo, *PCPUInfo;


unsigned int GetCPUSeries();

#endif // !HARDWARE_H
