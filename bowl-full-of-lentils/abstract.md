
# Bowl Full of Lentils

In this talk we will introduce ourselves to the configuration language, Dhall.
We will discuss the importance of Dhall in the configuration language space. It chooses
a unique set of features such as being total, safe, strong and statically types, and strongly
normalising. We will examine of this differs to its cousins JSON and YAML and what advantages it
provides over these configuration languages.

We will get a complete understanding of the language by examining these features, examining
them under the lens of its native types and functions, from Text and Naturals to Records and Unions types.
We will showcase the power and safety by looking at the use of functions and types to define some simple
configurations.

Once we have a good understanding of the language itself we will will introduce the
dhall-bhat library. The library encompasses many of the familiar concepts functional
programmers encounter, such as Functors, Applicatives, and Monads, as well as common
types we use such as Either, State, and Reader.

With a basic understanding of the functional programming library we will discuss a normalisation
problem that occurs with Dhall's merge function being nested on Union types. We will then show
how this nesting can be alleviated by utilising Yoneda to normalise expressions reducing the total
expression size input.

We will finish by introducing dada, a Dhall library that defines and ecosystem for recursion schemes.
Without going into to much detail around recursion schemes we will discuss how combining dhall-bhat
and dada we can write a domain specific configuration language. We will examine how this configuration
language acts a pure definition of a configuration that can be interpreted into the Haskell runtime
system to be executed.

