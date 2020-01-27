## Basic Algorithms - 

Notes by ***Ali Rassolie***



#### Insertion Sort

Basically the algorithm takes an unsorted array, loops through the indices, and one by one, evaluates them against all indices below the given index, and changes their position with each iteration, given the entry conditions that the value in the index above is less than that below.

 ##### Loop invariant

Several stuff that the loop invariant requires. 

| Requirement      |                                                              |
| ---------------- | ------------------------------------------------------------ |
| *Initialization* | the condition, or the given invariant, needs to be true before entry into the loop |
| Maintenance      | if the given condition is true before the iteration of one cycle in the loop, it will ***remain true*** for the next iteration of the loop. |
| Termination      | Upon loop termination, the loop invariant will provide us with a way to eval whether the algorithm was correct  . . . |



## Dictionary

| Key                  | value                                                        |
| -------------------- | ------------------------------------------------------------ |
| ***Loop invariant*** | in the book, they discuss LOOP INVARINTS<br/>	which is defined as a statement (or condition)<br/>	that remains true for each iteration of the loop<br/>	for instance, in the loop above a (weak) loop<br/>	invariant is that j >= 0 always, for any <br/>	iteration of the loop (one can find other<br/>	more complicated invariants also, ofcourse). |
|                      |                                                              |
|                      |                                                              |

