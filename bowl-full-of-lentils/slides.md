
# It Me

A quick explanation of who I am, who I work for


# Dhall

* https://dhall-lang.org/

* Dhall - The non-repetitive alternative to YAML

* You can think of Dhall as: JSON + functions + types + imports

* Not Turing-complete


# Dhall - Features

* Built-in types

* Records

* Unions

* Functions

* Let/Imports


# Bool - Type

```bash
$ dhall type <<< "True"
Bool
```

# Bool - Example 1

```bash
$ dhall <<< "True && False"
False
```
# Bool - Example 2

```bash
$ dhall <<< "True && True"
True
```

# Bool - Example 3

```bash
$ dhall <<< "True || False"
True
```

# Bool - Example 4

```bash
$ dhall <<< "False || False"
False
```


# Natural - Type

```bash
$ dhall type <<< "0"
Natural
```

# Natural - Example 1

```bash
$ dhall <<< "1 + 1"
2
```

# Natural - Example 2

```bash
$ dhall <<< "1 + 0"
1
```

# Natural - Example 3

```bash
$ dhall <<< "1 * 1"
1
```

# Natural - Example 4

```bash
$ dhall <<< "1 * 0"
0
```


# Integer - Type

```bash
$ dhall type <<< "-1"
Integer
```

# Integer - Example 1

```bash
$ dhall <<< "-1"
-1
```

# Integer - Example 2

```bash
$ dhall <<< "+1"
+1
```

# Integer - Example 3

```bash
$ dhall <<< "-1 + -2"
Use "dhall --explain" for detailed errors

Error: <+> only works on <Natural>s

-1 + -2

(stdin):1:1
```


# Double - Type

```bash
$ dhall type <<< "3.14"
Double
```

# Double - Example 1

```bash
$ dhall <<< "3.14"
3.14
```

# Double - Example 2

```bash
$ dhall <<< "Infinity"
Infinity
```

# Double - Example 3

```bash
$ dhall <<< "-Infinity"
-Infinity
```

# Double - Example 4

```bash
$ dhall <<< "3.14 * (3.0 * 3.0)"
Use "dhall --explain" for detailed errors

Error: <*> only works on <Natural>s

3.14 * (3.0 * 3.0)

(stdin):1:1
```


# Text - Type

```bash
$ dhall type <<< '"Hello, World!"'
Text
```

# Text - Example 1

```bash
$ dhall <<< '"I <3 Dhall"'
"I <3 Dhall"
```

# Text - Example 2

```bash
$ dhall <<< '"I" ++ " <3 " ++ "NYC"'
"I <3 NYC"
```

# Text - Example 3

```bash
$ dhall
''
    #!/bin/bash

    echo "Hi!"
''
<Ctrl-D>
''
    #!/bin/bash

    echo "Hi!"
''
```


# List - Type

```bash
$ dhall type <<< "[1, 2, 3]"
List Natural
```

# List - Example 1

```bash
$ dhall <<< "[1, 2, 3] # [4, 5, 6]
[ 1, 2, 3, 4, 5, 6 ]
```

# List - Example 2

```bash
$ dhall <<< "
List/fold
  Bool
  [True, False, True]
  Bool
  (\(x : Bool) -> \(y : Bool) -> x && y)
  True
"
False
```

# List - Example 3

```bash
$ dhall <<< "List/length Natural [1, 2, 3]"
3
```


# Optional - Type

```bash
$ dhall type <<< "None Natural"
Optional Natural
```

# Optional - Example 1

```bash
$ dhall type <<< "Some 1"
Optional Natural
```

# Optional - Example 2

```bash
$ dhall <<< '
Optional/fold
  Text
  (Some "ABC")
  Text
  (\(t : Text) -> t)
  "Uhoh"
'
"ABC"
```

# Optional - Example 3

```bash
$ dhall <<< '
Optional/fold
  Text
  (None Text)
  Text
  (\(t : Text) -> t)
  "Uhoh"
'
"Uhoh"
```


# Unit

```bash
$ dhall type <<< "{=}"
{}
```

```bash
$ dhall <<< "{=}
{=}
```


# Records - Type

```bash
dhall type <<< "
{ name : Text, age : Natural, email : Text }
"
Type
```

# Records - Example 1

```bash
dhall <<< "
{ name : Text, age : Natural, email : Text }
"
{ age : Natural, email : Text, name : Text }
```

# Records - Example 1

