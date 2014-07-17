package com.ascii

import java.util

import com.github.mdr.ascii.layout._
import org.yaml.snakeyaml.Yaml
import org.yaml.snakeyaml.constructor.Constructor
import scala.beans.BeanProperty

/**
 * Created by basca on 17/07/14.
 */
class GraphDescriptor {
  @BeanProperty var vertices = new util.ArrayList[String]()
  @BeanProperty var edges = new util.ArrayList[Tuple2]()
}

object AsciiGraph extends App {
  override def main(args: Array[String]): Unit = {
    val yaml = new Yaml(new Constructor(classOf[GraphDescriptor]))
    val gDescriptor:GraphDescriptor = yaml.load("").asInstanceOf[GraphDescriptor]

    val graph = Graph( vertices = gDescriptor.getVertices(), edges = gDescriptor.getEdges())
    val ascii = Layouter.renderGraph(graph)
  }
}
