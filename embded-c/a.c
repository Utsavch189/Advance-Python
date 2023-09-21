#include <stdio.h>
#include <sys/resource.h>

void getMemoryUsage(){
	struct rusage r_usage;
  	getrusage(RUSAGE_SELF,&r_usage);
 	 // Print the maximum resident set size used (in kilobytes).
  	printf("Memory usage: %ld kilobytes\n",r_usage.ru_maxrss);
}

int square(int i) {
	return i * i;
}
