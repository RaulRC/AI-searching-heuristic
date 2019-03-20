### BLOCKS PROBLEM

#### Description

Blocks World problem: https://en.wikipedia.org/wiki/Blocks_world

#### Usage

The following code will execute the default example: 

```python3 main.py -f configs/standard.cfg -s i```

Also you can find more examples in the subfolder ```configs/```:
* standard.cfg: basic example
* med.cfg: medium size problem
* hard.cfg: large size problem
* hell.cfg: extra complex problem 

There are three methods used for the solution: 
* Width search
* Depth search. Both Width and Depth works for a modest problem types (```standard.cfg``` file works well)
* A* method, also subdivided in two functions: recursive and iterative (recommended)

```bash
The arguments

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  -f CONFIG_FILE, --config-file CONFIG_FILE
                        Name of the config file to read
  -s SOLVER, --solver SOLVER
                        Solver applied [w|d|a|I]: [w]idth, [d]epth, [a]*
                        (recursive), [i] a* iterative (default [i])

```

Custom config file could be created as an ```ini``` file. Indicates initial and goal nodes in terms of table and stack.

```ini
[initial]
stack=E,D,A
table=C,B

[goal]
stack=E,D,C,B,A
table=
```

#### Example

##### Run: 

```bash
python3 main.py  -f configs/standard.cfg -s i
```

##### Output:

```bash
START!
Starting new search... 
[Initial state]
Stack:
|A|
|D|
|E|
 *      Table: {'C', 'B'}
---------

[Goal]
Stack:
|A|
|B|
|C|
|D|
|E|
 *      Table: {''}
---------

Expand... lvl 0
Expand... lvl 1
Expand... lvl 2
Expand... lvl 3
Final state: [move A to stack]
Stack:
|A|
|B|
|C|
|D|
|E|
 *      Table: set()
---------

Done! Depth: 4
Initial state -> remove from stack A -> move C to stack -> move B to stack -> move A to stack
Solution reached with solver [A* Iterative] in [4] levels (0.0 seconds)
Solution reached:
 Initial state -> remove from stack A -> move C to stack -> move B to stack -> move A to stack
Exit
===================================

```

##### Logging

Stored at generated ```output.log``` file.

##### Example ```output.log``` file:

```bash
2019-02-04 10:44:05,814 INFO: Init!
2019-02-04 10:44:05,814 INFO: Parsing arguments
2019-02-04 10:44:05,816 INFO: Starting new search...
[Initial state]
Stack:
|A|
|D|
|E|
 * 	Table: {'B', 'C'}
---------

[Goal]
Stack:
|A|
|B|
|C|
|D|
|E|
 * 	Table: {''}
---------

2019-02-04 10:44:05,816 INFO: Expand... lvl 0
2019-02-04 10:44:05,816 INFO: Expand... lvl 1
2019-02-04 10:44:05,817 INFO: Expand... lvl 2
2019-02-04 10:44:05,817 INFO: Expand... lvl 3
2019-02-04 10:44:05,818 INFO: Final state: [move A to stack]
Stack:
|A|
|B|
|C|
|D|
|E|
 * 	Table: set()
---------

2019-02-04 10:44:05,818 INFO: Solution reached:
 Initial state -> remove from stack A -> move C to stack -> move B to stack -> move A to stack
Exit
===================================
```