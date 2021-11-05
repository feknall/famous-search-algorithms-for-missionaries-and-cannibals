# famous-search-algorithms-for-missionaries-and-cannibals

## How to use
Just clone the project and run any file that you want by python. 


## Output of Depth First
```
Win! Last state: (0, 0, 'b')
Steps: [(3, 3, 'a'), (3, 1, 'b'), (3, 2, 'a'), (3, 0, 'b'), (3, 1, 'a'), (1, 1, 'b'), (2, 2, 'a'), (0, 2, 'b'), (0, 3, 'a'), (0, 1, 'b'), (0, 2, 'a'), (0, 0, 'b')]
depth: 0, index: 0, state: (3, 3, 'a')
├── depth: 1, index: 0, state: (3, 2, 'b')
└── depth: 1, index: 1, state: (3, 1, 'b')
    └── depth: 2, index: 0, state: (3, 2, 'a')
        └── depth: 3, index: 0, state: (3, 0, 'b')
            └── depth: 4, index: 0, state: (3, 1, 'a')
                └── depth: 5, index: 0, state: (1, 1, 'b')
                    └── depth: 6, index: 0, state: (2, 2, 'a')
                        └── depth: 7, index: 0, state: (0, 2, 'b')
                            └── depth: 8, index: 0, state: (0, 3, 'a')
                                └── depth: 9, index: 0, state: (0, 1, 'b')
                                    └── depth: 10, index: 0, state: (0, 2, 'a')
                                        └── ***** depth: 11, index: 0, state: (0, 0, 'b') *****

Finished! Solution found? True
```
## Output of Breadth First
```
States: [(3, 3, 'a')]
Current State: (3, 3, 'a')
Future State: (3, 2, 'b')
Future State: (3, 1, 'b')
Future State: (2, 2, 'b')

States: [(3, 2, 'b'), (3, 1, 'b'), (2, 2, 'b')]
Current State: (3, 2, 'b')

Current State: (3, 1, 'b')
Future State: (3, 2, 'a')

Current State: (2, 2, 'b')

States: [(3, 2, 'a')]
Current State: (3, 2, 'a')
Future State: (3, 0, 'b')

States: [(3, 0, 'b')]
Current State: (3, 0, 'b')
Future State: (3, 1, 'a')

States: [(3, 1, 'a')]
Current State: (3, 1, 'a')
Future State: (1, 1, 'b')

States: [(1, 1, 'b')]
Current State: (1, 1, 'b')
Future State: (2, 2, 'a')

States: [(2, 2, 'a')]
Current State: (2, 2, 'a')
Future State: (0, 2, 'b')

States: [(0, 2, 'b')]
Current State: (0, 2, 'b')
Future State: (0, 3, 'a')

States: [(0, 3, 'a')]
Current State: (0, 3, 'a')
Future State: (0, 1, 'b')

States: [(0, 1, 'b')]
Current State: (0, 1, 'b')
Future State: (0, 2, 'a')
Future State: (1, 1, 'a')

States: [(0, 2, 'a'), (1, 1, 'a')]
Current State: (0, 2, 'a')
Future State: (0, 0, 'b')

Current State: (1, 1, 'a')

States: [(0, 0, 'b')]
Current State: (0, 0, 'b')
Win! Last state: (0, 0, 'b')


State Stack:
(3, 3, 'a')
(3, 2, 'b')
(3, 1, 'b')
(2, 2, 'b')
(3, 2, 'a')
(3, 0, 'b')
(3, 1, 'a')
(1, 1, 'b')
(2, 2, 'a')
(0, 2, 'b')
(0, 3, 'a')
(0, 1, 'b')
(0, 2, 'a')
(1, 1, 'a')
(0, 0, 'b')

All States:
[(3, 3, 'a')]
[(3, 2, 'b'), (3, 1, 'b'), (2, 2, 'b')]
[(3, 2, 'a')]
[(3, 0, 'b')]
[(3, 1, 'a')]
[(1, 1, 'b')]
[(2, 2, 'a')]
[(0, 2, 'b')]
[(0, 3, 'a')]
[(0, 1, 'b')]
[(0, 2, 'a'), (1, 1, 'a')]
[(0, 0, 'b')]
Finished!
```
## Output of Best First
```
Frontiers: [(3, 3, 'a')]
Best State: (3, 3, 'a')
Best Value: 6

Frontiers: [(3, 2, 'b'), (3, 1, 'b'), (2, 2, 'b')]
Best State: (3, 1, 'b')
Best Value: 4

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 3, 'a')]
Best State: (3, 2, 'a')
Best Value: 5

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (3, 0, 'b'), (2, 2, 'b')]
Best State: (3, 0, 'b')
Best Value: 3

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 1, 'a'), (3, 2, 'a')]
Best State: (3, 1, 'a')
Best Value: 4

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 0, 'b'), (1, 1, 'b')]
Best State: (1, 1, 'b')
Best Value: 2

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 0, 'b'), (2, 2, 'a'), (3, 1, 'a')]
Best State: (2, 2, 'a')
Best Value: 4

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 0, 'b'), (3, 1, 'a'), (1, 1, 'b'), (0, 2, 'b')]
Best State: (1, 1, 'b')
Best Value: 2

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 0, 'b'), (3, 1, 'a'), (0, 2, 'b'), (2, 2, 'a'), (3, 1, 'a')]
Best State: (3, 1, 'a')
Best Value: 4

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 0, 'b'), (0, 2, 'b'), (2, 2, 'a'), (3, 1, 'a'), (3, 0, 'b'), (1, 1, 'b')]
Best State: (0, 2, 'b')
Best Value: 2

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 0, 'b'), (2, 2, 'a'), (3, 1, 'a'), (3, 0, 'b'), (1, 1, 'b'), (0, 3, 'a'), (2, 2, 'a')]
Best State: (0, 3, 'a')
Best Value: 3

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 0, 'b'), (2, 2, 'a'), (3, 1, 'a'), (3, 0, 'b'), (1, 1, 'b'), (2, 2, 'a'), (0, 2, 'b'), (0, 1, 'b')]
Best State: (0, 1, 'b')
Best Value: 1

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 0, 'b'), (2, 2, 'a'), (3, 1, 'a'), (3, 0, 'b'), (1, 1, 'b'), (2, 2, 'a'), (0, 2, 'b'), (0, 2, 'a'), (0, 3, 'a'), (1, 1, 'a')]
Best State: (0, 2, 'a')
Best Value: 2

Frontiers: [(3, 2, 'b'), (2, 2, 'b'), (3, 3, 'a'), (3, 1, 'b'), (2, 2, 'b'), (3, 2, 'a'), (3, 0, 'b'), (2, 2, 'a'), (3, 1, 'a'), (3, 0, 'b'), (1, 1, 'b'), (2, 2, 'a'), (0, 2, 'b'), (0, 3, 'a'), (1, 1, 'a'), (0, 1, 'b'), (0, 0, 'b')]
Best State: (0, 0, 'b')
Best Value: 0

Win! Last state: (0, 0, 'b')
Finished! Win: True
```

