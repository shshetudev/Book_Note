## Small: 
- The first rule of the function is that they should be small. The second rule of functions is that they should be small than that.
- **Code block**
  - **Dirty block (Listing: 3-2)**:
      ```java
      public static String renderPageWithSetupsAndTearDowns(PageData pageData, boolean isSuite) throw Exception {
          boolean isTestPage = pageDat.hasAttribute("Test");
          if(isTestpage) {
              Wikipage testPage = pageData.getWikiPage();
              StringBuffer newPageContent = new StringBuffer();

              includeSetupPages(testPage, newPageContent, isSuite);
              newPageContent.append(pageData.getContent());

              includeTeardownPages(testPage, newPageContent, isSuite);
          }
          return pageData.getHtml();
      }
      ```
  - **Clean block (Listing: 3-3)**
    ```java
    public static String renderPageWithSetupsAndTearDowns(PageData pageData, boolean isSuite) throws Exception {
      if (isTestPage(pageData))
          includeSetupAndTeardownPages(pageData, isSuite);
      return pageData.getHtml();
    }
    ```
  - **Blocks and Indenting:**
    - This implies that the blocks within `if`, `else`, `while` and so on should be one line long.
    - The indent level of a function should not be greater than one or two.

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
      - **Function is an event.** In this form there is an input arguemt but no output argument, and the function use the argument to alter the state of the system. **Ex: void passwordAttemptFailedNtimes(int attempts)**
    - We should try to avoid any monadic functions that don't follow these forms. 
      - **For example: void includeSetupPageInto(StringBuffer pageText)**. If a function is going to transform its input arguemnt, the transformation should appear as the return value.
  - **Flag Arguments(Boolean arguments)**
    - Flag arguments are ugly. It complicates the signature of the function. 
    - It makes the function does more that one thing, one thing if the flag is **true** and another if the flag is **false**.
    - They are confusing and should be eliminated if possible.
    - **Example:** Let's imagine we want to make a booking for a Hotel. There are two ways to do this, **regular** and **premium**. To use a flag argument here we would make a function declaration like this