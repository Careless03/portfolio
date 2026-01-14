object hw13 extends hwtest.hw("CS478"):
  def userName = "Aden Clymer"
    // I CERTIFY THAT I DID NOT USE ANY SOURCES OR RECEIVE ANY
    // ASSISTANCE REQUIRING DOCUMENTATION WHILE COMPLETING
    // THIS ASSIGNMENT.

    // Aden Clymer
  import scala.collection.mutable.Stack
  // use the push, pop, and isEmpty/nonEmpty methods
  // do ***NOT*** use += thinking it is the same as push, because it isn't

  enum Expr:
    case S
    case K
    case A(left: Expr, right: Expr)
  export Expr.{S,K,A}

  def evaluate(expr: Expr): Expr =
    val stack = Stack.empty[Expr]

    def restack(expr: Expr): Expr =
      def makeExprFromStack(expr: Expr, stack: Stack[Expr]): Expr =
        if stack.isEmpty then
          expr
        else
          val head = stack.pop()
          makeExprFromStack(A(expr,head), stack) // compile the stack into an expr
      makeExprFromStack(expr, stack)

    def eval(expr: Expr): Expr =
      expr match
        case A(left, right) =>
          stack.push(right)
          eval(left)

        case K =>
          // throw away 2nd argument, return 1st
          if stack.length >= 2 then
            val x = stack.pop()
            val y = stack.pop()
            eval(x)
          else
            restack(K)

        case S =>
          if stack.length >= 3 then
            val x = stack.pop()
            val y = stack.pop()
            val z = stack.pop()
            // S x y z === xz yz or A(x,z), A(yz)
            var newExpr = A(A(x,z),A(y,z))
            eval(newExpr)
          else
            restack(S)
    eval(expr)

  test("evaluate", evaluate, "expr")





  //////////////////////////////////////////////////////////////////////
  // YOU CAN IGNORE EVERYTHING AFTER THIS

  import hwtest.Testable

  given TestableExpr: Testable[Expr] =
    new Testable[Expr]:
      import hwtest.parsers.*
      val name = "Expr"
      def parse: Parser[Expr] =
        choose(
          'S' -> const(S),
          'K' -> const(K),
          'A' -> chain(parse, parse, A(_,_))
        )
      override def _show(x: Expr): String = x.toString
