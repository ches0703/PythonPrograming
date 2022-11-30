# # Generator
# def myRange(n):
#     i = 0
#     while i < n:
#         yield i
#         i += 1


# for i in myRange(5):
#     print("i = ", i)

# Generator
def myRange(n):
    i = 0
    while i < n:
        yield i
        i += 1


MAX_RANGE = 5

itr = myRange(MAX_RANGE)

for i in myRange(MAX_RANGE + 1):
    d = next(itr)
    print("d = ", d)