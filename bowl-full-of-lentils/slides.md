
# It Me

A quick explanation of who I am, who I work for

# Dhall

* https://dhall-lang.org/

* Dhall - The non-repetitive alternative to YAML

* You can think of Dhall as: JSON + functions + types + imports

* Not Turing-complete

# Dhall - Features

* Built-in types

* Functions

* Records

* Unions


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
```

(stdin):1:1

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

# Optional

# Unit

# Records

# Unions

# Let

# Functions

# Imports

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
