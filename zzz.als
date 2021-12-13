sig A {}

pred at_least_one_a {
  some A
}

pred more_than_one_a {
  at_least_one_a and not one A
}

run more_than_one_a