object hw7 extends hwtest.hw("CS385"):
  def userName = "Aden Clymer"

  // O(K log K + K + log((K * M)/C)*log(K))
  def howManySets(cardsPerStudent: Int, cards: Array[Long]): Long =
    // looks for the position of the target we look for in arr
    def helper(arr: Array[Long], target: Long): Int =
      var low = 0
      var high = arr.length - 1
      while low <= high do
        val mid = (low + high) / 2
        val midVal = arr(mid)
        if midVal < target then
          low = mid + 1
        else if midVal > target then
          high = mid - 1
        else
          return mid
      // no match return negative
      -(low + 1)
    // start of code
    val c = cardsPerStudent
    val k = cards.length
    // O(k log k)
    val sortedCards = cards.sorted
    val totalCards = sortedCards.sum

    // after review of code i added a memo array to speed it up
    // O(k)
    val memo = Array.fill(k+1)(0L)
    for i <- 1 until k + 1 do
      memo(i) = memo(i - 1) + sortedCards(i - 1)

    var left = 0L
    var right = totalCards / c // max num of sets

    // binary search over the possible number of full sets
    // while loop O(log K)
    // nested helper O( log (K * M) / c)
    while left < right do
      val mid = (left + right + 1) /2
      // Find a match for the target in the array
      val p = helper(sortedCards, mid)
      // boundary of target
      val idx = if p >= 0 then p else -(p + 1)
      val distributedCards = memo(idx) + (mid * (k - idx))
      // need at least mid * c "slots" to form mid full sets
      if distributedCards >= mid * c then
        left = mid
      else
        right = mid - 1
    left

  test("howManySets (small)", howManySets, "cardsPerStudent", "cards")
  test("howManySets (big)", howManySets, "cardsPerStudent", "cards")
