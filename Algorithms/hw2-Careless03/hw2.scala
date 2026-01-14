import scala.compiletime.ops.double
object hw2 extends hwtest.hw("CS385"):
  def userName = "Aden Clymer"

  // Fill in and sign the appropriate statement of assistance below
  // as described in DAAW 2024 Appendix B.C.1 (pages 30-31)

  // I CERTIFY THAT I DID NOT USE ANY SOURCES OR RECEIVE ANY
  // ASSISTANCE REQUIRING DOCUMENTATION WHILE COMPLETING
  // THIS ASSIGNMENT.
  // CDT ADEN CLYMER

  //////////////////////////////////////////////////
  // Problem 1
  // K = length of names array
  // T = num of tables
  // C = total # of campers
  // O(K log C) <-- fill in the Big-O running time here!
  def busiestTable(numTables: Int, names: Array[Int]): Int =
    def canSatisfyLimit(sizeLimit: Int): Boolean =
      // returns true if you can distribute the names across the
      // tables with no table receiving more than sizeLimit names
      // Initialize Variables
      var table_sum = 0
      var tables_used = 1
      var can_fit = true

      // Logic for checking tables
      for num_per_letter <- names do
        // checks to if any one group of campers exceed limit on table
        if num_per_letter > sizeLimit then can_fit = false
        // if the campers exceed the currently allowed limit then move to another table
        else if table_sum + num_per_letter > sizeLimit then
          tables_used += 1
          table_sum = num_per_letter
          // Logic to see if we have exceeded number of tables that exist
          if tables_used > numTables then can_fit = false
        // if the campers don't exceed the table limits then simply add them to the table
        else table_sum += num_per_letter
      can_fit

    // find the smallest sizeLimit that works (MUST USE BINARY SEARCH!)
    // min num is max val in names (see if any one group exceeds table limit)
    var left_limit = names.max
    var right_limit = names.sum // max size is total campers

    // loop through and using a binary search method utilizing decrease and conquer
    // It then uses the helper function to determine the table size.
    while left_limit < right_limit do
      val mid = (left_limit + right_limit) / 2
      if canSatisfyLimit(mid) then right_limit = mid
      else left_limit = mid + 1
    left_limit

  test("busiestTable", busiestTable, "numTables", "names")

  //////////////////////////////////////////////////
  // Problem 2

  // O(n log n) <-- fill in the Big-O running time here!
  def numDays(arr: Array[(Int, Int)]): Int =
    // function to merge the split arrays into one
    def merge(
        left: Array[(Int, Int)],
        right: Array[(Int, Int)]
    ): List[(Int, Int)] =
      // initialize variables
      var merged: List[(Int, Int)] = List.empty[(Int, Int)]
      var i = 0
      var j = 0

      // go through the sorted array and add them to merged
      // Before getting added to merge check to see if any dates overlap
      // To check for overlap use overlap handler, this is to avoid any
      // large chunks of code being constantly repeated.

      // Handle merging each of them together.
      while i < left.length && j < right.length do
        if left(i)._1 < right(j)._1 then
          merged = overlapHandler(merged, left(i))
          i += 1
        else
          merged = overlapHandler(merged, right(j))
          j += 1

      // Handle the remainder one at a time
      while i < left.length do
        merged = overlapHandler(merged, left(i))
        i += 1
      while j < right.length do
        merged = overlapHandler(merged, right(j))
        j += 1
      merged

    // This function matches the merged list and adds in a new time
    // and if necessary it overlaps two separate entities.
    def overlapHandler(
        merged: List[(Int, Int)],
        time: (Int, Int)
    ): List[(Int, Int)] =
      merged match
        case Nil => List(time)
        case head :: tail =>
          if head._2 >= time._1 then
            (head._1, math.max(head._2, time._2)) :: tail
          else time :: merged

    // Beginning of code for numDays
    // check to ensure the length is exists
    if arr.length == 0 then 0
    // the below line is unessecary but it this case it true, it significantly
    // reduces the time the code needs to complete
    else if arr.length == 1 then arr(0)._2 - arr(0)._1 + 1
    else
      val sorted = arr.sortBy(_._1)
      val mid = sorted.length / 2 // divide list in half
      val (left, right) = sorted.splitAt(mid) // tuples code, learned in class
      val reservations = merge(left, right) // conquer the step
      reservations
        .map(x => x._2 - x._1 + 1)
        .sum // glue together the outputted list.

  test("numDays", numDays, "arr")

// def numDays_inclass(arr: Array[(Int, Int)]): Int =
//   def canCombine(p1: (Int, Int), p2: (Int, Int)): Boolean =
//     (p1._2 >= p2._1 && p1._1 <= p2._2) || (p2._2 >= p1._1 && p2._1 <= p2._2)
//   def combine(p1: (int, Int), p2: (Int, Int)): (Int, Int) =
//     (p1._1 min p2._1, p1._2 max p2._2)
//   def helper(lo: Int, hi: Int): List[(Int, Int)] =
//     if hi == lo then arr(hi) :: List.empty[(Int, Int)]
//     else if hi - lo then
//       if canCombine(arr(lo), arr(hi)) then combine(arr(lo), arr(hi)) :: List.empty[(Int, Int)]
//       else arr(lo) :: arr(hi) :: List.empty[(Int, Int)]
//     else
//       val mid = (hi+low)/2
//       val left = helper(low, mid-1)
//       val right = helper(mid, hi)
//       ???
