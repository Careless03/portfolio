object hw5 extends hwtest.hw("CS385"):
  def userName = "Aden Clymer"

  // Fill in and sign the appropriate statement of assistance below
  // as described in DAAW 2024 Appendix B.C.1 (pages 30-31)
  // I CERTIFY THAT I DID NOT USE ANY SOURCES OR RECEIVE ANY
  // ASSISTANCE REQUIRING DOCUMENTATION WHILE COMPLETING
  // THIS ASSIGNMENT.
  // Aden Clymer
  //////////////////////////////////////////////////
  // Problem 1

  // State below which version you are doing: brute-force or memoization.
  // Brute Force

  // O(n * 2 ^ n)
  def whoopDeDoos(arr: Array[Int]): Int =
    var best = 0
    def validSeq(subseq: Array[Int]): Boolean =
      if subseq.length < 2 then true
      else
        var is_valid = true
        var first_non_zero = false
        var last_sign = 0
        for i <- 1 until subseq.length do
          val diff = subseq(i) - subseq(i - 1)
          if diff == 0 then is_valid = false
          val curr_sign = if diff > 0 then 1 else -1
          if !first_non_zero then first_non_zero = true
          else if curr_sign == last_sign then is_valid = false
          last_sign = curr_sign
        is_valid

    def helper(idx: Int, subseq: Array[Int]): Unit =
      if idx == arr.length then
        if validSeq(subseq) then best = best max subseq.length
      else
        helper(idx + 1, subseq)
        helper(idx + 1, subseq :+ arr(idx))
    helper(0, Array.empty)
    best

  test("whoopDeDoos (small)", whoopDeDoos, "elevation")
  ignoretest("whoopDeDoos (big)", whoopDeDoos, "elevation")

  //////////////////////////////////////////////////
  // Problem 2

  // State below which version you are doing: brute-force or memoization.
  // memoization

  // O(n ^ 2)
  def dogWalker(requests: Array[(Int, Int, Int)]): Int =
    // each request is (startTime, endTime, paymentOffered)
    // assume payment is > 0
    val sorted = requests.sortBy(_._2)
    val n = sorted.length
    // for each reques store the idx p(i) of the request j so that
    // it ends strictly before i starts, or -1 if none
    val p = Array.fill(n)(-1)
    for i <- 0 until n do
      val (start_i, end_i, pay_i) = sorted(i)
      var j = i - 1
      while j >= 0 do
        val (start_j, end_j, pay_j) = sorted(j)
        if end_j < start_i then
          p(i) = j
          j = -1
        else j -= 1
    // memo for recursion piece
    val memo = Array.fill(n)(-1)
    def helper(i: Int): Int =
      if i < 0 then 0
      else if memo(i) != -1 then memo(i)
      else
        val (start_idx, end_idx, pay_idx) = sorted(i)
        val skip = helper(i - 1)
        val take = pay_idx + helper(p(i))
        val result = skip max take
        memo(i) = result
        result
    helper(n - 1)

  test("dogWalker (small)", dogWalker, "requests")
  test("dogWalker (big)", dogWalker, "requests")
