# Strings 

Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points.

```py
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
```

Return a string version of object. If object is not provided, returns the empty string. 

```py
print(str(b'Zoot!')) # Output: b'Zoot!'
```

## Formatted strings

Python formatted strings (also known as f-strings) are a convenient way to embed expressions within string literals. They allow for easy and readable string interpolation.
```py
name = "Ariel"
age = 26
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is Ariel and I am 25 years old.
```


## Commonly used methods

### str.capitalize()
Return a copy of the string with its first character capitalized and the rest lowercased.

```py
print(str('learning python with official docs at: docs.python.org').capitalize())
# Output: Learning python with official docs at: docs.python.org
```

### str.lower()
Return a copy of the string with all the cased characters [4] converted to lowercase

```py
print("MY CAT ATE A FISH".lower())
# Output: my cat ate a fish
```

### str.casefold()
Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.

> Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. For example, the German lowercase letter 'ß' is equivalent to "ss". Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss".

```py
print(str('Try python in the Newest version 3.11').casefold())
# Output: try python in the newest version 3.11
```

### str.title()
Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.

For example:
```py
print("they're bill's friends from the UK".title())
# Output: They'Re Bill'S Friends From The Uk
```


### str.count(sub[, start[, end]])
Return the number of non-overlapping occurrences of substring sub in the range [start, end]. Optional arguments start and end are interpreted as in slice notation.

If sub is empty, returns the number of empty strings between characters which is the length of the string plus one.

```py
# string in which occurrence will be checked
string = "geeks for geeks"
 
print(string.count("geeks", 0, 5))
# Output: 1
print(string.count("geeks", 0, 15))
# Output: 2
print(string.count("geeks", 0, 3))
# Output: 0
```

### str.encode(encoding='utf-8', errors='strict')
Return the string encoded to bytes.

encoding defaults to 'utf-8'; see [Standard Encodings](https://docs.python.org/pt-br/3/library/codecs.html#standard-encodings) for possible values.

```py
print("My cat eat my fish".encode("utf-8"))
# Output: b'My cat eat my fish'
```



### str.find(sub[, start[, end]])
Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.

```py
text = "Hello, world!"
index = text.find("world")
print(index)  # Output: 7
```

You can also specify optional start and end positions to limit the search range.

```py
text = "Hello, world!"
index = text.find("world", 0, 5)
print(index)  # Output: -1 (not found within the range 0 to 5)
```

### str.removeprefix(prefix, /)
If the string starts with the prefix string, return string[len(prefix):]. Otherwise, return a copy of the original string:
```py
print('TestHook'.removeprefix('Test'))
# Output: Hook
print('BaseTestCase'.removeprefix('Test'))
# Output: BaseTestCase
```

### str.removesuffix(suffix, /)
If the string ends with the suffix string and that suffix is not empty, return string[:-len(suffix)]. Otherwise, return a copy of the original string:

```py
print('MiscTests'.removesuffix('Tests'))
# Output: Misc
print('TmpDirMixin'.removesuffix('Tests'))
# Output: TmpDirMixin
```

### str.join()
The join() method concatenates elements of an iterable (like a list) into a single string, with each element separated by the string that calls join().
This is useful for joining lists of strings into a single string.

```py
words = ["Hello", "world"]
sentence = " ".join(words)
print(sentence)  # Output: Hello world
```

### str.replace()
The replace() method replaces all occurrences of a specified substring with another substring. It returns a new string, leaving the original string unchanged.

```py
text = "Hello, world!"
new_text = text.replace("world", "Python")
print(new_text)  # Output: Hello, Python!
```

You can also specify an optional count argument to limit the number of replacements.

```py
text = "apple apple apple"
new_text = text.replace("apple", "orange", 2)
print(new_text)  # Output: orange orange apple
```

### str.split()
The split() method splits a string into a list, using the specified delimiter. By default, it splits by any whitespace. You can also provide an optional maxsplit argument, which limits the number of splits.

```py
text = "apple, banana, cherry"
fruits = text.split(", ")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
```

If no delimiter is provided, split() splits by whitespace.

```py
text = "Hello   world"
words = text.split()
print(words)  # Output: ['Hello', 'world']
```

### str.startswith()
The startswith() method checks if a string begins with a specified prefix and returns True if it does, otherwise False.
You can also specify an optional start and end range to limit the check.

```py
text = "Hello, world!"
result = text.startswith("Hello")
print(result)  # Output: True
```

### str.endswith()
The endswith() method checks if a string ends with a specified suffix and returns True if it does, otherwise False.
You can also specify an optional start and end range to limit the check.

```py
text = "Hello, world!"
result = text.endswith("world!")
print(result)  # Output: True
```