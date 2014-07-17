package com.ascii

import com.github.mdr.ascii.layout._

import scala.collection.mutable

/**
 * Created by basca on 17/07/14.
 */
object AsciiGraph extends App {
  override def main(args: Array[String]): Unit = {
    val vertices: mutable.ListBuffer[String] = new mutable.ListBuffer[String]()
    val edges: mutable.ListBuffer[(String, String)] = new mutable.ListBuffer[(String, String)]()

    Iterator.continually(Console.readLine()).takeWhile(_ != "END").foreach {
      case l if l.startsWith("vertex:") =>
        val vertex:String = l.replace("vertex:", "").trim
        vertices.append(vertex)
      case l if l.startsWith("edge:") =>
        val edge:Array[String] = l.replace("edge:", "").trim.split(",")
        edges.append((edge(0).trim, edge(1).trim))
    }

    val graph:Graph[String] = Graph[String](vertices = vertices.toList, edges = edges.toList)
    val ascii:String = Layouter.renderGraph[String](graph)
    println(ascii)
  }
}
