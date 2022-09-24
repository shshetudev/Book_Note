#### A short story
* Tom and Joe work as a software devloper for Acme enterprises, a startup compnay that offers a free online service for funding the best deals in your area.
* The company received investor funding and is now franatically working toward its first official launch.
* So far, development of the software has stayed withing the time and budget constraints.
* However the manual and error-prone build and delivery process slows them down significantly.

#### Life without project automation
* __My IDE does the job:__
  * At Acme, developers do all their coding within the IDE, from navigating through the source code, implementing new features, and compiling and refactoring code, to running unit and integration tests.
  * If the IDE tells them that there is no compilation error and the tests are passing, they check the code into version control so it can be shared with the rest of them.   
  * The IDE is a powerful tool, but every developer will need to install it first with a standerdized version to be able to perform all of these tasks.
* __It works on my box:__
  *  Starting down a ticking clock, Joe checks out the code from version control and realizes that it doesn't compile anymore.
  *  It seems like one of the classes is missing from the source code.
  *  After discussing the issue, Tom realizes that he probably forgot to check in one of his classes, which causes the compilation process to fail.
  *  The rest of the team is now blocked and can't continue their workjntill Tom checks in the missing `source` file.
* __The code integration is a complete disaster:__
  * Acme has two different development groups, one specializing in building the web-based user interface and the other working on the compilation for the whole application, build a deliverable, and deploy it to a web server in a test evnironment.
  * Both teams sit together at Tom's computer to run the compilation fo rthe whole application, build a deliverable, and deploy it to a web server in a test environment.
* __The testing process slows to a crawl:__
  * The quality assurance (QA) team is eager to get their hands on a first version of the application.
  * As we can imagine, they aren't too happy about testing low-quality software.
  * With every fix the development team puts into place, they have to run through the same manual process.
* __Deployment turns into a marathon:__
  * From experience, the team knows that the outcome of deploying an application is unpredicable due to unforeseen problems.
  * The infrastructure and runtime environment has to set up, the database hast to be prepared with seed data.
  * The actual deployment of the applications has to happen, and intial health monitoring needs to be performed.
  * Of course, the team has an action plan in place, but each of the steps has to be executed manually.
  
#### Benefits of project automation

* __Prevents manual intervention:__
  * Having to manually perform steps to produce and deliver software is time-consuming and error-prone.
  * Frankly, as a developer and system administrator, we have better things to do than to handhold a compilation prcess or to copy a file from directory A to directory B.
  * __Any step in our software development process that can be automated should be automated.__
  
* __Creates repeatable builds:__
  * The actual building of our software usually follows predefined and ordered steps.
  * __For example, we compile our source code first, then run our tests, and lastly assemble a deliverable.__
  * We'll need to run the same steps over and over again-every day.
  * This shoud be as easy as pressing a button.

* __Makes builds portable:__
  * We've seen that being able to run a build from and IDE is very limiting.
  * First of all, we'll need to have the particular prduct installed on our machine.
  * Second, the IDE may only be available for a specific operating system.
  * __An automated build shouldn't require a specific runtime environment to work, whether this is an operating system or IDE.__
  * __Optimally, the automated tasks should be executable from the command line, which allows us to run the build from any machine we want, whenever we want.__
  
#### Types of project automation

* __On-demand builds:__
  * The typical use case for on-demand automation is when a user triggers a build on his or her machine.
  * In most cases, the user executes a script on the command line that performs tasks in a predined order.
  ![On demand build](/images/1.1-on-demand-build.png)

  * __For example:__
    > `compiling source code -> copying a file from directory A to directory B -> assembling a deliverable.`
  * Usually, this type of automation is executed multiple times per day.

* __Triggered builds:__
  * If we are practicing agile software development, we're interested in receiving fast feedback about the health of our project.
  * __We will want to know if our source dode can be compiled without any errors or if there's a potential software defect indicated by a failed unit or integration test.__
  ![Triggered build](/images/1.2-triggerd-build.png)
  * This type of automation is usually triggerd if code was checked into version control.

