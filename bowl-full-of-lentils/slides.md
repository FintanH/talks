
# It Me

A quick explanation of who I am, who I work for

# Dhall

Give a brief background on Dhall

# Dhall - Features

List the primary dhall features that we will discuss

TODO: Go to blog post to take examples of language features. Make sure they're up to date

# Dhall - Feature 1

# Dhall - Feature 2 etc.

# Use Case - Machine Learning Configuration

TODO: Look into maybe a logisitic/linear regression model and have a way to configure them via CLI

Then can do:

```bash
for config in `dhall <<< "./learner [input1, input2, input3, input4]"`
  ./runModel $config >> config.results
end
```

