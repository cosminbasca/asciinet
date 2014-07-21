package com.ascii

import java.io.{InputStreamReader, BufferedReader}
import java.net.InetSocketAddress
import com.simplehttp.startServer

/**
 * Created by basca on 21/07/14.
 */
object Server extends App {
  def serveForever(port: Int, dieOnBrokenPipe: Boolean) {
    val appContainer: AsciiGraphContainer = new AsciiGraphContainer()
    val boundAddress: InetSocketAddress = startServer[Nothing](appContainer, port)

    println(s"${boundAddress.getPort}")

    if (dieOnBrokenPipe) {
      // Exit on EOF or broken pipe.  This ensures that the server dies
      // if its parent program dies.
      val stdin: BufferedReader = new BufferedReader(new InputStreamReader(System.in))
      try {
        stdin.readLine()
        System.exit(0)
      } catch {
        case e: java.io.IOException =>
          System.exit(1)
      }
    }
  }

  override def main(args: Array[String]): Unit = {
    val (port:Int, die:Boolean) = args.length match {
      case 0 =>
        (0, false)
      case 1 =>
        (args(0).toInt, false)
      case 2 =>
        (args(0).toInt, true)
    }

    serveForever(port, die)
  }
}