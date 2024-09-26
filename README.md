Medians and order Statistics & Elementary Data Structures

This Assignment focuses on the implementation of medians, order statistics and elementary data structures.

'median.py': contains determinstic implementation for selection in worst-case linear time.

'randomized_quickselect.py': contains a randomized algorithm for selection in expected linear time.

'empirical_comparison.py': contains the logic to empirically compare the running time of the deterministic and randomized selection algorithms on different inout sizes and distributions.

'class_arrays.py': contains the implementation of basic operations such as inserion, deletion and access.

'class_matrix.py': contains the logic to implement basic operations such as insertion, deletion and access.

'class_stacks.py': contains the implementation of both stack and queue operations using arrays.

'class_Queues.py': contains the logic to implement both stack and queue operations using arrays.

'single_linked_lists.y': contains the implementation of singly linked lists with operations such as insertion, deletion and traversal.

'rooted_trees.py': contains the implementation of rooted trees using linked lists to represent the nodes and their relationships.

prerequisites:

python3.x

Run the code:

To run above files below are the commands:

python median.py

python randomized_quickselect.py

python empirical_comparison.py

python class_arrays.py

python class_matrix.py

python class_stacks.py

python class_Queues.py

python single_linked_lists.py

python rooted_trees.py

sample output for median.py:

python -u "/home/manasa/vscode_projects/medians_order_statistics/median.py"

The 5th smallest element is: 6

sample output for randomized_quickselect.py:

python -u "/home/manasa/vscode_projects/medians_order_statistics/randomized_quickselect.py"

The 8th smallest element is: 9

sample output for empirical_comparison.py:

python -u "/home/manasa/vscode_projects/medians_order_statistics/empirical_comparison.py"

Results for size 100:

  Distribution: random, Deterministic: 0.000111s, Randomized: 0.000035s
  
  Distribution: sorted, Deterministic: 0.000272s, Randomized: 0.000023s
  
  Distribution: reverse_sorted, Deterministic: 0.000065s, Randomized: 0.000030s
  
  Distribution: duplicates, Deterministic: 0.000033s, Randomized: 0.000022s

Results for size 1000:
  
  Distribution: random, Deterministic: 0.000702s, Randomized: 0.000301s
  
  Distribution: sorted, Deterministic: 0.000539s, Randomized: 0.000240s
  
  Distribution: reverse_sorted, Deterministic: 0.000557s, Randomized: 0.000360s
  
  Distribution: duplicates, Deterministic: 0.000233s, Randomized: 0.000208s

Results for size 10000:

  Distribution: random, Deterministic: 0.009432s, Randomized: 0.003920s
  
  Distribution: sorted, Deterministic: 0.006432s, Randomized: 0.002530s
  
  Distribution: reverse_sorted, Deterministic: 0.006308s, Randomized: 0.001362s
  
  Distribution: duplicates, Deterministic: 0.002521s, Randomized: 0.001190s

Results for size 100000:

  Distribution: random, Deterministic: 0.084176s, Randomized: 0.021501s
  
  Distribution: sorted, Deterministic: 0.068649s, Randomized: 0.028692s
  
  Distribution: reverse_sorted, Deterministic: 0.064618s, Randomized: 0.027993s
  
  Distribution: duplicates, Deterministic: 0.031139s, Randomized: 0.013824s
  
sample output for class_arrays.py:

python -u "/home/manasa/vscode_projects/medians_order_statistics/class_arrays.py"

[1, 2, 3]

3

[1, 3]

sample output for class_matrix.py:

python -u "/home/manasa/vscode_projects/medians_order_statistics/class_matrix.py"

1       0       0

0       0       5

sample output for class_stacks.py:

python -u "/home/manasa/vscode_projects/medians_order_statistics/class_stacks.py"

[1, 2]

2

1

sample output for class_Queues.py:

python -u "/home/manasa/vscode_projects/medians_order_statistics/class _Queues.py"

[1, 2]

1

2

sample output for single_linked_lists.py:

python -u "/home/manasa/vscode_projects/medians_order_statistics/single_linked_lists.py"

3 -> 2 -> 1

3 -> 1

sample output for rooted_trees.py:

python -u "/home/manasa/vscode_projects/medians_order_statistics/rooted_trees.py"

Root -> Child 1 -> Child 1.1 -> Child 1.2 -> Child 2 -> Child 2.1

This project is licensed under the MIT License - see the LICENSE file for details.
