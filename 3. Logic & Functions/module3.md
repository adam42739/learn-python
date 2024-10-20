# Logic & Functions

## Contents

1. [Logic](#logic)
2. [If Statements](#if-statements)
3. [Loops](#loops)
4. [Functions](#functions)

## Logic

We can perform comparisions in Python.

| Comparison       | Code     |
| ---------------- | -------- |
| Equality         | `a == b` |
| Inequality       | `a != b` |
| Greater Than     | `a > b`  |
| Greater or Equal | `a >= b` |
| Less Than        | `a < b`  |
| Less or Equal    | `a <= b` |

Note that these comparisions are converted to boolean true or false values when they are executed.

```python
a = 10
b = 15
myBool = (a < b)
print(myBool)
>>> True
```

## If Statements

We can use comparisions to create if statements in Python.

```python
a = 10
b = 15
if a < b:
    print("A Less Than B")
else:
    print("A Not Less Than B")
```

It may also be handy to flip a boolean value. To do this we use the keyword `not`.

```python
a = False
b = not a
print(b)
>>> True
```

## Loops

We can loop using the `range` function. Not that the range is inclusive of only the first number, not the second.

```python
for i in range(0, 5):
    print(i)

>>> 0
>>> 1
>>> 2
>>> 3
>>> 4
```

We can also loop through elements in a list or dictionary.

```python
myList = [1, 3, 5, 10]
for item in myList:
    print(item)

>>> 1
>>> 3
>>> 5
>>> 10

myDict = {
    1: 10,
    2: -6,
    3: 12
}
for key in myDict:
    print("Key:", key, "Value:", myDict[key])

>>> Key: 1 Value: 10
>>> Key: 2 Value: -6
>>> Key: 3 Value: 12
```

## Functions

We can create functions to store code we might want to run again later.

```python

def add_dict_values(myDict):
    total_sum = 0
    for key in myDict:
        total_sum += myDict[key]
    return total_sum

myDict = {
    1: 10,
    2: -6,
    3: 12
}
print(add_dict_values(myDict))

>>> 16

myDict = {
    "4": 2,
    "12": -23
}
print(add_dict_values(myDict))

>>> -21
```
