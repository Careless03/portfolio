object hw3 extends hwtest.hw("CS478"):
  def userName = "Aden Clymer"

  // Fill in and sign the appropriate statement of assistance below
  // as described in DAAW Appendix B1

  //////////////////////////////////////////////////////////////////////
  // Problem 1
  // Write a context-free grammar for strings that would match the regular
  // expression a*b*, but that contain no more than twice as many of one
  // letter than the other letter.
  //
  // Problem 2
  // Write a context-free grammar for strings that would match the regular
  // expression (a|b)*, but that contain strictly more as than bs.
  //////////////////////////////////////////////////////////////////////

  /*
    Write your first context-free grammar below:
      S = aXb | Xb | aX | ab | -
      X = aSb

    Write your second context-free grammar below:
      S = a | XaX
      X = - | SbS | XaX
  */


  // Write an implementation of the "itemsAndIndexes" function below:
  def itemsAndIndexes(L: List[String]): List[(String, Int)] =
    def itemsHelper(L: List[String], index: Int): List[(String, Int)] =
      L match
        case Nil => Nil
        case h::t =>
          (h, index) :: itemsHelper(t, index+1)
    itemsHelper(L, 0)

  // Provide justification of your function's correctness (as a comment) below:
  // I had to make a helper funciton in order for this to work.
  // The helper helps keep track of the index as it iterates through.
  // It then pattern matches the List. I have a base case of NIL, then I moved
  // on to looking for a h::t pattern.
  // I then took that pattern and made it into a tuple with the header and the
  // index  then appended that to the helper funciton recursively
