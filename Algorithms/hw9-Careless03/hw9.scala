object hw9 extends hwtest.hw("CS385"):
  def userName = "Aden Clymer"

  enum Tree23:
    case Empty
    case Node2(left: Tree23, elem: Int, right: Tree23)
    case Node3(left: Tree23, elem1: Int, mid: Tree23, elem2: Int, right: Tree23)

  import Tree23.*

  def leafNode2(k1: Int): Tree23.Node2 =
    Node2(Empty, k1, Empty)

  def leafNode3(k1: Int, k2: Int): Tree23.Node3 =
    Node3(Empty, k1, Empty, k2, Empty)

  def isEmpty(tree: Tree23): Boolean =
    tree match
      case Empty => true
      case _     => false

  def treeHeight(tree: Tree23): Int =
    tree match
      case Empty                   => 0
      case Node2(left, _, _)       => treeHeight(left) + 1
      case Node3(left, _, _, _, _) => treeHeight(left) + 1

  def is_leaf(tree: Tree23): Boolean =
    tree match
      case Node2(Empty, _, Empty)           => true
      case Node3(Empty, _, Empty, _, Empty) => true
      case _                                => false

  def treePrint(tree: Tree23): Unit =
    import scala.collection.immutable.Queue

    val height = treeHeight(tree)
    var level = height
    var nodeQ = Queue[Tree23]()
    var nextLevel = Queue[Tree23](tree)

    val leafNodes = math.pow(3, height - 1).toInt

    while nextLevel.nonEmpty do
      nodeQ = nextLevel
      nextLevel = Queue[Tree23]()
      val levelNodes = math.pow(3, height - level).toInt
      val empties = (leafNodes - levelNodes)
      val spacers = empties / (levelNodes * 2)

      while nodeQ.nonEmpty do
        print("      " * spacers)
        var (node, rest) = nodeQ.dequeue
        nodeQ = rest
        node match
          case Empty =>
            print("  __  ")
            nextLevel = nextLevel.enqueue(Empty)
            nextLevel = nextLevel.enqueue(Empty)
            nextLevel = nextLevel.enqueue(Empty)
          case Node2(left, k1, right) =>
            print(f" $k1%3d  ")
            if !isEmpty(left) then
              nextLevel = nextLevel.enqueue(left)
              nextLevel = nextLevel.enqueue(Empty)
              nextLevel = nextLevel.enqueue(right)
          case Node3(left, k1, mid, k2, right) =>
            print(f"$k1%2d,$k2%2d ")
            if !isEmpty(left) then
              nextLevel = nextLevel.enqueue(left)
              nextLevel = nextLevel.enqueue(mid)
              nextLevel = nextLevel.enqueue(right)
        print("      " * spacers)

      level = level - 1
      println()

      if nextLevel.forall(t =>
          t match
            case Empty => true
            case _     => false
        )
      then nextLevel = Queue[Tree23]()

  // DO NOT MODIFY ABOVE THIS LINE

  def lookup(elem: Int, tree: Tree23): Boolean =
    tree match
      case Empty => false
      case Node2(left, node, right) =>
        if elem == node then true
        else if elem < node then lookup(elem, left)
        else lookup(elem, right)
      case Node3(left, node1, mid, node2, right) =>
        if elem == node1 || elem == node2 then true
        else if elem < node1 then lookup(elem, left)
        else if elem < node2 then lookup(elem, mid)
        else lookup(elem, right)

  test("lookup", lookup, "elem", "tree")

  //
  // HELPER FUNCTIONS FOR INSERT BC I COULND'T IMPLEMENT WITHOUT THEM
  //
  // retrieves the data for a node and returns it in a triple tuple
  def downLevel(tree: Tree23): (Tree23, Int, Tree23) =
    tree match
      case Node2(left, node, right) => (left, node, right)
      case _                        => (Empty, 0, Empty)

  // go into a tree and return the node
  def getNodeFromSubtree(tree: Tree23): Int =
    tree match
      case Node2(left, node, right) => node
      case _                        => 0

  // Take a 3 node that needs to be seperated and gather the appropriate tree
  // based on instructions in the homework
  def splitNode3(
      tree1: Tree23,
      node1: Int,
      tree2: Tree23,
      node2: Int,
      tree3: Tree23,
      node3: Int,
      tree4: Tree23
  ): (Tree23, Boolean) =
    val keys = List(node1, node2, node3).sorted
    val lowest_node = keys(0)
    val mid_node = keys(1)
    val highest_node = keys(2)

    val left_node = Node2(tree1, lowest_node, tree2)
    val right_node = Node2(tree3, highest_node, tree4)
    (Node2(left_node, mid_node, right_node), true)
  //
  def merge(base: Tree23, subtree: Tree23): (Tree23, Boolean) =
    // Returns the result of combining the base tree and a Node2 subtree as a tuple
    // with the result tree and a boolean indicating whether or not the
    // merge caused a 3-node to split (and therefore the root of the resulting
    // tree belongs at the next higher level).

    // NOTE: THIS IS OPTIONAL. Implement it if you find it helpful.
    base match
      // if nothing is there then return the subtree
      case Empty => (subtree, false)

      // handle a 2 node
      case Node2(left, node, right) =>
        val sub_node = getNodeFromSubtree(subtree)
        val is_leaf = left == Empty && right == Empty

        if is_leaf then
          // handle if subtree is smaller
          if sub_node < node then
            (Node3(Empty, sub_node, Empty, node, Empty), false)
          // handle if subtree is larger
          else if sub_node > node then
            (Node3(Empty, node, Empty, sub_node, Empty), false)
          // all other
          else (base, false)
        // if it is not a leaf, handle cases
        else
        // if subtree is less than node then handle all cases
        if sub_node < node then
          val (new_left, left_split) = merge(left, subtree)
          if !left_split then (Node2(new_left, node, right), false)
          else
            val (left_sub, key, right_sub) = downLevel(new_left)
            (Node3(left_sub, key, right_sub, node, right), false)
        // handle if bigger
        else if sub_node > node then
          val (new_right, right_split) = merge(right, subtree)
          if !right_split then (Node2(left, node, new_right), false)
          else
            val (left_sub, key, right_sub) = downLevel(new_right)
            (Node3(left, node, left_sub, key, right_sub), false)
        // all other cases
        else (base, false)

      // Handle if node is a three Node
      // Good god what have I got in to
      case Node3(left, node1, mid, node2, right) =>
        val sub_node = getNodeFromSubtree(subtree)
        val is_leaf = left == Empty && right == Empty && mid == Empty

        if is_leaf then
          // if it is a three node you need to make the lowest node another tree
          // to the left and the right most node tto the right while the middle
          // should be your own node.
          val sorted_keys = List(node1, node2, sub_node).sorted
          val lowest_node = sorted_keys(0)
          val mid_node = sorted_keys(1)
          val highest_node = sorted_keys(2)

          val left_node = Node2(Empty, lowest_node, Empty)
          val right_node = Node2(Empty, highest_node, Empty)

          val promoted = Node2(left_node, mid_node, right_node)
          (promoted, true)
        else
        // handle if less the first node
        if sub_node < node1 then
          val (new_left, did_split) = merge(left, subtree)
          if !did_split then (Node3(new_left, node1, mid, node2, right), false)
          else
            val (left_sub, key, right_sub) = downLevel(new_left)
            splitNode3(left_sub, key, right_sub, node1, mid, node2, right)
        // cover if between 1st and 2nd node values
        else if sub_node < node2 then
          val (newMid, did_split) = merge(mid, subtree)
          if !did_split then (Node3(left, node1, newMid, node2, right), false)
          else
            val (left_sub, key, right_sub) = downLevel(newMid)
            splitNode3(left, node1, left_sub, key, right_sub, node2, right)
        // this will run if it higher than the first two
        else
          val (new_right, did_split) = merge(right, subtree)
          if !did_split then (Node3(left, node1, mid, node2, new_right), false)
          else
            val (left_sub, key, right_sub) = downLevel(new_right)
            splitNode3(left, node1, mid, node2, left_sub, key, right_sub)

  def insert(elem: Int, tree: Tree23): Tree23 =
    val singleton = Node2(Empty, elem, Empty)
    val (merged, did_split) = merge(tree, singleton)
    merged

  test("insert", insert, "elem", "tree")

  // IGNORE EVERYTHING BELOW THIS LINE

  import hwtest.parsers.*
  given TestableTree23: hwtest.Testable[Tree23] with
    val name = "Tree23"
    def parse: Parser[Tree23] =
      choose(
        'E' -> const(Tree23.Empty),
        'N' -> chain(parse, pInt, parse, Tree23.Node2(_, _, _)),
        'M' -> chain(
          parse,
          pInt,
          parse,
          pInt,
          parse,
          Tree23.Node3(_, _, _, _, _)
        )
      )
