package com.ascii

import java.io.{InputStreamReader, BufferedReader}
import java.net.InetSocketAddress
import com.simplehttp.{LocalNotifierServer, startServer}

/**
 * Created by basca on 21/07/14.
 */
object Server extends LocalNotifierServer[Nothing, AsciiGraphContainer] {
  override def container:AsciiGraphContainer = new AsciiGraphContainer()
}