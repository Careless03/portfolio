object hw6 extends hwtest.hw("CS385"):
  def userName = "Aden Clymer"

  // I CERTIFY THAT I DID NOT USE ANY SOURCES OR RECEIVE ANY
  // ASSISTANCE REQUIRING DOCUMENTATION WHILE COMPLETING
  // THIS ASSIGNMENT.
  // Aden Clymer
  ////////////////////////////////////////////////////////////
  // Problem 1

  // O(rows * cols * breaches)
  def viableRoutes(str: String, breaches: Int): Int =
    // ignore str, it is there to make the input easier to
    // understand when you've failed a test
    // instead, the real inputs are map (below) and breaches
    val map = str.trim.split("\\n").map(_.trim) // an array of strings
    // map is two-dimensional, access it as map(row)(col)
    val rows = map.length
    val cols = map(0).length
    if rows == 0 || cols == 0 then return 0
    val paths = Array.fill[Int](rows, cols, breaches + 1)(0)

    def obstExists(r: Int, c: Int): Int =
      if map(r)(c) == 'X' then 1 else 0
    // initialize
    val initial_cost = obstExists(0, 0)
    if initial_cost <= breaches then paths(0)(0)(initial_cost) = 1

    // Fill table
    for row <- 0 until rows do
      for col <- 0 until cols do
        for used <- 0 until breaches + 1 do
          if obstExists(0, 0) <= breaches then paths(0)(0)(obstExists(0, 0)) = 1
          val cost_at_given_point = paths(row)(col)(used)
          // if an obstacle exists then check for paths
          if cost_at_given_point > 0 then
            // Check right
            if row + 1 < rows then
              val cost = obstExists(row + 1, col)
              val new_used = used + cost
              if new_used <= breaches then
                paths(row + 1)(col)(new_used) += cost_at_given_point
            // Check down
            if col + 1 < cols then
              val cost = obstExists(row, col + 1)
              val new_used = used + cost
              if new_used <= breaches then
                paths(row)(col + 1)(new_used) += cost_at_given_point
    var total_ways_through_map = 0
    for k <- 0 until breaches + 1 do
      total_ways_through_map += paths(rows - 1)(cols - 1)(k)
    total_ways_through_map

  test("viableRoutes", viableRoutes, "map", "breaches")

  ////////////////////////////////////////////////////////////
  // Problem 1

  // O(row x col)
  def largestTerrainModel(grid: Array[Array[Int]]): Int =
    val rows = grid.length
    val cols = grid(0).length
    if rows == 0 || cols == 0 then return 0
    val dp = Array.fill(rows, cols)(-99)
    var max_side = 0
    // go through the grid
    for row <- 0 until rows do
      for col <- 0 until cols do
        // handle first row or col
        if row == 0 || col == 0 then dp(row)(col) = grid(row)(col)
        // iterate through the grid and find side
        else if grid(row)(col) == 1 then
          dp(row)(col) = (dp(row - 1)(col) min (dp(row)(col - 1) min dp(
            row - 1
          )(col - 1))) + 1
        else dp(row)(col) = 0
        max_side = max_side max dp(row)(col)
    max_side * max_side

  test("largestTerrainModel", largestTerrainModel, "grid")

  // DO NOT CHANGE OR DELETE THE LINE BELOW!
  given hwtest.Testable[Array[Array[Int]]] = hwtest.Testable.TestableGrid[Int]
