package com.ascii

import com.simplehttp._


/**
 * Created by basca on 17/07/14.
 */
class AsciiGraphContainer extends ApplicationContainer(None) {
  routes += "/asciiGraph" -> new AsciiGraph
}
