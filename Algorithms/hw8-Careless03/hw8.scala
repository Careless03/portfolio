object hw8 extends hwtest.hw("CS385"):
  def userName = "Aden Clymer"
  // I CERTIFY THAT I DID NOT USE ANY SOURCES OR RECEIVE ANY
  // ASSISTANCE REQUIRING DOCUMENTATION WHILE COMPLETING
  // THIS ASSIGNMENT.
  // Aden Clymer

  import hwtest.mlist.*

  // Used to adjust the info node to it's opposite version
  def switch_front_back(mheader: MHeader[String]): Unit =
    mheader.info match
      case "forward"  => mheader.info = "backward"
      case "backward" => mheader.info = "forward"

  // O(n)
  def reverse1(mheader: MHeader[String]): MHeader[String] =
    // Utilize stack to help with the reversal
    val stack = scala.collection.mutable.Stack[Int]()
    var curr = mheader.front
    // O(n)
    while curr.nonEmpty do
      stack.push(curr.head)
      curr = curr.tail
    curr = mheader.front
    // O(n)
    while curr.nonEmpty do
      curr.head = stack.pop()
      curr = curr.tail
    switch_front_back(mheader)
    mheader

  test("reverse1", reverse1, "mlist")

  //////////////////////////////////////////////////////////////////////
  // O(n)
  def reverse2(mheader: MHeader[String]): MHeader[String] =
    var prev = MList.empty
    var curr = mheader.front
    // O(n) - reversal loop
    while curr.nonEmpty do
      val next = curr.tail
      curr.tail = prev
      prev = curr
      curr = next
    mheader.front = prev
    switch_front_back(mheader)
    mheader

  test("reverse2", reverse2, "mlist")
