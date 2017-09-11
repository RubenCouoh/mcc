#include <stdio.h>
#include <math.h>
#include <limits>

using namespace std;

int imax = std::numeric_limits<int>::max();

int mod(int base, int exp, int mod){ 

	unsigned result = 1;

	while (exp > 0) {
		
		unsigned acc = 1;
		unsigned acc2 = 1;
		
		while (acc2 <= imax && exp > 0) {
			acc = acc2;
			acc2 = acc2 * base;
			exp = exp-1;
		}

		if (acc2 <= imax) {
			acc = acc2;
		} else {
			exp = exp +1;
		}

		result *= acc % mod;
	}

	return result % mod;
}


bool primo(int n) {

 	int next=3, count=0;
 	int sqrtn = sqrt(n)+1;
 	bool isPrime = false;
 	
 	if (n == 2) {
 		isPrime = true;
 	} else if (n%2 != 0) {
 		
		while (next<=sqrtn) {
			count+= (n % next == 0)?1:0;
			next+= 2;
		}
		
		isPrime = count==1 ? true: false;
 	}

	return isPrime;	
}
	
bool fermat(int n){
	// teorema de fermat a^n mod n = a
	
  long int a = 2;
	
	for (a=2; a<=(n-1); a++) {
		long int modulo= mod(a,n,n);

		if (modulo == a) {
			return true; 
		}	
	}

	return false;
}
			
int  main() {
	printf("Ingrese un numero\n");
	
	int n=0;
	scanf("%d",&n);
	
	if (n<=2) {
		printf("El numero %d es incorrecto\n",n);
	} else {
	  
		if (!primo(n) && fermat(n)) {
		
				printf("El numero %d es Carmichael\n",n);

		} else {

			printf("El numero %d es Normal\n",n);
		}

	}
		
	return 0;
}