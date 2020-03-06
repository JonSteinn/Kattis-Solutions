# Scripts

## Add
This script will take all problems solutions in a temporary working folder, move them into src and create a `info.json` file for each problem and finally update the `README.md` file for the problems. The only thing required is the problem's KATTIS url.

### Example
Suppose we have the following directory:
```
.
├── README.md
├── scripts
├── src
└── new_probs
    ├── prob1
    │   ├── C
    │   │   └── main.c
    │   ├── C++
    │   │   └── main.cpp
    │   └── urlfile
    └── prob2
        ├── Java
        │   └── main.java
        └── urlfile
```
Each problem in `new_probs` must have this structure, that is the programming language as a directory and then the files and for each problem there must be a file containing a single line with the link to the problem on Kattis. They must all share a name. To run the script:
```Bash
python scripts/add.py new_probs urlfile myrepo
```
In my case, `myrepo` would me `https://github.com/JonSteinn/Kattis-Solutions`. The script has default values of `tmp`, `url.txt` and my repo.

## Url checker
This scripts extracts all links from the `README.md` file and checks if a get request to them returns a 200 status code.