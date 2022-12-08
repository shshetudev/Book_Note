- **Small**: 
  - Should be at maximum **20 lines** long.
  - The blocks within **if, else, while** and so on should be **one** line long. Probably that line should be a function call.
  - The nested structure(blocks) should be **one**v or **two** at maximum.
  - **Listing 3-1** is refactored to be **Listing 3-2** and then refactored to be shorten to **Listing 3-3**.
  - **Listing 3-1 | HtmlUtil.java**
    ```java
    public static String testableHtml(PageData pageData, boolean includeSuiteSetup) throws Exception {
      WikiPage wikiPage = pageData.getWikiPage();
      StringBuffer buffer = new StringBuffer();
      
      if(pageData.hasAttribute("Test")) {
        
        if(includeSuiteSetup) {
          WikiPage suiteSetup = PageCrawlerImpl.getInheritedPage(SuiteResponder.SUITE_SETUP_NAME, wikiPage);
          
          if(suiteSetup != null) {
            WikiPagePath setupPath = wikiPage.getPageCrawler().getFullPath(setup);
            String pagePathName = PathParser.render(pagePath);
            buffer.append("!include-setup .").append(pagePathName).append("\n");
          }
        }
      }
    }
    ``` 

- **Do One Thing:**
  - **Functions should do one thing, they should do it well. They should do it only.**
  - Functions that do one thing can not be reasonably divided into sections.

- **One level of Abstraction per Function**
  - Inorder to make sure our functions are doing one thing, we need to make sure that the statements withing our function are all at the same level of abstraction.
  - **Mixing the level of abstarction within a function is always confusing. Readers may not be able to tell whether a particular expression is an essential concept or a detail.**
  - **Reading code from Top to Bottom: The Stepdown Rule**
    - We want to write the method **renderPageWithSetupsAndTearDowns()** in one level of abstraction per function way like this:
      - To include setups and teardowns, we include setups then we include the test page content and then we include the teardowns.
      - To include setups, we include teh suite setup if this is a suite, then we include the regular setup.
      - To include the suite setup, we search the parent hierarchy for the **SuiteSetup** page and add an include statement with the path of that page.
    - **Code block**
      - **Cleaner block**
        ```java
        public class SetupTeardownIncluder {
            private PageData pageData;
            private boolean isSuite;
            private WikiPage testPage;
            private StringBuffer newPageContent;
            private PageCrawler pageCrawler;

            public static String render(PageData pageData) throws Exception {
                return new SetupTearDownIncluder(pageData).render(isSuite);
            }

            public static String render(PageData pageData, boolean isSuite) throws Exception {
                return new SetupTeardownIncluder(pageData).render(isSuite);
            }

            private SetupTeardownIncluder(PageData pageData) {
                this.pageData = pageData;
                testPage = pageData.getWikiPage();
                pageCre
            }
        }
        ``` 
- **Use Descriptive names:**
  - A long descriptive name is better than a short unclear name.
  - A long descriptive name is better than a long descriptive comment.
  - Not to be afraid to spend time choosing a name.
  - Choosing descriptive names will clarify the design of the module in our mind and help us to improve it.
  - To be consistent in our names. To use the same phrases, nouns and verbs in the function names that we choose for our modules.

- **Function Arguments:**
  - The ideal number of arguments for a function is zero.
  - Three arguments should be avoided as possible.
  - More than three requires a special justification.. and shouldn't be used anyway.
  - **Common Monadic forms (One argument function):**
    - There are three reasons to pass a single argument into a function:
      - **Function that asking a question** about that argument. **Ex: boolean fileExists("MyFile")**
      - **Function that trasforming the argument into something else and returning it**. **Ex: InputStream fileOpen("MyFile")** trasforms a file name **String** into an **InputStream** return value.
      - **Function is an event.** In this form there is an input arguemt but no output argument, and the function use the argument to alter the state of the system. **Ex: void passwordAttemptFailed.Ntimes(int attempts)**
    - We should try to avoid any monadic functions that don't follow these forms. 
      - **For example: void includeSetupPageInto(StringBuffer pageText)**. If a function is going to transform its input arguemnt, the transformation should appear as the return value.
  - **Flag Arguments(Boolean arguments)**
    - Flag arguments are ugly. It complicates the signature of the function. 
    - It makes the function does more that one thing, one thing if the flag is **true** and another if the flag is **false**.
    - They are confusing and should be eliminated if possible.
    - **Example:** Let's imagine we want to make a booking for a Hotel. There are two ways to do this, **regular** and **premium**. To use a flag argument here we would make a function declaration like this
    ```java
    //pseuduo-code
    class Hotel ...
    public Booking book(Customer customer, boolean isPremium) {
      if(isPremium)
        //logic for premium booking
      else
        //logic for regular booking
    }
    ```
    - Then when we see this function call `book(customer, true)`, we can't remember what is the function doing and what is the boolean argument means without going to read its implementation.
    - But it's better if we seperate it to two functions `regularBook(customer)` and `premiumBook(customer)`, so now it's easy to know what is the function doing exactly from his call without need to go to it's implementation.
    ```java
    //pseudo-code
    class Hotel ...
    public Booking regularBook(Customer customer) {...}
    public Booking premiumBook(Customer customer) {...}
    ``` 
  **Dyadic Functions (two arguemnts function)**
  - A function with two arguments is harder to understand than a **mondic** function. But of course, **there are times where two arguemnts are appropriate like are appropriate like `Point p = new Point(0, 0);`.** This is for sure because the points naturally take two arguments.
  - It will be better if we find a mechanism to convert the **dyadic** function to **monadic**. For example, `writeField(outputStream, name)` can be converted to **monadic** by any one of these methods:
    - **Making the `writeField` a member function of `OutputStream` class so that we can say `outputStream.writeField(name)`**
    - **Making the `outputStream` a member variable for the current class so that we don't have to pass it, like this writeField(name)**