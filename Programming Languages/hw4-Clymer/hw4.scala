object hw4 extends hwtest.hw("CS478"):
  def userName = "Aden Clymer"

  // Fill in and sign the appropriate statement of assistance below
  // as described in DAAW Appendix B1

  // I CERTIFY THAT I HAVE COMPLETELY DOCUMENTED ALL SOURCES THAT I USED TO
  // COMPLETE THIS ASSIGNMENT AND THAT I ACKNOWLEDGE ALL ASSISTANCE I RECEIVED
  // IN THE COMPLETION OF THIS ASSIGNMENT.

  // Matthew Wanta suggested that I look on the course website and utilize the
  // for-comprehension method to solve for my problem 2. This occured on 9/11/2024 at approxiametely 2100 via text.

  // I utilized the course website found at: https://eecscourses.westpoint.edu/courses/cs478/options.html
  // to solve many of my problems

  // While attempting to solve with tuples I utilized the following website for
  // documentation assistance.
  // https://docs.scala-lang.org/overviews/scala-book/tuples.html

  ////////////////////////////////////////
  // PROBLEM 1

  def parse1(list: List[Char]): Boolean =
    // use a recursive helper function!
    // Read the code
    // Check for the following '&', '|', and '!'
    def parse1helper(list2: List[Char]): (Boolean, List[Char]) =
      // the below code was inspired by the in class notes
      // cases were used because if statements were throwing me errors that I could
      // not figure out for the life of me why. 3 hours were spent trying to solve
      // the issue of that if statement
      list2 match
        case Nil         => throw new Exception("End of Input")
        case 'T' :: tail => (true, tail)
        case 'F' :: tail => (false, tail)

        case '|' :: tail =>
          val (leftExpr, rest1) = parse1helper(tail)
          val (rightExpr, rest2) = parse1helper(rest1)
          (leftExpr || rightExpr, rest2)

        case '&' :: tail =>
          val (leftExpr, rest1) = parse1helper(tail)
          val (rightExpr, rest2) = parse1helper(rest1)
          (leftExpr && rightExpr, rest2)

        case '!' :: tail =>
          val (expr, rest) = parse1helper(tail)
          (!expr, rest)

        case _ :: _ => throw new Exception("It was throwing an error otherwise")

    val (result, ending) = parse1helper(
      list
    ) // based off of scala tuple documentation
    result

  test("parse1", parse1, "list")

  ////////////////////////////////////////
  // PROBLEM 2

  def parse2(str: String): Option[Boolean] =
    // use a recursive helper function!
    if (
      str.isEmpty ||
      (str(0) != 'T' &&
        str(0) != 'F' &&
        str(0) != '|' &&
        str(0) != '&' &&
        str(0) != '!')
    ) then
      None // this is ineffiecient but the best I have, couldn't figure out a grammar checker
    else
      def parse2helper(index: Int): Option[(Boolean, Int)] =
        if (index >= str.length) then None
        else
          str(index) match
            case 'T' => Some((true, index + 1))
            case 'F' => Some((false, index + 1))
            case '&' =>
              for // This for-comprehension was suggested by matthew wanta
                (leftExpr, rest1) <- parse2helper(index + 1)
                (rightExpr, rest2) <- parse2helper(rest1)
              yield (leftExpr && rightExpr, rest2)
            case '|' =>
              for // This for-comprehension was suggested by matthew wanta
                (leftExpr, rest1) <- parse2helper(index + 1)
                (rightExpr, rest2) <- parse2helper(rest1)
              yield (leftExpr || rightExpr, rest2)
            case '!' =>
              for (expr, rest) <- parse2helper(index + 1)
              yield (!expr, rest)
      parse2helper(0).map(_._1) // Based off of Options on course website

  test("parse2", parse2, "str")
