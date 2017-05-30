from collections import deque

# maxlen is optional argument
dq = deque(range(10), maxlen=10)
print('deque(range(10), maxlen=10) = {0}'.format(dq))

# Rotating with n > 0 takes items from the right end and prepends them to the
# left; when n < 0 items are taken from left and appended to the right.
dq.rotate(3)
print('dq.rotate(3) = {}'.format(dq))
dq.rotate(-4)
print('dq.rotate(-4) = {}'.format(dq))
dq.appendleft(0)
print('dq.appendleft(0) = {}'.format(dq))
dq.append(10)
print('dq.append(10) = {}'.format(dq))

# Adding three items to the right pushes out the leftmost
dq.extend([20,30, 40])
print('dq.extend([20,30, 40]) = {0}'.format(dq))

# Note that extendleft(iter) works by appending each successive item of the
# iter argument to the left of the deque, therefore the final position of the
# items is reversed
dq.extendleft(list('abc'))
print("dq.appendleft(list('abc')) = {}".format(dq))

# Pop right item
dq.pop()
print('dq.pop() = {}'.format(dq))

# Pop left item
dq.popleft()
print('dq.popleft() = {}'.format(dq))
