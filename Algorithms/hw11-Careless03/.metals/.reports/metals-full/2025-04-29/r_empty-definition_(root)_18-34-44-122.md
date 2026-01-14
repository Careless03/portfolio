error id: `<none>`.
file:///C:/Users/aden.clymer/OneDrive%20-%20West%20Point/Classes/2025-2%20Classes/Day%201/CS385/hw11-Careless03/hw11.scala
empty definition using pc, found symbol in pc: `<none>`.
empty definition using semanticdb
empty definition using fallback
non-local guesses:

offset: 78
uri: file:///C:/Users/aden.clymer/OneDrive%20-%20West%20Point/Classes/2025-2%20Classes/Day%201/CS385/hw11-Careless03/hw11.scala
text:
```scala
import scala.io.StdIn.readInt
import scala.collection.mutable.ArrayBuffer

@@enum Cell:
  case Node(row: Int, col: Int)
  case Wall(row: Int, col: Int)
  case Edge(weight: Double)

object hw11:
  def userName = "Aden Clymer"
  import Cell.*
  // Tabulation explained: https://www.youtube.com/watch?v=FNUUImx9j3c

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

  def generate_random_maze(
      rows: Int,
      cols: Int
  ): Array[Array[Cell]] =
    val grid = Array.tabulate(rows, cols)((r, c) =>
      if r == 0 || c == 0 || r == rows - 1 || c == cols - 1 || (r % 2 == 0 && c % 2 == 0)
      then Wall(r, c)
      else if r % 2 != 0 && c % 2 != 0 then Node(r, c)
      else Edge(math.random())
    )
    grid

  def turn_into_graph(
      maze: Array[Array[Cell]]
  ): Array[Array[Cell]] =
    val rows = maze.length
    val cols = maze(0).length

    // Convert to Union
    val node_rows = rows / 2
    val node_cols = cols / 2
    val uf: Array[Array[UF]] =
      Array.tabulate(node_rows, node_cols)((_, _) => new UF)

    def ufAt(r: Int, c: Int): UF =
      val i = (r - 1) / 2
      val j = (c - 1) / 2
      uf(i)(j)

    // find all neighboring edges around a node
    var neighbors =
      ArrayBuffer.empty[(Int, Int, (Int, Int), (Int, Int), Double)]
    val directions = List((0, 2), (0, -2), (2, 0), (-2, 0))
    // only nodes are located in odd-odd cells
    for
      r <- 1 until rows by 2
      c <- 1 until cols by 2
    do
      // for each direction (N, E, S, W) compute if there is a viable Neighbor and save it
      // dr, dc = row/column in __ direction
      for (dr, dc) <- directions do
        val nr = r + dr
        val nc = c + dc
        // within bound of the walls
        if nr > 0 && nr < rows && nc > 0 && nc < cols then
          val wr = r + dr / 2 // wall row
          val wc = c + dc / 2 // wall column
          maze(wr)(wc) match
            case Edge(weight) =>
              // record walls on row and column, which nodes it connects to and weight
              neighbors.append((wr, wc, (r, c), (nr, nc), weight))
            case _ => ()

    val sorted_neighbors = neighbors.toList.sortBy(_._5)
    // Kruskal algo with UF
    for ((wr, wc, node1, node2, _) <- sorted_neighbors) do
      val u1 = ufAt(node1._1, node1._2)
      val u2 = ufAt(node2._1, node2._2)
      if u1.find() != u2.find() then
        maze(wr)(wc) = Node(wr, wc)
        u1.union(u2)
    maze(1)(0) = Node(1, 0)
    maze(rows - 2)(cols - 1) = Node(rows - 2, cols - 1)
    maze

  def convert_to_maze(graph: Array[Array[Cell]]): Array[Array[Char]] =
    val maze = Array.fill(graph.length, graph(0).length)('e')
    for
      i <- 0 until graph.length
      j <- 0 until graph(0).length
    do
      graph(i)(j) match
        case Node(row, col) => maze(i)(j) = '.'
        case Wall(row, col) => maze(i)(j) = '#'
        case Edge(weight)   => maze(i)(j) = '#'
    maze

  @main def run(rows_in: Int, cols_in: Int): Unit =
    var rows = rows_in + 2 // account for walls
    var cols = cols_in + 2 // account for walls
    if rows % 2 == 0 then rows += 1
    if cols % 2 == 0 then cols += 1
    else if rows < 3 || cols < 3 then
      throw new IllegalArgumentException("Rows and Columns are too small")
    val numbers = generate_random_maze(rows, cols)
    val graph = turn_into_graph(numbers)
    val maze = convert_to_maze(graph)
    maze.foreach(row => println(row.mkString(" ")))

```


#### Short summary: 

empty definition using pc, found symbol in pc: `<none>`.