# Infinite generators in python
def infinite_chai():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))

# an infinite generator is python generator that keeps producing values forever..
# when working with sequence and hove no natural end then it becomes useful.