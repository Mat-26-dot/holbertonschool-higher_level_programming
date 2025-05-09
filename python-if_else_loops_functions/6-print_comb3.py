#!/usr/bin/python3
print(*("{:02d}".format(i) for i in range(90) if i // 10 < i % 10), sep=", ")