```bash
dhall type <<< '
{ name = "Fintan", age = 26, email = "finto@haps.com" }
'
{ age : Natural, email : Text, name : Text }
```

# Records - Example 1

```bash
dhall <<< '
{ name = "Fintan", age = 26, email = "finto@haps.com" }
'
{ age = 26, email = "finto@haps.com", name = "Fintan" }
```

# Records - Example Type Annotation

```bash
dhall <<< '
{ name = "Fintan" } : { name : Text, age : Natural }
'
Error: Expression doesn\'t match annotation

{ + age : …
, …
}

{ name = "Fintan" } : { name : Text, age : Natural }
```

# Records - Example Projection 1

```bash
dhall <<< '{ name = "Fintan", age = 26 }.age'
26
```

# Records - Example Projection 2

```bash
dhall <<< '{ name = "Fintan", age = 26 }.{ age, name }'
{ age = 26, name = "Fintan" }
```

# Unions - Type

```bash
$ dhall type <<< "
< Monday
| Tuesday
| Wednesday
| Thursday
| Friday
>
"
Type
```

# Unions - Example Enum

```bash
$ dhall <<< "
< Monday
| Tuesday
| Wednesday
| Thursday
| Friday
>
"
< Friday | Monday | Thursday | Tuesday | Wednesday >
```

# Unions - Example Enum Constructor

```bash
$ dhall <<< "
< Monday
| Tuesday
| Wednesday
| Thursday
| Friday
>.Monday
"
<Friday | Monday | Thursday | Tuesday | Wednesday>.Monday
```

# Unions - Example Eliminator

```bash
$ dhall <<< "
merge
{ Monday = True
, Tuesday = False
, Wednesday = False
, Thursday = False
, Friday = False
}
<Monday | Tuesday | Wednesday | Thursday | Friday>.Monday
"
True
```

# Unions - Example Sum Type

```bash
$ dhall <<< "< IsNat : Natural | IsText : Text >"
```

# Unions - Example Sum Type Constructor

```bash
$ dhall type <<< "
< IsNat : Natural | IsText : Text >.IsNat
"
∀(IsNat : Natural) → < IsNat : Natural | IsText : Text >
```


# Functions - Type

```bash
$ dhall type <<< "\(x : Natural) -> x + 1"
∀(x : Natural) → Natural
```

# Functions - Example

```bash
$ dhall <<< "\(x : Natural) -> x + 1"
λ(x : Natural) → x + 1
```

# Functions - Example Evaluation 1

```bash
$ dhall <<< "(\(x : Natural) -> x + 1) 41"
42
```

# Functions - Example Evaluation 2

```bash
$ dhall <<< '
   ( \(a : Type)
  -> \(b : Type)
  -> \(x : a)
  -> \(y : b)
  -> x
   ) Text Natural "Ignored!" 17
'
"Ignored!"
```


# Let/Imports - Example 1

```bash
$ dhall <<< '
let identity = \(a : Type) -> \(x : a) -> x
in identity Text "It me!"
'
"It me!"
```

# Let/Imports - Example 2

```bash
$ dhall <<< "
let enumerate = https://dhall/Prelude/Natural/enumerate
in enumerate 10
"
[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
```

# Let/Imports - Example 3

```bash
$ dhall <<< "let f = ../identity in f Natural 42"
42
```


# Machine Learning Configuration - SVM

* Support Vector Machine (SVM)

* Simple Script in Python using Scikit-Learn

* Hyperparameter Learning

# SVM - Imports

```python
import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
```

# SVM - Train and Predict

```python
def train_and_predict(X_train, y_train, X_test, y_test, gamma, c, label):
    svc = svm.SVC(kernel="rbf", gamma=gamma, C=c).fit(X_train, y_train)

    print("Training Label: %s" % label)
    print("GAMMA=%f, C=%f" % (gamma, c))
    predictions = svc.predict(X_test) == y_test
    print("PREDICTION=%f\n\n" % (sum(predictions) / len(predictions)))
```

# SVM - Load

# More Tasty Meals

* https://functional.works-hub.com/learn/bowl-full-of-lentils-fcbf3

* https://functional.works-hub.com/learn/yo-yoneda-a2965

* https://kowainik.github.io/posts/2018-09-09-dhall-to-hlint.html

* https://github.com/dhall-lang

# Other Links

* https://scikit-learn.org/stable/index.html

* https://medium.com/all-things-ai/in-depth-parameter-tuning-for-svc-758215394769
