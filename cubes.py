"""
// 1729 = 1^3 + 12^3 = 9^3 + 10^3
----------^^^^^^^^^^ A
-----------------------^^^^^^^^^^ B
      R = f(...)     = g(...)
     
# a^3 + b^3 = c^3 + d^3 < N
# a,b,c,d >= 0 ; a!=c ; a!=d
"""
import heapq

      
class Int(int):
    """An int annotated with whatever we need"""

    def __new__(cls, value, gen, j):
        rv = super().__new__(cls, value)
        rv.gen = gen
        rv.j = j
        return rv

    # below was useful for debugging...
    # def __repr__(self):
    #     return "%s %s %s" % (self, self.j, id(self.gen))


def f(N):
    heap = []
    for j in range(1, int(N ** (1/3)) + 1):  # imprecise bound
        gen = iter(range(j))
        i = next(gen)
        n = Int(i ** 3 + j ** 3, gen, j)
        heapq.heappush(heap, n)

    while heap:
        n = heap[0]
        yield n
        try:
            n = Int(next(n.gen) ** 3 + n.j ** 3, n.gen, n.j)
            if n > N:
                raise StopIteration()  # precise bound
        except StopIteration:
            heapq.heappop(heap)
        else:
            heapq.heappushpop(heap, n)


def solutions(N):
    last = None
    for n in f(N):
        if n == last:
            yield n
        last = n
