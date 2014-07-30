package com.ascii

import com.github.mdr.ascii.layout.{Layouter, Graph}
import com.simplehttp.MsgpackMapHandler
import org.msgpack.`type`.Value
import org.msgpack.ScalaMessagePack._

/**
 * Created by basca on 21/07/14.
 */
class AsciiGraph extends MsgpackMapHandler[Nothing] {
  override def getResult(arguments: Map[String, Value], application: Option[Nothing]): Any = {
    val verticesArray: Array[String] = arguments.get("vertices") match {
      case Some(vertices) => vertices.asArray[String]
      case None => Array.empty[String]
    }

    val edgesArray: Array[(String, String)] = arguments.get("edges") match {
      case Some(edges) =>
        edges.asArrayValue().getElementArray.map {
          case value: Value =>
            val edge: Array[String] = value.asArray[String]
            (edge(0), edge(1))
        }
      case None => Array.empty[(String, String)]
    }

    if (verticesArray.nonEmpty && edgesArray.nonEmpty) {
      val graph: Graph[String] = Graph[String](vertices = verticesArray.toList, edges = edgesArray.toList)
      Layouter.renderGraph[String](graph)
    } else {
      ""
    }
  }
}
