//
// author: Cosmin Basca
//
// Copyright 2010 University of Zurich
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//        http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
package com.ascii

import com.github.mdr.ascii.graph.Graph
import com.github.mdr.ascii.layout.GraphLayout
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
      val graph: Graph[String] = Graph[String](vertices = verticesArray.toSet, edges = edgesArray.toList)
      GraphLayout.renderGraph[String](graph)
    } else {
      ""
    }
  }
}
