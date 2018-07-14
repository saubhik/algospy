#### flatten
>Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.


Knowledge of isinstance() is the key. Then a simple recursion
logic works. Traverse over elements in a list, and if the elements
are lists themselves, we need to get into nested loops. So this
calls for a recursion stack. A recursive method requires an
initialiser wrapper, but with Python's capability of using optional
arguments, we can finish this using a single function.

```python
def flatten(l, answer=[]):
    for elem in l:
        if not isinstance(elem, list):
            answer.append(elem)
        else:
            flatten(elem, answer)
    return answer
```

But there is a problem here. The problem 
with using default arguments is that only one instance of 
them actually exists. So, we need answer to be initialised with
an empty list every time this function is called.

```python
def flatten(l, answer=None):
    if answer is None:
        answer = []
    for elem in l:
        if not isinstance(elem, list):
            answer.append(elem)
        else:
            flatten(elem, answer)
    return answer
```

I saw from [this](https://stackoverflow.com/questions/6794285/python-function-remembering-earlier-argument-kwargs) 
SO question that one can also do `answer = None or answer`. Cool.
