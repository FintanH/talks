let liftA2 =
      https://raw.githubusercontent.com/FormationAI/dhall-bhat/master/Applicative/liftA2

let List/applicative =
      https://raw.githubusercontent.com/FormationAI/dhall-bhat/master/List/applicative

let Hyperparameters = ./Hyperparameters.dhall

in    λ(gammas : List Double)
    → λ(cs : List Double)
    → liftA2
      List
      List/applicative
      Double
      Double
      Hyperparameters
      (λ(gamma : Double) → λ(c : Double) → { gamma = gamma, C = c })
      gammas
      cs
