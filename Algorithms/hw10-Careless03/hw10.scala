object hw10 extends hwtest.hw("CS385"):
  def userName = "Aden Clymer"

  // O(n + battles)
  def kaijuTypes(n: Int, battles: Array[(Int, Int)]): Array[Int] =
    val ufArray: Array[UF] = Array.fill(3 * n)(new UF)
    for (winner, loser) <- battles do
      // winner(Type 1) ~ loser(Type 2)
      ufArray(winner).union(ufArray(loser + n))
      // winner(Type 2) ~ loser(Type 3)
      ufArray(winner + n).union(ufArray(loser + 2 * n))
      // winner(Type 3) ~ loser(Type 1)
      ufArray(winner + 2 * n).union(ufArray(loser))
    val type1 = ufArray(0).find()
    val type2 = ufArray(n).find()
    val type3 = ufArray(2 * n).find()
    // for each kaiju i, which one is Type X according to type 1
    val result = Array.fill(n)(-1)
    for i <- 0 until n do
      if ufArray(i).find() == type1 then result(i) = 1
      else if ufArray(i + n).find() == type1 then result(i) = 2
      else if ufArray(i + 2 * n).find() == type1 then result(i) = 3
    result

  test("kaijuTypes", kaijuTypes, "n", "battles")

  //////////////////////////////////////////////////////////////////////
  // Implementation of union-find.
  //   new UF           -- makes a new union-find node
  //   uf1.union(uf2)   -- unions two union-find nodes
  //   uf.find()        -- find the root of the tree
  // *** DO NOT CHANGE THE CODE BELOW! ***

  class UF:
    private var parent: UF = null
    private var rank = 0

    def union(other: UF): Unit =
      val root1 = this.find()
      val root2 = other.find()
      if root1 == root2 then return // if the roots are the same, do nothing
      if root1.rank == root2.rank then
        root1.rank += 1
        root2.parent = root1
      else if root1.rank > root2.rank then root2.parent = root1
      else root1.parent = root2

    def find(): UF =
      if parent == null then this
      else
        val root = parent.find()
        parent = root
        root
