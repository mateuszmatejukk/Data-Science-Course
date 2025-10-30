---

## Escape Characters

| Escape | Description  | Example Output                           |
| :----- | :----------- | :--------------------------------------- |
| `\n`   | New line     | `"Hello\nWorld"` →<br>`Hello`<br>`World` |
| `\t`   | Tab          | `"Hello\tWorld"` → `Hello   World`       |
| `\\`   | Backslash    | `"Hello\\World"` → `Hello\World`         |
| `\'`   | Single quote | `"Hello\'World"` → `Hello'World`         |
| `\"`   | Double quote | `"Hello\"World"` → `Hello"World`         |

```python
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello\\World")
print("Hello\'World")
print("Hello\"World")
```

---

## Case Manipulation

```python
a = 'AbCd'
a.lower(), a.upper(), a.title()
# ('abcd', 'ABCD', 'Abcd')
```

---

## Whitespace Handling

```python
b = "  Ala ma kota  \n"
b.strip()  # 'Ala ma kota'
```

---

## String Alignment

```python
text = "Align"
text.center(20, "-")  # '-------Align--------'
text.ljust(20, "-")  # 'Align---------------'
text.rjust(20, "-")  # '---------------Align'
```

---

## String Replacement

```python
text = 'Hello world!'
text.replace('world', 'python')  # 'Hello python!'
```

> **To Do:** Learn about **regex (regular expressions)** for more powerful text manipulation.

---

## Membership Operator

```python
text = 'abcd'
'a' in text  # True
'n' in text  # False
'n' not in text  # True
```

---

## Counting and Finding

```python
text = 'banana'
text.count('a')  # 3
text.find('a')  # 1   (first occurrence)
text.rfind('a')  # 5   (last occurrence)
```

---

## String Starts and Ends

```python
text = 'Hello world'
text.startswith('Hel')  # True
text.endswith('abc')  # False
```

---

## String Testing Methods

```python
text = "Hello123"
text.isalnum()  # True (letters + digits)

text = "12345"
text.isdigit()  # True
int(text) / 2  # 6172.5
# text/2 → TypeError (strings can’t be divided)
```

```python
text = "hello"
text.islower()  # True

text = "HELLO"
text.isupper()  # True

text = "   "
text.isspace()  # True
```

