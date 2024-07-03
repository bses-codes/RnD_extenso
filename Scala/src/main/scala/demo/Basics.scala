package demo

object Basics extends App{
   val a: Int = 42
   val b = false
   val s = "I love Scala"
   val composed_s = "Hello" + " "+ "World"
   val interpolated_s = s"I want to say that $s"
   val expression = 2+3
   val ifexpression = if (a > 45) codeblock else 999
   val chained_if =
     if (a >43) 56
     else if (a<0) -2
     else if (a>999) 78
     else 0

   val codeblock = {
     val x = 67
     x + 3
   }
   def func(x:Int, y:String): String ={
     y + " " + x
   }

   def factorial(n:Int): Int =
     if (n <= 1) 1
     else n * factorial(n - 1)

   def myunit(): Unit = {
     println("Hello world")
   }
   val theUnit = ()

   println(factorial(5))
}
