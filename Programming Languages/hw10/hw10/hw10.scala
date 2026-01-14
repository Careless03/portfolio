import scala.collection.mutable._ // https://www.geeksforgeeks.org/queue-in-scala/
import scala.compiletime.ops.boolean
import java.{util => ju}

object hw10 extends hwtest.hw("CS478"):
  def userName = "Aden Clymer"

  // I CERTIFY THAT I HAVE COMPLETELY DOCUMENTED ALL
  // SOURCES THAT I USED TO COMPLETE THIS ASSIGNMENT AND THAT
  // I ACKNOWLEDGED ALL ASSISTANCE I RECEIVED IN THE
  // COMPLETION OF THIS ASSIGNMENT.
  // Aden Clymer

  // Got help from the website: https://www.geeksforgeeks.org/queue-in-scala/
  // It helped me understand how queue works as a refresher.

  // I referenced old ICE's from CS384 to attempt to figure out how everything works

  // To whom is grading. I apologize for the ugly code. I am quite confused and
  // attempting to write this over the span of two day of sleep-deprived, spite-induced
  // coding rampage of sad proportions. I hope the following makes somewhat sense

  { // don't delete these curly braces, they're preventing name conflicts
    import hwtest.searchtrees.*

    // I realize we were supposed to use has Next and next a lot more. But to be
    // completely transparent. I have no idea what the actual heck is going on.
    // The following code is OOP as best possible, but not best practice. please
    // excuse my stupidity.
    def searchTreeIterator(tree: SearchTree[Int]): Iterator[Int] =
      new Iterator[Int]:
        var listOfTrees = helper(tree).reverse

        def helper(node: SearchTree[Int]): List[SearchTree[Int]] =
          node match
            case Empty                   => List.empty[SearchTree[Int]]
            case Node(left, item, right) => node :: helper(left)

        def hasNext(): Boolean = listOfTrees.nonEmpty
        def next =
          if !hasNext then
            throw new NoSuchElementException("next of emtpy Iterator")
          listOfTrees match
            case Node(left, item, right) :: rest =>
              listOfTrees = helper(right).reverse ::: rest
              item
            case _ => throw new NoSuchElementException("next of Empty Iterator")
      // new Iterator[Int]:
      //   var nodeList = List.empty[SearchTree[Int]]
      //   addLeftToNodeList(tree)

      //   // function that finds the smallest left hand path aka tree
      //   def addLeftToNodeList(node: SearchTree[Int]): Unit =
      //     node match
      //       case SearchTree.Empty =>
      //       case SearchTree.Node(left, item, _) =>
      //         nodeList = node :: nodeList
      //         addLeftToNodeList(left)

      //   def hasNext(): Boolean = nodeList.nonEmpty

      //   def next(): Int =
      //     nodeList match
      //       case Nil => // Empty makes the program upset.
      //         throw new NoSuchElementException("next on empty iterator")
      //       // check for node and if there is a next on the list
      //       case SearchTree.Node(_, item, right) :: tail =>
      //         nodeList = tail
      //         addLeftToNodeList(right)
      //         item

    test(
      "searchTreeIterator",
      searchTreeIterator(_: SearchTree[Int]).toList,
      "tree"
    )
  }

  { // don't delete these curly braces, they're preventing name conflicts
    import hwtest.binarytrees.*

    // I tried my best
    def levelByLevel(tree: BinaryTree[Int]): Iterator[List[Int]] =
      new Iterator[List[Int]]:
        var treesToProcess =
          tree match
            case Empty => scala.collection.mutable.Queue.empty[BinaryTree[Int]]
            case _     => scala.collection.mutable.Queue(tree)

        def hasNext = treesToProcess.nonEmpty

        def next =
          if !hasNext then
            throw new NoSuchElementException("next of empty Iterator")

          var newQueue = scala.collection.mutable.Queue.empty[BinaryTree[Int]]
          var valuesToReturn = scala.collection.mutable.Queue.empty[Int]
          for tree <- treesToProcess do
            tree match
              case Node(item, left, right) =>
                left match
                  case BinaryTree.Empty => {}
                  case _                => newQueue.enqueue(left)
                left match
                  case BinaryTree.Empty => {}
                  case _                => newQueue.enqueue(right)
                valuesToReturn.enqueue(item)
              case Empty =>
                throw new NoSuchElementException("next of empty Iterator")
          treesToProcess = newQueue
          valuesToReturn.toList
      new Iterator[List[Int]]:
        // establish base variables
        var curLvl = 0 // keep track of overall level
        var curLvlList = List.empty[Int] // keep track of list per level
        var queue = Queue[(BinaryTree[Int], Int)]()

        // establish head
        tree match
          case BinaryTree.Empty => // auto populated BinaryTree.Empty, apply logic to rest of code
          case BinaryTree.Node(item, left, right) =>
            queue.enqueue((BinaryTree.Node(item, left, right), 0))

        def hasNext(): Boolean = queue.nonEmpty

        // A lot of this code came from ICE's from Data Structures and just
        // combining the logic from them to try and create something that works.
        def next(): List[Int] =
          if (curLvlList.nonEmpty) then
            val result = curLvlList
            curLvlList = List.empty[Int]
            result
          else
            while queue.nonEmpty do
              val (node, lvl) = queue.dequeue()
              node match
                case BinaryTree.Empty =>
                case BinaryTree.Node(item, left, right) =>
                  item :: curLvlList
                  if left != BinaryTree.Empty then
                    queue.enqueue((left, lvl + 1))
                  if right != BinaryTree.Empty then
                    queue.enqueue((right, lvl + 1))
            curLvl += 1
            curLvlList

    test("levelByLevel", levelByLevel(_: BinaryTree[Int]).toList, "tree")
  }
