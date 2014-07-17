import AssemblyKeys._

// ---------------------------------------------------------------------------------------------------------------------
//
// assembly setup
//
// ---------------------------------------------------------------------------------------------------------------------
name := "asciigraph"

version := "0.1.0"


scalaVersion := "2.10.4"

scalacOptions ++= Seq("-optimize", "-Yinline-warnings", "-feature", "-deprecation")


excludedJars in assembly <<= (fullClasspath in assembly) map { cp =>
  cp filter {
    _.data.getName == "minlog-1.2.jar"
  }
}

// ---------------------------------------------------------------------------------------------------------------------
//
// build info setup
//
// ---------------------------------------------------------------------------------------------------------------------
buildInfoSettings

sourceGenerators in Compile <+= buildInfo

buildInfoKeys := Seq[BuildInfoKey](name, version, scalaVersion, sbtVersion)

buildInfoPackage := "com.avalanche"

// ---------------------------------------------------------------------------------------------------------------------
//
// dependencies
//
// ---------------------------------------------------------------------------------------------------------------------

libraryDependencies ++= Seq()

libraryDependencies += ("org.scalatest" %% "scalatest" % "2.1.7" % "test")

libraryDependencies += ("com.github.mdr" %% "ascii-graphs" % "0.0.3")