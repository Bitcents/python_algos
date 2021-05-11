# Here we implement the classical game of the Towers of Hanoi
# The best data structure to implement the Hanoi solver is to use the stack
# We will use the stack implementation that we have created ourselves
from stack import Stack

# Setting up the towers here
# We will start with the classical three discs
num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()

for i in range(1, num_discs + 1):
    tower_a.push(i)

def hanoi(start: Stack, dest: Stack, temp: Stack, n: int) -> None:
    if n == 1:
        disc_number = start.pop()
        print(f'inserting {disc_number} from {start} to {dest}')
        dest.push(disc_number)
    else:
        hanoi(start, temp, dest, n-1)
        hanoi(start, dest, temp, 1)
        hanoi(temp, dest, start, n-1)

if __name__=='__main__':
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)