#include <array>
#include <iostream>
using namespace std;

array<long long,20201227> data;

long long operate(long long x, long long n)
{
	long long y = 1;
	while (n--)
		y = (y*x) % 20201227;
	return y;
}


int main()
{
	long long pubkey[2];

	cin >> pubkey[0] >> pubkey[1];

	data[0] = 1;
	for (int i = 1; i < 20201227; i++) {
		data[i] = (data[i-1]*7) % 20201227;
		if (data[i] == pubkey[0])
			cout << "key 1: " << i << ": " << operate(pubkey[1], i) <<  endl;
		else if (data[i] == pubkey[1])
			cout << "key 2: " << i << ": " << operate(pubkey[0], i) <<  endl;
	}
}