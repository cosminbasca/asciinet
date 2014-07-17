logLevel := Level.Warn

resolvers += Resolver.url("artifactory", url("http://scalasbt.artifactoryonline.com/scalasbt/sbt-plugin-releases"))(Resolver.ivyStylePatterns)

resolvers ++= Seq(
  "Sonatype Snapshots" at "http://oss.sonatype.org/content/repositories/snapshots",
  "Sonatype Releases" at "http://oss.sonatype.org/content/repositories/releases"
)

addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "0.11.2")

addSbtPlugin("com.eed3si9n" % "sbt-buildinfo" % "0.3.2")

// The above automatically adds 4 global tasks to sbt prompt: cleanCacheFiles, cleanCache, cleanLocalFiles, and cleanLocal.
addSbtPlugin("com.eed3si9n" % "sbt-dirty-money" % "0.1.0")