* __Scheduled builds:__
  * __We can think of scheduled automation as a time-based job scheduler (in the context of a Unix-based operation system, also known as a cron job).__
  ![Scheduled build](/images/1.3-scheduled-build.png)
  * It runs in particular intervals or at concrete times - for example, every morning at 1.00 a.m. or every 15 minutes.
  * As with all cron jobs, scheduled automation generally runs on a dedicated server.
  * __The practice that implements scheduled and triggered builds is commonly referred to as continuous integration(CI).__

#### Build tools

* A programming utility that lets us express our automation neeeds as executable is ordered tasks.
![orderd tasks](/images/1.4-build-tools.png)
* Each of these tasks in the above figure represents a unit of work.
* The order is important. We can't create the ZIP archive if the required class file haven't been compiled. Therefore the compilation task needs to be executed first.
  
#### Directed Acyclic Graph (DAG)
  
* Internally, tasks and their dependencies are modeled as a directed acyclic graph (DAG).
* A DAG is a data structure containing following two elements:
  * __Node:__
    * __A unit of work.__ In this case of a build tool, this is a task (for example, compiling source code).
  * __Directed edge:__
    * __A directed edge, also called an arrow, representing the relationship between nodes.__
    * In our situation, the arrow means _depends on._
    * If a task defines dependent tasks, they'll need to execute before the task itself can be executed.
* Each node knows about it's own execution state.
* __A node, and therefore the task can only be executed once.__
  ![DAG representation](/images/1.5-dag-representation.png)

  #### Anatomy of a build tool

  * It's important to understand the interactions among the components of a build tool, the actual definition of the build login, and the data that goes in and out.
  * __Build File:__
    * __The bulid file contains the configuration needed for the build, defines external dependencies such as third-party libraries, and contains the instructions to achieve a specific goal in the form of tasks and their independencies.__
    ![Build file](/images/1.6-build-file.png)
    * Oftentimes, a scripting language is used to express the build logic.
    * __That's why a build file is also referred to as a *build script.*__
  * __Build inputs and outputs:__
    * __A task takes an input, works on it by executing a series of steps, and produces an output.__
    * Some tasks may not need any input to function correctly, nor is creating an output considerd __mandatory__.
    * __Complex task dependency graphs may use the output of a dependent task as input.__
    ![Task inputs and outputs](/images/1.7-task-input-output.png)
  * __Build Engine:__
    * The build file's step-by-step instructions or rule set must be translated into an internal model the build tool can understand.
    * __The build engine processes the build file at runtime, resolves dependencies between tasks, and setup the entire configuration needed to command the execution.__
    * __Once the internal model is built, the engine will execute the series of tasks in the correct order.__
    ![Build engine](/images/1.8-build-engine.png) 
    * Some build tools allow us to access this model via an API to query for this information at runtime.
  * __Dependency Manager:__
    * __The dependency manager is used to process declarative dependency definations for our build file, resolve them from an artifact repository (for example, the local file system, an FTP, or an HTTP server),__ and make them available to our project.
    ![Dependency manager](/images/1.9-dependency-manager.png) 
    * A __dependecny__ is generally an external, reusable library in the form of a JAR file(for example, Log4j for logging support).
    * The __repository__ acts as storage for dependencies, and organizes and describes them by identifiers, such as name and version.
    * A typical repository can be an __HTTP server or the local file system.__

#### Java build tools

* __Apache Ant:__
  * __Apache Ant (Another Neat Tool) is an open source build tool written in Java.__
  * Its main purpose is __to provide automation for typical tasks needed in Java projects, such as compiling source files to classes, running unit tests, packaging JAR files, and creating Javadoc documentation.__
  * __While Ant's core is written in Java__, our build file is expressed through XML, which makes it portable across different runtime environments.
  * __Cons of Apache Ant:__
    * __Ant does not provide a dependency manager, so we'll need to manage external dependencies ourselves.__
    * However, Ant integrates well with another Apache project called __Ivy, a full-fledged, standalone dependency manager.__
    * Integrating Ant with Ivy requires additional effort and has to be done manually for each individual project.
     
