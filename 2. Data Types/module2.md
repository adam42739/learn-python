# Data Types

## Contents

1. [Boolean](#boolean)
2. [Integer](#integer)
3. [String](#string)
4. [Float](#float)
5. [Tuple](#tuple)
6. [List](#list)
7. [Dictionary](#dictionary)

## Boolean

```python
bool

myBool = True
```

## Integer

```python
int

myInt = 5
```

## String

```python
str

myString = "5.0"
```

## Float

```python
float

myFloat = 5.0
```

## Tuple

```python
tuple

myTuple = (5, 5.0, "5.0")
```

Tuples are a colletion of items. The items can be any type including other tuples, lists, or dictionaries. However, tuples do not support item assignment.

```python
myTuple[1] = 6.0
>>> TypeError: 'tuple' object does not support item assignment
```

## List

```python
list

myList = [5, 5.0, "5.0"]
```

Lists are similar to tuples, except they do support item assignmnet

```python
myList[1] = 6.0
print(myList)
>>> [5, 6.0, "5.0"]
```

## Dictionary

Dictionaries are a collection of key-value pairs. Values in a dict can be any type including lists and other dictionaries. Keys on the other hand must be "hashable". The definition of "hashable" is not super important, but think `int`, `float`, and `string` for dictionary keys.

```python
dict

myDict = {
    "key1": 1.0,
    "key2": "1.0",
    "key3": [5, 6.0, "5.0"]
}
```
