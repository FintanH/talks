# Bowl Full of Lentils

Copy-paste is a ubiquitous tool in a programmer's box of shortcuts. Sometimes we just
don't care that we're repeating ourselves because we need this thing fast. This is even
more so when it comes to configurations. We are all guilty of taking an existing configuration
file, copying its content and changing a few values. JSON and YAML do not have enough expressive
power to avoid this effectively. But what if I told you there was something that does have this
power? What if I told you we could DRY up our configuration files and practice functional programming
at the same time? What will you choose the red pill or the blue pill?

In this talk we will introduce ourselves to the configuration language, Dhall.
We will discuss the importance of Dhall in the configuration language space. Dhall chooses
a unique set of features such as being total, safe, strong & statically typed, and strongly
normalising, giving us the expressive power that we deserve in our configuration language.
We will examine how Dhall differs from its cousins JSON and YAML and what advantages it
provides over these configuration languages.

We will get a complete understanding of the language by examining its features under the lens of its native types and functions,
from Text and Naturals to Records and Unions. With a grounding in the types that we can work with in Dhall, we will go through
a configuration file that is geared for tuning a (mock) machine learning model, seeing how painful it is to copy and paste these
in JSON, and making it all-so-much-better by using Dhall instead.

We will alleviate the pain of configurations even more by introducing the dhall-bhat library. We will
take a tour of the library and get familiar with the functional concepts it has to offer. We will look at
such concepts as Functors, Applicatives, and Monads. We will also look at types that we commonly come across,
such as Either, State, and Reader. We will then look through the previous example of a machine learning configuration
and apply some functional techniques to get an even DRYer implementation.

Attendees are recommended to have some familiarity with the functional concepts mentioned above, but are not required.
