# famous-search-algorithms-for-missionaries-and-cannibals

## How to use
Just clone the project and run any file that you want by python. 


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
