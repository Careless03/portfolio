object hw8 extends hwtest.hw("CS478"):
  def userName = "Aden Clymer"

  // DON'T FORGET TO INCLUDE ANY NEEDED DOCUMENTATION AS INLINE
  // COMMENTS, EITHER JUST ABOVE OR JUST BELOW THE POINT IN THE CODE
  // WHERE THE DOCUMENTATION IS RELEVANT!

  // I CERTIFY THAT I HAVE COMPLETELY DOCUMENTED ALL
  // SOURCES THAT I USED TO COMPLETE THIS ASSIGNMENT AND THAT
  // I ACKNOWLEDGED ALL ASSISTANCE I RECEIVED IN THE
  // COMPLETION OF THIS ASSIGNMENT.

  // Aden Clymer

  // CDT Satvik '26 textually assisted when I struggled to not utilize variables on Problem 3. I had solved the problem but was utilizing a var diff and saving it as a tuple before find the difference as a return value. I described my problem to CDT Satvik and he told me that I should utilize a match to finish up the code.

  type CompactedList = List[(String, List[(Char, List[Int])])]
  type ExpandedList = List[(String, Char, Int)]

  def expand(compactedList: CompactedList): ExpandedList =
    compactedList.flatMap(set =>(set._2.flatMap(item => item._2.map(int => (set._1, item._1, int)))))
  test("expand", expand, "compactedList")


  def squishAndRemoveOddsAndSingletons(data: List[Array[Option[Set[Int]]]]): List[Set[Int]] =
    data.flatMap(_.filter(_.isDefined).map(_.get.filter(_%2==0))).filter(_.size != 1)
  test("squishAndRemoveOddsAndSingletons", squishAndRemoveOddsAndSingletons, "data")


  // assume the list has at least two elements
  // assume the result will NOT overflow an Int
  def greatestDiff(list: List[Int]): Int =
    list.foldRight(Int.MaxValue,Int.MinValue)(
      (item,acc) =>
        (math.min(item, acc._1), math.max(item, acc._2))
    ) match // The idea for a match was given by CDT Sadvik on 17OCT24 when I struggled on how I could avoid utilizing a variable.
      case Tuple2(_1, _2) => Math.abs(_2-_1)
  test("greatestDiff", greatestDiff, "list")

  //why god why
  def combos(xs: List[Int], ys: List[Char]): List[(Int,Char)] =
    xs.foldRight(List.empty[(Int, Char)])( //List.empty[Int, Char] == A
      (intX, acc) => // acc == A
        // function that pulls in ys
        ys.foldRight(acc)( // needs same type: A
          (charY, acc) =>
            //low level and high level combined
            (intX, charY) :: acc
        )
    )
  test("combos", combos, "xs", "ys")
