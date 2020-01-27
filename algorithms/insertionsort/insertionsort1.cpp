#include <iostream>
using namespace std;

void printList(int *list, int listLength){
	cout << "";
	for (int i = 0; i < listLength; ++i)
	{
		cout << list[i] << "\n";
	}
	// return 0;
}

int main(int argc, char const *argv[])
{
	int listLength       = 7;
	int list[listLength] = {4,5,2,1,3,8,9};
	int key;
	int j;

	for (int i=1; i<listLength; i++){
		key = list[i];
		j = i - 1;
		cout << "key: " << key << "\n";

		while ((j > 0) && list[j] > key){
			list[j+1] = list[j];
			j = j-1;
		}

		list[j+1] = key;
	}

	printList(list, listLength);

	return 0;
}