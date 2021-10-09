# Planning

## Member variables

* `correct_word` will be stored as a list for easy parsing

* `guess_list` is the list that is displayed to the user

## Member functions

* `display()`:

   * the number of attempts **left**

   * underscores for correct word

      * Correct word

```
Number of attemps: x


_ _ _ _ _ _ _
```

* `get_game_guess()` - gets a guess

* `validate_guess()` - validate user guess

* `end_game()` - determine if we should end game right now. Return True if game
should end now, false if it shouldn't

   * Game will end if user has gotten all letters correct. No underscores in
   `guess_list`

  