* __Build Script terminology:__
  * A build script consists of three basic elements: __the project, multiple target and the used tasks.__
  * __Task:__
    * In Ant, a __task is a piece of executable code__, for example, for creating a new directory or moving a file.
    ![Hierarchical build script](/images/1.10-ant-hierarchial-build-script.png)
    * The task's behavior can be configured by it's exposed attributes.
    * The following code snippet shows the usage of the `javac` Ant tak for compiling Java source code withing our build script:
    ![Target](/images/1.10.1-build-script.png)
    * While Ant ships with a wide range of predefined tasks, we can extend our build script's capabilites by writing our own task in Java.
  * __Target:__
    * __A `target` is a set of tasks we want to be executed.__
    * We can think of it as a logical grouping.
    * When running Ant on command line, we provide the name fo the target(s) we want to execute.
    * By declaring dependencies between targets, a whole chain of commands can be created. The following code snippet shows two dependent targets:
    ![Target](/images/1.10.2-target.png)
  * __Project:__
    * Mandatory to all Ant projects is the overarching container, the `project`.
    * __Project is the top-level elemnet in an Ant script and contains one or more targets.__
    * We can only define one project per build script.
    * The following code snippet shows the project in releation to the targets:
    ![Project](/images/1.10.3-project.png)

* __Sample Build Script:__
  *  Say we want to write a script that compiles our Java source code in the directory `src` using the Java compiler and put it into the output directory `build`.
  *  Our Java `source code` has a dependency on a class from the external library `Apache Commons Lang`.
  *  We will tell the compiler about it by referencing the library's JAR file in the classpath.
  *  After compiling the code, we want to assemble a JAR file.
  *  Each unit of work, source code compilation, and JAR assembly will be grouped in an individual target.
  *  We will also add two more targets for initializing and cleaning up the required output directories.
  *  The structure of the Ant build script we'll create is shown:
  ![Hierarchical project structure of Ant build script](/images/1.11-hierarchical-project-structure-of-sample-ant-build-script.png)
  * __Implementation:__
    * Let's implement this example as a Ant build script. The following figure shows the whole project and targets required to achieve our goal:
     ![Ant Script](/images/1.11.1-ant-script-with-targets-for-compiling-source-code-and-assembling-JAR-file.png)
     * Ant doesn't impose any restrictions on how to define our build's structure.
     * This makes it easy to adapt to existing project layouts.
     * For example, the source and output directories in the sample script have been chosen arbitrarily.
     * It would be very easy to change them by setting a different value to their corresponding properties.
     * The same is true for target definition.
     * We have full flexibility to choose with logic needs to be executed per target and the order of execution.
  
  * __Shortcomings:__
    * __Versbose bulid scripts:__ Using XML as the definition language for our build logic results in overly large and verbose build scripts compared to build tools with a more succinct definition language.
    * __Unmaintainable build scripts:__
      * Complex build logic leads to long and unmaintainable build scripts.
      * Trying to define conditional logic like if-then/if-then-else statements becomes a burden when using a markup language.
    * __No guidelines:__ 
      * Ant doesn't give us any guidelines on how to setup our project.
      * In enterprise setting, this often leads to a build file that looks different every time.
    * __Monitoring API not exposed:__
      * Ant dosen't expose an API that lets us query information about the in-memory model at runtime.
    * __Without Ivy makes it hard:__
      * Using Ant without Ivy makes it hard to manage dependencies.
      * Oftentimes, we will need to check our JAR files into version control an manage their organization manually.

#### Apache Maven
##### Why Maven?
* __Maintainability:__
  * Using Ant across many projects within an enterprise has a big impact on maintainability.
  * With flexibility comes a lot of duplicated code snippets that are copied from one project to another.
* __Idea of convention over configuration:__
  * The Maven team realized the need for a standerdaized project layout an unified build lifecycle.
  * Maven picks up on the __idea of convention over configuration,__ meaning that it provides sensible default values for our project configuration and its behavior.
