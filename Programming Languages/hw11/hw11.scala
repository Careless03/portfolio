object hw11 extends hwtest.hw("CS478"):
  def userName = "Aden Clymer"

  // // I CERTIFY THAT I HAVE COMPLETELY DOCUMENTED ALL
  // SOURCES THAT I USED TO COMPLETE THIS ASSIGNMENT AND THAT
  // I ACKNOWLEDGED ALL ASSISTANCE I RECEIVED IN THE
  // COMPLETION OF THIS ASSIGNMENT.f
  // Aden Clymer
  // Sources:
  // https://docs.scala-lang.org/scala3/book/fun-anonymous-functions.html
  // I read the above source on anonymous functions and lambdas on how to utilize
  // and implement them for the problems I was given.

  // Dr. O assisted me on 11/14/2024 by assisting and helping develop my thought
  // process when approaching problem 1. He also informed me that since both
  // horizontal and vertical routes are infinite, that .toList() would not work.

  //////////////////////////////////////////////////////////////////////
  // PROBLEM 1

  def diagonalize(ioi: Iterator[Iterator[Int]]): Iterator[List[Int]] =
    // assume that both the outer iterator and the inner iterators are
    // are infinitely long
    // also, "ioi" is supposed to mean "iterator of iterators"

    new Iterator[List[Int]]:
      def hasNext = true // this is infinite, so it will never run out
      var itList = List.empty[Iterator[Int]]

      def next(): List[Int] =
        var returnList = List.empty[Int]
        itList = ioi.next() :: itList
        for iterators <- itList do returnList = iterators.next() :: returnList
        returnList

  test("diagonalize", diagonalizeWrapper, "iter")

  //////////////////////////////////////////////////////////////////////
  // PROBLEM 2

  type Dict = Int => Option[String] // keys are Ints, values are Strings

  def empty: Dict = _ => None

  // insert a key-value pair into the dictionary
  // (it's fine if the key was already in the dictionary, but if so, looking
  // up the key should return the new value, not the old value)
  def insert(key: Int, value: String, dict: Dict): Dict =
    lambda => if lambda == key then Some(value) else dict(lambda)

  // lookup a key in the dictionary
  // return the appropriate value in a Some, or None if the key is not there
  def lookup(key: Int, dict: Dict): Option[String] = dict(key)

  // delete a key from the dictionary
  // (afterwards, looking up the key in the new dictionary should return None)
  def delete(key: Int, dict: Dict): Dict =
    lambda => if lambda == key then None else dict(lambda)

  // TESTING YOUR DICTIONARY
  // The tester does not support the data structure you've just implemented.
  // Instead, do your testing with asserts. I've supplied a few, but
  // you should add more.

  val readyToTest = true // change to true when you're ready to test!

  registerAction {
    if readyToTest then
      println("Begin dictionary tests")

      assert(lookup(5, empty) == None)
      assert(lookup(5, insert(5, "pig", empty)) == Some("pig"))
      // ADD MORE ASSERTS HERE!
      // Testing inserting a new key
      val dict1 = insert(5, "pig", empty)

      // Testing inserting a new key
      val dict2 = insert(3, "cow", dict1)
      assert(lookup(3, dict2) == Some("cow"))

      // Find an old key
      assert(lookup(5, dict2) == Some("pig"))

      // Testing updating an existing key
      val dict3 = insert(5, "sheep", dict2)
      assert(lookup(5, dict3) == Some("sheep"))
      assert(lookup(3, dict3) == Some("cow"))

      // Testing deleting a key
      val dict4 = delete(5, dict3)
      assert(lookup(5, dict4) == None)
      assert(lookup(3, dict4) == Some("cow"))

      // Testing deleting a non-existent key
      val dict5 = delete(10, dict4)
      assert(lookup(3, dict5) == Some("cow"))
      assert(lookup(10, dict5) == None)

      println("Passed all dictionary tests")
    else println("IGNORING all dictionary tests")
  }

  //////////////////////////////////////////////////////////////////////
  // DO NOT **CHANGE** ANYTHING BELOW HERE!
  // IT'S JUST INFRASTRUCTURE THAT YOU CAN SAFELY IGNORE,
  // BUT IF YOU CHANGE ANYTHING, YOU COULD BREAK IT.
  //
  // You can look at the stuff below, if you're curious,
  // but I don't think you'll find any useful clues...

  def make(lol: List[List[Int]]): Iterator[Iterator[Int]] =
    val row = Iterator.continually(-99)
    lol.map(_.iterator ++ row).iterator ++ Iterator.continually(row)

  def unmake(iol: Iterator[List[Int]]): List[List[Int]] =
    iol.takeWhile(_.forall(_ >= 0)).toList

  def diagonalizeWrapper: List[List[Int]] => List[List[Int]] =
    unmake.compose(diagonalize).compose(make)
