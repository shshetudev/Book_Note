# Chapter 1

## What is Design and Architecture?
- **Architecture**: Used in the context of something at a high level that is divorced from the lower-level details.
- **Design**: Implies structures and decisions at a lower level.
- The low-level details and the high-level structure are all part of the same whole. They form a continuous fabric that defines the shape of the system.

## Goal of a software architecture
- The goal of software architecture is to minimize the human resources required to build and maintain the required system.
- If that effort is low, and stays low throughout the lifetime of the system. the design is good.
- If the effort grows with each new release, the design is bad.

## What Went Wrong?
- **Morals from Aesop**:
  - Slow and steady wins the race.
  - The race is not to the swift, nor the battle of the strong.
  - The more haste, the less speed.
- The developers buy into a familiar lie: **We can clean it up later. We just have to get to market first!**
- But the developers can not go back and clean things up because they've got to get the next feature done, an the next and the next and the next.
- The bigger lie that developers buy into is the notion that writing messy code makes them go fast in the short term, and just slows them down in the long term.
- **The only way to go fast, in to go well**.
- **Their overconfidence will drive the redesign into the same mess as the original project.**


# Chapter 2: A tale of two values
- Every software system provides two different values to the stakeholders: **behavior and structure**.
- Software developers are responsible for ensuring that both those values remain high.

## Behavior
- The first value.
- Programmers are hired to make machines behave in a way that makes or saves money for the stakeholders.
- Many programmers believe their job is to make the machine implement the requirements and to fix any bugs. They are sadly mistaken.

## Architecture
- The second value.
- Software was invented to be "soft". That is it must be easy to change.
- If we'd wanted the behavior of machines to be hard to change, we would have called it hardware.
- The difficulty in making such a change should be proportional only to the scope of the change, and not to the shape of the change.
- Architectures should be as shape agnostic are practical.

## The Greater Value
- Managers will often say it's more important for the software system to work.
- If you give me a program that works perfectly bu is impossible to change, then it won't work when the requirements change. Therefore the program will become useless.
- If you give me a program that does not work but is easy to change, then I can make it work, and keep it working as requirment changes. Therefore the program will remain continually useful.
- It is the responsibility of the software development team to assert the importance of architecture over the urgency of features.

## Eisenhower's Matrix:
- There are four kinds of problems: 
  - Important Urgent. (I1)
  - Important not Urgent. (I2)
  - Unimportant Urgent. (U1)
  - Unimportnat Not Urgent. (U2) 
  
## FIGHT FOR THE ARCHITECTURE  
- Fulfilling this responsibility means wading into a fight.
- If architecture comes last, than the system will become ever more costly to develop, and eventually change will become practically impossible for part or all of the system.

# Chapter 3: PARADIGM OVERVIEW
- There are 3 paradigms in programming:
  - Structured programming.
  - Object-oriented programming.
  - Functional programming.
- **Structured programming:**
  - The first paradigm8 to be adopted was structured programming, which was discovered by Edsger Wybe Dikstra in 1968.
  - Dikstra showed that the use of unrestrained jums(goto statements) is harmful to program structure.
  - He, replaced those jumps with the more familiar `if/then/else` and `do/while/until` constructs.
  - **Structured programming imposes discipline on direct transfer of control.**

- **Object Oriented programming:**
- This second paradigm was actually discovered by Ole Johan Dahl and Kristen Nygaard.
- **Object oriented programming imposes discipline on indirect transfer of control.**

- **Functional programming:**
- The third paradigm is known as Functional programming.
- This is the direct result of the work of ALonzo Church, who in 1936 invented 1-calculus while pursuing the same mathematical problem that was motivating Alan Turing at the same time.
- **Functional programming imposes discipline upon assignment.**

# Chapter 4: STRUCTURED PROGRAMMING

## Some interesting facts about Dijkstra
- Dijkstra concluded that the intellectual challenge of programming was greater than the intellectual challenge of theoretical physics. As a result, he chose programming as his long-term career.
- The Dutch authorities were unwilling to accept "programmer" as Dijkstra's profession. They had never heard of such a profession. To satisfy them, Dijkstra settled for "theoretical physicist" as his job title.
- **Dijkstra’s solution was to apply the mathematical discipline of proof. His vision was
the construction of a Euclidian hierarchy of postulates, theorems, corollaries, and
lemmas**. 
- **Dijkstra thought that programmers could use that hierarchy the way
mathematicians do**. 
- In other words, programmers would use proven structures, and
tie them together with code that they would then prove correct themselves.
- Dijkstra discovered that certain uses of goto statements
prevent modules from being decomposed recursively into smaller and smaller units,
thereby preventing use of the divide-and-conquer approach necessary for reasonable
proofs.
- **Bohm and Jacopini, proved that all programs can be constructed from just three structures: sequence, selection and iteration.**
- **Dijkstra showed that sequential statements could be proved correct through simple
enumeration.**
3- **Dijkstra tackled selection through reapplication of enumeration**.
- **To prove an iteration correct, Dijkstra had to use
induction. He proved the case for 1 by enumeration. Then he proved the case that if
N was assumed correct, N + 1 was correct, again by enumeration. He also proved the
starting and ending criteria of the iteration by enumeration.**

## SCIENCE TO THE RESCUE
- The statement `This is a lie` in neither true nor false.
- **Ultimately we can say that, mathematics is the discipline of proving provable stements true. Science in contrast, is the discipline of proving provable statement false.**

## TESTS
- Dijkstra once said, **Testing shows the presence, not the absence of bugs.** 
- In other words, **a program can be proven incorrect by a test, but it can not be proven correct.**