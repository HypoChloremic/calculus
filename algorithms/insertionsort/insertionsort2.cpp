#include <iostream>

using namespace std;

// very simple function
// printList -- func
// will print the list that is 
// passed
void printList(int *list, int listLength){ 
	// what is interesting here is that we 
	// tell the function that we are going to pass
	// a pointer. Look below how that pointer is passed
	for (int i = 0; i < listLength; i++){
		cout << list[i] << " ";
	}
	cout << "\n";
}

int main(int argc, char const *argv[])
{
	// we declare our variables and values
	int listLength = 7;
	int list[listLength] = {2,4,6,2,123,56,7};
	int k, j;
	cout << "Input: \n";
	printList(list, listLength);

	// this outside for loop is important, 
	// as it remembers our position in 
	// the list, and will remain unaffected
	// by the manipulations by the while loop
	for (int i = 1; i < listLength; i++){
		// this constant declaration of k
		// is very important, for the 
		// algo to remember what the 
		// value we are moving is.  
		k = list[i];
		j = i - 1;

		// we eval whether the 
		// constant value k is less than 
		// val at index j. Note that the 
		// index j moves down the list, 
		// and will break either if k
		// is more than than list at index j
		// or if j is outside the array scope. 
		while ((k < list[j]) && (j >= 0)){
			cout << "Evalling\n";
			printList(list, listLength);
			list[i] = list[j];
			list[j] = k;
			j = j - 1;
			i = i - 1;
		} 
	}

	// in the book, they discuss LOOP INVARINTS
	// which is defined as a statement (or condition)
	// that remains true for each iteration of the loop
	// for instance, in the loop above a (weak) loop
	// invariant is that j >= 0 always, for any 
	// iteration of the loop (one can find other
	// more complicated invariants also, ofcourse). 

	// what we can see here is that when
	// we pass the list not in the form
	// of a pointer, but as the list in 
	// its entirety. 
	// so, somehow, the function knows 
	// to only use the pointer
	// and furthermore to access that 
	// same function.
	// 
	cout << "Output: \n";
	printList(list, listLength);

	return 0;
}