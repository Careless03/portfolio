object hw3 extends hwtest.hw("CS385"):
  def userName = "Aden Clymer"
  // Fill in and sign the appropriate statement of assistance below
  // as described in DAAW 2024 Appendix B.C.1 (pages 30-31)
  // I CERTIFY THAT I DID NOT USE ANY SOURCES OR RECEIVE ANY
  // ASSISTANCE REQUIRING DOCUMENTATION WHILE COMPLETING
  // THIS ASSIGNMENT.
  // Aden Clymer

  // IMPORTANT! IMPORTANT! IMPORTANT!
  // This file will include your code, but your ANALYSIS must
  // be turned in as an "analysis.pdf" file in your GitHub repo!

  //////////////////////////////////////////////////
  // Problem 1 Code

  // return true if the target is present, or false if it's not
  // your analysis should go in the PDF
  def binarySearch(target: Int, list: List[Int]): Boolean =
    // define a helper function here to do all the real work
    def helper(low: Int, high: Int): Boolean =
      if low > high then false
      else
        val mid = (high + low) / 2
        val midVal = list(mid)
        if midVal == target then true
        else if midVal > target then helper(low, mid - 1)
        else helper(mid + 1, high)
    // kick off the helper function
    helper(0, list.length - 1)

  test("binarySearch", binarySearch, "target", "list")

  //////////////////////////////////////////////////
  // Problem 2 Code

  // return true if the target is present, or false if it's not
  // your analysis should go in the PDF
  def binarySearchWithChop(target: Int, list: List[Int]): Boolean =
    // define a helper function here to do all the real work
    def helper(curr_list: List[Int], length: Int): Boolean =
      if length <= 0 then false
      else
        val mid = length / 2
        val midVal = curr_list(mid)
        if midVal == target then true
        else if midVal > target then helper(curr_list, mid)
        else helper(curr_list.drop(mid + 1), length - (mid + 1))
    // kick off the helper function
    helper(list, list.length)
  test("binarySearchWithChop", binarySearchWithChop, "target", "list")
