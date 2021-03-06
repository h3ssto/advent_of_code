# advent_of_code
Repository for [Advent of Code](https://adventofcode.com/) solvers.

## 2021
For [2021](https://adventofcode.com/2021) I'm setting myself the challenge to solve the puzzles in Rust (probably I will solve each puzzle in Python first and then try to realize it in Rust some time later...).

## 2020
In [2020](https://adventofcode.com/2020), I solved the majority of puzzles in Python. When I come around to clean up the code a bit, I will upload it as well (14.5/25).

### Run Instructions
* Create a virtual environment (`python3 -m venv .venv`) and activate it (`source .venv/bin/activate`)
* Install the requirements (`pip install -r requirements.txt`)
    * If you don't want to execute `populate.py`, `pip install termcolor` suffices
* Get your personalized *input* from Advent of Code and place it in the directory of the respective day
    * You can use the `populate.py` script (needs your session cookie as `SESSION` in a `.env` file) 
    * **Be responsible! Do not remove the 10s delay between requests!**
* From the directory `2020` execute `python3 -m day<nr>.solve`

