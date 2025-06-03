#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)  # Store the iterator object
        self.counter = 0                # Initialize the counter

    def get_count(self):
        return self.counter             # Return the current count

    def __iter__(self):
        return self                     # The iterator returns itself

    def __next__(self):
        item = next(self.iterator)
        self.counter += 1               # Increment the counter
        return item     # Get next item or raise StopIteration

# Testing the CountedIterator

if __name__ == "__main__":
    data = [100, 200, 300]
    counted_iter = CountedIterator(data)

    print("Manual iteration with next():")
    try:
        print(next(counted_iter))  # 100
        print(next(counted_iter))  # 200
        print("Count so far:", counted_iter.get_count())  # 2
        print(next(counted_iter))  # 300
        print(next(counted_iter))  # Should raise StopIteration
    except StopIteration:
        print("No more items!")

    print("\nIteration with a for-loop:")
    counted_iter = CountedIterator(data)
    for item in counted_iter:
        print(item)
    print("Total items iterated:", counted_iter.get_count())
