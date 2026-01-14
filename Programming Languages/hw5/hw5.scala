object hw5 extends hwtest.hw("CS478"):
  def userName = "Aden Clymer"

  // DON'T FORGET TO INCLUDE ANY NEEDED DOCUMENTATION AS INLINE
  // COMMENTS, EITHER JUST ABOVE OR JUST BELOW THE POINT IN THE CODE
  // WHERE THE DOCUMENTATION IS RELEVANT!

  // I CERTIFY THAT I DID NOT USE ANY SOURCES OR RECEIVE ANY
    // ASSISTANCE REQUIRING DOCUMENTATION WHILE COMPLETING
    // THIS ASSIGNMENT.
    // Aden Clymer

  // Wanta, Matthew '25 gave verbal assitance on 9/25/2024 at 1530,
  // stating that I should utilize the stack.pop command in order to get items
  // from the stack. I also asked him if I could just do a for loop with
  // p <- program and he stated that it should work. I then applied that knowledge
  // to problem 1 with command <- commands

  ////////////////////////////////////////
  // PROBLEM 1: Robot Interpreter

  def robot(commands: String): Int =
    var x = 0
    var y = 0
    var direction = 0 // 0 - up, 1 - right, 2 - down, 3 - left
    var visited = Set((x,y))
    for (command <- commands) do
      command match
        case 'F' =>
          direction match
            case 0 => y += 1
            case 1 => x += 1
            case 2 => y -= 1
            case 3 => x -= 1
          visited += ((x,y))
        case 'R' =>
          direction = (direction + 3) % 4
        case 'L' =>
          direction = (direction + 1) % 4
    visited.size
  test("robot", robot, "commands")

  ////////////////////////////////////////
  // PROBLEM 2: BabyGrok

  // these are the things that can be in the program
  // it may seem strange that Num is here, but that's
  // because the Num command pushes its int onto the stack
  enum Command:
    case ADD
    case SUB
    case MUL
    case SWAP
    case DUP
    case POP
    case Num(n: Int)
  export Command.*

  def babyGrok(program: List[Command]): Array[Int] =
    val stack = scala.collection.mutable.Stack.empty[Int]
    for (p <- program) do
      p match
        case Num(n: Int) => stack.push(n) //Informed by Matthew Wanta
        case ADD =>
          val previous = stack.pop()//Informed by Matthew Wanta to utilize the pop command
          val beyond_previous = stack.pop()
          val added_num = previous+beyond_previous
          stack.push(added_num)
        case SUB =>
          val previous = stack.pop()
          val beyond_previous = stack.pop()
          val sub_num = beyond_previous-previous
          stack.push(sub_num)
        case MUL =>
          val previous = stack.pop()
          val beyond_previous = stack.pop()
          val mult_num = previous*beyond_previous
          stack.push(mult_num)
        case SWAP =>
          val previous = stack.pop()
          val beyond_previous = stack.pop()
          stack.push(previous)
          stack.push(beyond_previous)
        case DUP =>
          var previous = stack.pop()
          stack.push(previous)
          stack.push(previous)
        case POP => stack.pop()


    // this will return the final contents of the stack as an array
    // the .reverse is so that the array will display with the top
    // of the stack on the RIGHT (as in the diagrams) instead of
    // on the left
    stack.toArray.reverse

  test("babyGrok", babyGrok, "program")


  //////////////////////////////////////////////////////////////////////
  // YOU CAN IGNORE EVERYTHING BELOW!
  // I mean, you can look at it if you want to, but it's not going
  // to help you with the homework.

  import hwtest.parsers.{Parser, choose, const, chain, pInt, pList}
  import hwtest.Testable

  given TestableCommand: Testable[Command] =
    new Testable[Command]:
      val name = "Command"
      def parse: Parser[Command] =
        choose(
          'A' -> const(ADD),
          'S' -> const(SUB),
          'M' -> const(MUL),
          'W' -> const(SWAP),
          'D' -> const(DUP),
          'P' -> const(POP),
          'N' -> chain(pInt, Num(_))
        )
      override def _show(x: Command): String =
        x match
          case Num(n) => n.toString
          case _ => x.toString

  given TestableCommands: Testable[List[Command]] =
    new Testable[List[Command]]:
      val name = "Commands"
      def parse: Parser[List[Command]] = pList(TestableCommand.parse)
      override def _show(x: List[Command]): String =
        x.map(TestableCommand.show(_)).mkString(" ")
