// object hw1 extends hwtest.hw("CS385"):
//   def userName ="Aden Clymer"

//   // Fill in and sign the appropriate statement of assistance below
//   // as described in DAAW 2024 Appendix B.C.1 (pages 30-31)

//   // I CERTIFY THAT I HAVE COMPLETELY DOCUMENTED ALL
//   // SOURCES THAT I USED TO COMPLETE THIS ASSIGNMENT AND THAT
//   // I ACKNOWLEDGED ALL ASSISTANCE I RECEIVED IN THE
//   // COMPLETION OF THIS ASSIGNMENT.
//   // Aden Clymer

//   // O(log n) <-- fill in the Big-O running time here!
//   def firstIndex(target: Int, arr: Array[Int]): Int =
//     var left = 0
//     var right = arr.length - 1
//     while left <= right do
//       val mid = (right + left) / 2
//       if target <= arr(mid) then
//         right = mid - 1
//       else
//         left = mid + 1
//     left

//   test("firstIndex", firstIndex, "target", "arr")

//   // I utilized Russian Peasant Multiplication as explained through this
//   // https://www.wikihow.com/Multiply-Using-the-Russian-Peasant-Method
//   // I found this by googling: ways to repeat multiply two numbers quickly
//   // which populated various results, russian peasant multiplication being one
//   // of them.

//   // O(log n) <-- fill in the Big-O running time here!
//   def weirdMultiply(m: Int, n: Int): Int =
//     var x = m
//     var y = n
//     var result = 0
//     while y > 0 do
//       if y % 2 != 0 then
//         result += x
//       x *= 2
//       y /= 2
//     result

//   test("weirdMultiply", weirdMultiply, "m", "n")

import scala.collection.mutable

// ── Tree definition ────────────────────────────────────────────────
enum BinaryTree[+A]:
  case Empty // Represents an empty tree
  case Node(item: A, left: BinaryTree[A], right: BinaryTree[A])

object practice:
  import BinaryTree._
  final class UnionFind(n: Int):
    private val parent = (0 until n).toArray
    private val rank = Array.fill(n)(0)
    def find(x: Int): Int =
      if parent(x) != x then parent(x) = find(parent(x))
      parent(x)
    def union(x: Int, y: Int): Boolean =
      val (rx, ry) = (find(x), find(y))
      if rx == ry then false
      else
        if rank(rx) < rank(ry) then parent(rx) = ry
        else if rank(rx) > rank(ry) then parent(ry) = rx
        else { parent(ry) = rx; rank(rx) += 1 }
        true

  // ── Breadth-First Search (level-order traversal)
  def bfs[A](root: BinaryTree[A]): List[A] =
    val queue = mutable.Queue(root)
    val visited = mutable.ListBuffer[A]()
    while queue.nonEmpty do
      queue.dequeue match
        case BinaryTree.Empty => ()
        case BinaryTree.Node(item, left, right) =>
          visited += item
          queue.enqueue(left)
          queue.enqueue(right)
    visited.toList

  def dfs[A](root: BinaryTree[A]): List[A] =
    root match
      case BinaryTree.Empty => Nil
      case BinaryTree.Node(item, left, right) =>
        item :: dfs(left) ::: dfs(right)

  // ────────────────────────────────────────────────────────────
  //  Small UF helper for Kruskal
  // ────────────────────────────────────────────────────────────

  // Edge tuple: (u, v, w)
  type Edge = (Int, Int, Double)
  // ────────────────────────────────────────────────────────────
  //  Build edge list from matrix  (upper triangle only)
  // ────────────────────────────────────────────────────────────
  def edgesFromMatrix(matrix: Array[Array[Double]]): List[Edge] =
    val n = matrix.length
    for
      i <- (0 until n).toList
      j <- i + 1 until n
      w = matrix(i)(j) if w.isFinite
    yield (i, j, w)

  // ────────────────────────────────────────────────────────────
  //  Kruskal – variant returning MST edge set
  // ────────────────────────────────────────────────────────────
  def kruskalMST(mat: Array[Array[Double]]): List[Edge] =
    val n = mat.length
    val uf = UnionFind(n)
    val mst = mutable.ListBuffer[Edge]()
    for (u, v, w) <- edgesFromMatrix(mat).sortBy(_._3) do
      if uf.union(u, v) then mst += ((u, v, w))
    mst.toList

  // ────────────────────────────────────────────────────────────
  //  Kruskal – variant returning total weight only
  // ────────────────────────────────────────────────────────────
  def kruskalWeight(mat: Array[Array[Double]]): Double =
    kruskalMST(mat).map(_._3).sum

  // ────────────────────────────────────────────────────────────
  //  Prim’s algorithm – returns MST edge set
  // ────────────────────────────────────────────────────────────
  def primMST(mat: Array[Array[Double]], start: Int = 0): List[Edge] =
    val n = mat.length
    val inMST = Array.fill(n)(false)
    val key = Array.fill(n)(
      Double.PositiveInfinity
    ) // there are infinite edge weights to each node
    val parent = Array.fill(n)(-1) // -1 if parent isn't chosen

    key(start) = 0.0
    for _ <- 0 until n do
      var u = -1
      var min = Double.PositiveInfinity
      // search through the list for the smallest node to connect to
      for v <- 0 until n do
        if !inMST(v) && key(v) < min then
          min = key(v)
          u = v
      inMST(u) = true
      for v <- 0 until n do
        val w = mat(u)(v)
        if !inMST(v) && w.isFinite && w < key(v) then
          key(v) = w
          parent(v) = u

    (1 until n).collect {
      case v if parent(v) != -1 => (parent(v), v, key(v))
    }.toList

  // ────────────────────────────────────────────────────────────
  //  Dijkstra – single-source shortest paths (list of distances)
  // ────────────────────────────────────────────────────────────
  def dijkstra(mat: Array[Array[Double]], src: Int): Array[Double] =
    val n = mat.length
    val dist = Array.fill(n)(Double.PositiveInfinity)
    val visited = Array.fill(n)(false)
    dist(src) = 0.0

    for _ <- 0 until n do
      var u = -1
      var min = Double.PositiveInfinity
      for v <- 0 until n do
        if !visited(v) && dist(v) < min then
          min = dist(v)
          u = v
      visited(u) = true
      for v <- 0 until n do
        val w = mat(u)(v)
        if !visited(v) && w.isFinite && dist(u) + w < dist(v) then
          dist(v) = dist(u) + w
    dist

  // ── Example ────────────────────────────────────────────────────────
  @main def run(): Unit =
    import BinaryTree.*
    val tree =
      Node(
        1,
        Node(2, Node(4, Empty, Empty), Node(5, Empty, Empty)),
        Node(3, Empty, Node(6, Empty, Empty))
      )

    println(bfs(tree)) // prints: List(1, 2, 3, 4, 5, 6, 7)
    println(dfs(tree))

    val inf = Double.PositiveInfinity
    val g = Array(
      Array(0.0, 2.0, 3.0, inf, inf),
      Array(2.0, 0.0, 4.0, 7.0, inf),
      Array(3.0, 4.0, 0.0, 1.0, 8.0),
      Array(inf, 7.0, 1.0, 0.0, 5.0),
      Array(inf, inf, 8.0, 5.0, 0.0)
    )

    println("Kruskal MST edges: " + kruskalMST(g))
    println("Kruskal total weight: " + kruskalWeight(g))
    println("Prim  MST edges: " + primMST(g))
    println("Dijkstra from 0: " + dijkstra(g, 0).mkString(", "))
