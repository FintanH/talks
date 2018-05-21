% Read the Functional Manual – But First We Have To Write It
% Fintan Halpenny
% June 4, 2018

# What we will go through

* Introduction to Myself

* Documentation in Haskell

* Tips, Tricks and Tools

* Call to Action

# This Guy

![It me](me.png)

# This Guy

* Studied Computer Science in Trinity College, Dublin

![Trinity College, Dublin](campanile.jpg)

# This Guy

* First exposure to Haskell in one of our modules

* Banged my head a bit more in the follow up module

* Began to see the light reading Haskell Programming From First Principles

![Haskell]()

# This Guy

* Three years of Python in LogoGrab, sneaking some Haskell in after a while

![LogoGrab]()

# This Guy

* Now working for Formation

* But the learning journey continues

![Formation]()

# Functionally Dependent Documentation

* We're more functional when the documentation is good

* Documentation is the first point of contact

* Imagine trying to read the source code for EVERYTHING.

* Past Fintan can sometimes be smarter than Future Fintan. He should do him the courtesy of reminding him what he was doing.

* Open source documentation will encourage people to help out more.

# Finding the Needle in the Haystack

* When we are working on problems we should know how to search

* Search a package

* Search a module

* Search a function name

* Search a type signature

# How can we search documentation in Haskell?

* We will see a few options that I generally use

* Pick which one suits you best

* We can test the WiFi and do a search

# The OG: Hoogle

* http://haskell.org/hoogle

* First Haskell API Search Engine

* Searches Hackage

* Has a command line tool

# The Alt-Kid: (Reactive) Hoogle

* http://hoogle.haskell.org

* Very similar to original Hoogle

* Reactive interface, i.e. searches change as you type

* Results can differ

# The New Kid on the Block: Stackage

* http://stackge.org

* Searches Stackage snapshots

* Snapshots are the LTS resolvers you use with Stack

* Can explore snapshot libraries which is very useful
  * e.g. seeing the history of versions of a library

# Building a Framework to Work In

* It can be too easy to let documentation to slip

* We want to be able to have a way of thinking about documentation

* And create an iterative process of how we document

* Easiest way is to break up documentation into distinct categories

# Categories of Documentation

* So when I think about documentation, I think of a few categories

* Documentation through types

* Documentation through naming and descriptions

* Documentation through usage and tutorials

* Documentation through blog posts (similar to tutorials but more free form)

# Types as Documentation

* First let us look at a few problems

* What is the issue here:

```haskell
getUser :: Text -> Text -> IO User
```

* How many implementations does this have:

```haskell
arithmetic :: Int -> Int -> Int
```

* Types get us very far, but thankfully we can do better than the above

* Let us talk about domains

# Domain of Machine Integers

* What is our domain here?

```haskell
Int -> Int
```

# Domain of Natural numbers

* What is our domain here?

```haskell
Natural -> Natural
```

# Domain of Identity Computation and String of Characters

* What is our domain here?

```haskell
Identity String -> String
```

# Domain of Here be Dragons

* What is our domain here?

```haskell
IO String
```

# Domain of Database Interactions

* What is our domain here?

```haskell
DB User
```

# Constrain Domains

* We can constrain our domains using polymorphic and ad-hoc polymorphic functions

```haskell
-- only one reasonable thing to do
a -> a
-- once again we're constrained to only use `fmap` and we can't do anything with `a`
void :: Functor f => f a -> f ()
-- can follow the types to implement this
dimap :: (a -> b) -> (c -> d) -> (b -> c) -> a -> d
```

* So constraining the types we use benefits us as authors

# Revisit our Int Problem

* Before we had:

```haskell
arithmetic :: Int -> Int -> Int
```

* We can constrain that:

```haskell
arithmetic :: Num a => a -> a -> a
```

* Or even more:

```haskell
arithmetic :: Ring a => a -> a -> a
```

# Repurposing Domains

* We can be more specific about the domains we're working in

* `newtype` your `Text`, `String` and `Int` types!

# Pop Quiz

* Which is better?

```haskell
type Username = Text
```

```haskell
newtype Username = Username { unUserName :: Text }
```

# What's the Difference?

```haskell
type Username = Text
-- definition
lookupUser :: Username -> User

-- use
-- can use any kind of text
lookupUser "absolute-garabage"
```

```haskell
newtype Username = Username { unUserName :: Text }`
-- definition
lookupUser :: Username -> User

-- make sure we don't pass in garbage
validateUsername :: Text -> Validation Error Username

-- use
lookupUser <$> validateUsername "Fintan Halpenny"
```

# One More Example

```haskell
newtype Db a = Db
  { runDb :: Pool
          -> ReaderT SqlBackend (IO a)
  }
```

* We know that we're only interacting with DB related functionality and not just arbitrary IO

# Revisiting our getUser Problem

* We had:

```haskell
getUser :: Text -> Text -> IO User
```

* Learning from our `newtype` technique:

```haskell
newtype Username = Username { unUserName :: Text }

-- purposefully don't have a Show instance for Password
newtype Password = Password { unPassword :: Text }

newtype DB = { runDB :: etc. }

getUser :: Username -> Password -> DB User
```

# Names and Descriptions

* You've gotten to the point of having this abstract thing in your head (maybe on paper)

* Next step is you're going to define it for realz

* Here we come to naming and describing things

# Domains, Domains, Domains

* Talk the language of your domain, if possible

* This will help _you_ know what to write

* And help _others_ know what to search

# Example: Banking

```haskell
data Account = Account
  { accUser :: User
  , accNumber :: AccountNumber
  , accBalance :: Balance
  }

data Balance = Balance { unBalance :: Money }

withdraw :: Account -> Maybe Money

deposit :: Money -> Account
```

# Example: Algebra

```haskell

data Vector n a
data Matrix n m a

multMat :: Num a
        => Matrix n m a
        -> Matrix m p a
        -> Matrix n p a

dotProduct :: Num a => Vector n a -> Vector n a -> a
```

# Naming your Sheds

* Naming things can be hard

* But it can also be fun!

* Use something memorable and mnemonic

  * Terrafomo – a Terraform library

  * Esqueleto – a SQL EDSL

  * Weeder – tool for removing unused pieces of your code base

# Describing the Madness

* Don't let descriptions live in your head

* When writing functions and things get hairy

  * Don't: Write it and leave it as is

  * Do: Write a description of what the function achieves

  * Do: Write intermediate comments for smaller parts

# Help the n00bs

* When describing things assume the least amount of knowledge as possible

* This helps _you_ by making you understand what you're writing in its simplest terms

* This helps _others_ by helping them understand when coming to your library

* Never use the words "obvious" or "obviously"
