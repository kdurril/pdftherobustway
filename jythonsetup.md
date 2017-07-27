## Set up Jython

**Jython**
1. [Download](http://search.maven.org/remotecontent?filepath=org/python/jython-installer/2.7.1/jython-installer-2.7.1.jar)
2. Install with [Install instructions](https://wiki.python.org/jython/InstallationInstructions)
3. See [fwierzbicki blog](http://fwierzbicki.blogspot.com/2017/07/jython-271-final-released.html) for more details

**PDFBox**
1. [Download](https://pdfbox.apache.org/index.html)
2. [Install](https://pdfbox.apache.org/building.html)
3. [Maven](https://pdfbox.apache.org/building.html), from root directory, mvn clean install 

**Run jython with PDFBox in classpath**

/Users/<user>/jython2.7.0/bin/jython -Dpython.path=/Users/<user>/Development/pdfbox-2.0.0-RC2/app/target/pdfbox-app-2.0.0-RC2.jar