* __Knows where to search:__ The project automatically knows what directories to search for source code and what tasks to perform when running the build.
* __Ability to generate HTML project documentation:__ Maven also has the ability to generate HTML project documentation that includes the Javadocs for our application.
* __Plugin support:__
  * Maven's core functionality can be extended by custom logic developed as __plugins.__
  * The community is very active, and we can find a plugin for almost every aspect of build support, from integration with other development tools to reporting.
  * If a __plugin does not exist for our specific needs, we can write our own extension.__

##### Standard directory layout
* __Specific file existence:__ By introducing a default project layout, Maven ensures that every developer with the knowledge of Maven project will immediately know where to expect specific file types.
* __Java application source code:__ Java application source code sites in the directory `src/main/java`.
* All default directories are configurable.
* 
##### Build Lifecycle
* Maven is based on the concept of a build lifecycle.
* Every project knows exactly which steps to perform to build, package, and distribute an application, including the following functionality:
  * Compiling source code.
  * Running unit and integration tests.
  * Assembling the artifact (for example, a JAR file).
  * Deploying the artifact to a local repository.
  * Releasing the artifact to a remote repository.
* __Phase__
  * Every step in this build lifecycle is called a `phase`.
  * Phases are executed sequentially.
  * The phase we want to execute is defined when running the bulid on the command line.
  ![Maven's default project layout](/images/1.12-maven-default-project-layout.png) 
  * __We call the phase for packaging the application, Maven will automatically determine that the dependent phases like source code compliation and running tests need to be executed beforehand.__
  * The below figure-1.13 shows the predefined phases of Maven build and their order of execution.
  ![Maven build lifecycle phases](/images/1.13-maven-build-lifecycle.png) 

##### Dependency Management
* __Dependencies to external libraries:__ In maven projects, dependencies to external libraries are declared within the build script.
* __For example, if our project requires the popular Java library Hibernate, we simply define its unique artifact coordinates, such as organization, name, version, in the dependencies configuration block.__
* __How Maven dependency manager works?__
  * __At runtime, the declared libraries and their transitive dependencies are downloaded by Maven's dependency manager, stored in the local cache for later reuse__, and made available to our build (for example, for compiling source code).
  ![Maven dependency manager](/images/1.13.1-dependency-management.png) 
  * __Maven precofigures the use of repository, Maven Central, to download dependencies.__
  * __Subsequent builds will reuse an existing artiface from the local cache and therefore won't contact Maven Central.__
  * __Maven Central is the most popular binary artifact repository in the Java community.__
  ![Maven interaction with maven central](/images/1.14-maven-interaction-with-maven-central.png)
* __Is depenedency management in Mave limited to external libraries?__
  * __No. Dependency management in Maven isn't limited to external libraries. We can also declare a dependency on other Maven projects.__
  * __This need arises if we decompose software into `modules`, which are smaller components based on associated functionality.__
  ![Modularized architechture](/images/1.15-modularized-architecture.png)

##### Simple Build Script
  * The following figure shows a sample Maven build script named `pom.xml` that will implement the same functionality as the Ant build.
  ![Maven POM for building standardized Java project](/images/1.15.1-maven-pom.png) 
  * We will stick to the the default conventions here, so maven will look for the source code in the directory `src/main/java` instead of `src`.

##### Shortcomings
* __Restrictive structure and lifecycle:__ Maven proposes a default structure and lifecycle for a project that often is too restrictive and may not fit our project's needs.
* __Custom extension overl cumbersome:__ 
  * Writing custom extensions for Maven is overly cumbersome.
  * We will need to learn about __Mojos (Maven's internal extenstion API)__, how to provide a plugin descriptor (again in XML), and about specific annotations to provide the data needed in our extension implementation.
* __Brittle and unstable builds:__ 
  * Earlier versions of __Maven (2.0.9) automatically try to update their own core plugins.__ 
  * This may cause brittle and unstable builds.


##### Requirement for a next generation build tool
* __Problems on both Ant and Maven:__
  * __By picking Ant__, we choose full flexibility and extensibility but get weak project standardization, tons of boilerplate code and no support for dependency management.
  * __By picking maven__, which offers a convention over configuration approach and a seamlessly integrated dependency manager, but an overly restrictive mindset and cumbersome plugin system.