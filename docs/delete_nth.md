#### defaultdict & delete_nth
>Given a list lst and a number N, create a new list
>that contains each number of the list at most N times without reordering.
>For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2],
>drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3,
>which leads to [1,2,3,1,2,3]

Well, I could traverse through the entire list every time I check a new element to count the number of
times that element is there. But that would result in O(n^2) time complexity. Not good.

If I use a hash map, then I can add a key every time I encounter a new element and update value for
existing key every time I encounter an existing number. The space complexity is O(n), but time complexity
is O(n), since I am traversing through the list only once.

```python
def delete_nth(lst, N):
    hashmap = dict()
    answer = []
    for num in lst:
        if num in hashmap.keys():
            hashmap[num] += 1
        else:
            hashmap[num] = 1
        if hashmap[num] > N:
            break
        answer.append(num)
    return answer
```

But this seems to be O(n^2). We are iterating through hashmap.keys(). Not exactly the right way to
implement. Let's use defaultdict. This automatically creates an entry for any key which was not
encountered before.

```python
from collections import defaultdict

def delete_nth(lst, N):
    hashmap = defaultdict(int)
    answer = []
    for num in lst:
        hashmap[num] += 1
        if hashmap[num] > N:
            break
        answer.append(num)
    return answer
```

[Home](../README.md)