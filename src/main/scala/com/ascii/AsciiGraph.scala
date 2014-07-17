package com.ascii

import java.util

import com.github.mdr.ascii.layout._
import scala.collection.JavaConversions._
import org.yaml.snakeyaml.Yaml
import org.yaml.snakeyaml.constructor.Constructor
import scala.beans.BeanProperty
import scala.collection.mutable

/**
 * Created by basca on 17/07/14.
 */
class GraphDescriptor {
  @BeanProperty var vertices:mutable.Buffer[String] = new util.ArrayList[String]()
  @BeanProperty var edges = new util.ArrayList[util.ArrayList[String]]()
}

object AsciiGraph extends App {
  override def main(args: Array[String]): Unit = {
    val yaml = new Yaml(new Constructor(classOf[GraphDescriptor]))
    val gDescriptor:GraphDescriptor = yaml.load("").asInstanceOf[GraphDescriptor]

    val graph = Graph(
      vertices = gDescriptor.getVertices.toList,
      edges = gDescriptor.getEdges.map{
        case edge: util.ArrayList[String] => (edge.get(0), edge.get(1))
      }.toList
    )
    val ascii = Layouter.renderGraph(graph)
  }
}
