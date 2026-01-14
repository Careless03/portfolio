object hw4 extends hwtest.hw("CS385"):
  def userName = "Aden Clymer"

  // Fill in and sign the appropriate statement of assistance below
  // as described in DAAW 2024 Appendix B.C.1 (pages 30-31)
  // I CERTIFY THAT I DID NOT USE ANY SOURCES OR RECEIVE ANY
  // ASSISTANCE REQUIRING DOCUMENTATION WHILE COMPLETING
  // THIS ASSIGNMENT.
  // Aden Clymer

  //////////////////////////////////////////////////
  // Problem 1

  // O(n log n)
  def howManyRooms(reservations: List[(Int, Int)]): Int =
    if reservations.length == 0 then 0
    else
      // Step 1 - convert reservations into a check in and check out with values
      // +1  for check in
      // -1 for check out
      val stays =
        reservations.flatMap(x => List((x._1, 1), (x._2, -1))) // O(n)
      // Step 2 - sort events by same day, then by check in
      val sorted_stay = stays.sortBy(x => (x._1, -x._2)) // O(nlogn)
      // Step 3 - Go through all the sorted events and count them up
      var current_rooms = 0
      var max_rooms = 0
      for stay <- sorted_stay do // O(n)
        current_rooms += stay._2
        max_rooms = max_rooms max current_rooms // O(1)
      max_rooms
  test("howManyRooms", howManyRooms, "reservations")

  //////////////////////////////////////////////////
  // Problem 2

  // O(2^n)
  // The number of recursive calls grows exponentially
  def mostMoney(donations: Array[Int]): Int =
    val res = Array.fill(donations.length + 1)
    for i <- arr.length - 1 until 0 by -1 do
      res(i) = (arr(i) + res(i + 2)) max res(i + 1)

  test("mostMoney", mostMoney, "donations")
