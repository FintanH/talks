
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


# Bool

```bash
$ dhall type <<< "True"
Bool
```

```bash
$ dhall <<< "True && False"
False
```

```bash
$ dhall <<< "True && True"
True
```

```bash
$ dhall <<< "True || False"
True
```

```bash
$ dhall <<< "False || False"
False
```


# Natural

```bash
$ dhall type <<< "0"
Natural
```

```bash
$ dhall <<< "1 + 1"
2
```

```bash
$ dhall <<< "1 + 0"
1
```

```bash
$ dhall <<< "1 * 1"
1
```

```bash
$ dhall <<< "1 * 0"
0
```


# Integer

```bash
$ dhall type <<< "-1"
Integer
```

```bash
$ dhall <<< "-1"
-1
```

```bash
$ dhall <<< "+1"
+1
```

```bash
$ dhall <<< -1 + -2
Use "dhall --explain" for detailed errors

Error: <+> only works on <Natural>s

-1 + -2

(stdin):1:1
```


# Double

```bash
$ dhall type <<< "3.14"
Double
```

```bash
$ dhall <<< "3.14"
3.14
```

```bash
$ dhall <<< "Infinity"
Infinity
```

```bash
$ dhall <<< "-Infinity"
-Infinity
```

```bash
$ dhall <<< "3.14 * (3.0 * 3.0)
Use "dhall --explain" for detailed errors

Error: <*> only works on <Natural>s

3.14 * (3.0 * 3.0)

(stdin):1:1
```


# Text

```bash
$ dhall type <<< '"Hello, World!"'
Text
```

```bash
$ dhall <<< '"I <3 Dhall"'
"I <3 Dhall"
```

```bash
$ dhall <<< '"I" ++ " <3 " ++ "NYC"'
"I <3 NYC"
```

# Text

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


# List

```bash
$ dhall type <<< "[1, 2, 3]"
List Natural
```

```bash
$ dhall <<< "[1, 2, 3] # [4, 5, 6]
[ 1, 2, 3, 4, 5, 6 ]
```

```bash
$ dhall <<< "
List/fold
  Bool
  [True, False, True]
  Bool
  (\(x : Bool) -> \(y : Bool) -> x && y)
  True
"
"
False
```

```bash
$ dhall <<< "List/length Natural [1, 2, 3]"
3
```


# Optional

```bash
$ dhall type <<< "None Natural"
Optional Natural
```

```bash
$ dhall type <<< "Some 1"
Optional Natural
```

# Optional

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

# Optional

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
$ dhall <<< "{=}"
{}
```

```bash
$ dhall <<< "{=}
{=}
```


# Records

```bash
dhall type <<< "
{ name : Text, age : Natural, email : Text }
"
Type
```

```bash
dhall <<< "
{ name : Text, age : Natural, email : Text }
"
{ age : Natural, email : Text, name : Text }
```

```bash
dhall type <<< '
{ name = "Fintan", age = 26, email = "finto@haps.com" }
'
{ age : Natural, email : Text, name : Text }
```

```bash
dhall <<< '
{ name = "Fintan", age = 26, email = "finto@haps.com" }
'
{ age = 26, email = "finto@haps.com", name = "Fintan" }
```

```bash
dhall <<< '
{ name = "Fintan" } : { name : Text, age : Natural }
'
Error: Expression doesn't match annotation

{ + age : …
, …
}

{ name = "Fintan" } : { name : Text, age : Natural }
```

```bash
dhall <<< '{ name = "Fintan", age = 26 }.age'
26
```

```bash
dhall <<< '{ name = "Fintan", age = 26 }.{ age, name }'
{ age = 26, name = "Fintan" }
```

# Unions

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

```bash
$ dhall <<< "
< Monday
| Tuesday
| Wednesday
| Thursday
| Friday
>.Monday
"
< Friday | Monday | Thursday | Tuesday | Wednesday >.Monday
```

```bash
$ dhall <<< "
merge
{ Monday = True
, Tuesday = False
, Wednesday = False
, Thursday = False
, Friday = False
} < Monday | Tuesday | Wednesday | Thursday | Friday >.Monday
"
True
```


# Functions

```bash
$ dhall type <<< "\(x : Natural) -> x + 1"
∀(x : Natural) → Natural
```

```bash
$ dhall <<< "\(x : Natural) -> x + 1"
λ(x : Natural) → x + 1
```

```bash
$ dhall <<< "(\(x : Natural) -> x + 1) 41"
42
```

```bash
$ dhall <<< '(\(a : Type) -> \(b : Type) -> \(x : a) -> \(y : b) -> x) Text Natural "Ignored!" 17'
"Ignored!"
```


# Let/Imports

```bash
$ dhall <<< 'let identity = \(a : Type) -> \(x : a) -> x in identity Text "It me!"'
"It me!"
```

```bash
$ dhall <<< "let enumerate = https://raw.githubusercontent.com/dhall-lang/dhall-lang/master/Prelude/Natural/enumerate in enumerate 10"
[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
```

```bash
$ dhall <<< "let f = ../identity in f Natural 42"
42
```


# Use Case - Machine Learning Configuration

TODO: Look into maybe a logisitic/linear regression model and have a way to configure them via CLI

Then can do:

```bash
for config in `dhall <<< "./learner [input1, input2, input3, input4]"`
  ./runModel $config >> config.results
end
```

# More Tasty Meals

* https://functional.works-hub.com/learn/bowl-full-of-lentils-fcbf3

* https://functional.works-hub.com/learn/yo-yoneda-a2965

* https://kowainik.github.io/posts/2018-09-09-dhall-to-hlint.html

* https://github.com/dhall-lang
