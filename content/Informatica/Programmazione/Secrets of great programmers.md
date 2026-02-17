---
tags:
  - software-development
  - software-testing
  - unit-testing
---


What are the best-kept secrets of great programmers?

If I told you then I would have to kill you.

More seriously:

0. Everything can be done with hashmaps.

1. Managers always lie. That important system that needed to be ready yesterday, when delivered, will not be taken a look at in two months.

2. It is much better to write something "right" than make it fast and buggy. Whenever you have to hurry, simply don't, you always have all the time in the world. Always do the right thing. The system will take a lot less time to write and you will feel a lot better about the code.

3. If they say "we don't have more money, hurry up", then reduce the scope, remove features, do less, use agile methodologies. Never hurry up.

4. The GIGO effect: Garbage in, garbage out. Make sure the requirements are right.

5. There are no undocumented features. Either they are documented or nobody will know they exist.

6. RTFM is bad manners. Hallway usability is much better. If you think this contradicts number 5, maybe. Maybe not.

This is the main reason Windows beat Unix on the desktop: Unix and Linux were concerned about user manuals and educating its users. Windows was concerned about what the immediate reaction of users was, that is, getting rid of manuals and education and letting people perform their real jobs. I have never seen a manual for the iPhone or for Android devices, even 3 years old can use it. There is a lesson to be learned here. But I doubt that internally Microsoft, Apple and Google don't document the functionality and "how things are done over here", I worked at Microsoft and everything was documented, the style was always "half a page", the most direct and clear stuff you can imagine. The program managers were in charge of the comparative analysis with other products and competitors and there documents were always big like phone books, nevertheless, their style was the same.

7. You learn a lot more when you see how people use your system. Monitor usage and fix accordingly.

 One little story here. About 20 years ago I developed a system for some young let us call them secretaries to store and search information about patients. It turns out some information was changed, some deleted and they were not using their respective accounts and they blamed each other. I changes all their passwords and recorded every action in a database table used for recording this. The problem happened again, I went back to my desk and returned before the discussion was finished. I pointed at one of the girls and said: you did it, this day at this time. We never had that problem again. 

8. Unit testing is a lot more effective than traditional QA. Use both at the beginning. [Unit Tests Are FIRST](https://pragprog.com/magazines/2012-01/unit-tests-are-first "pragprog.com")

 The whole point of doing automated unit test is that you never again need to use the debugger (once a year is ok, specially if you need to debug your tests). [Writing Great Unit Tests: Best and Worst Practices](http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/ "blog.stevensanderson.com"), contrary to popular belief you should mock internal things in the system, it is ok, to mock the database and to mock external systems, but not internal ones, so in a sense a unit test is also an internal integration test. But you should also use your very same unit tests as integration tests, by flipping a switch. The general rule for unit testing is "test everything that can fail". [Top 12 Selected Unit Testing Best Practices - Software Engineering Candies](http://www.sw-engineering-candies.com/blog-1/unit-testing-best-practices "www.sw-engineering-candies.com") And since some people recommend using one assert per test method, it means if 10 things can fail, you need to write 10 test methods, and all will look the same, the next will have just one more line than the previous. What is the purpose of this? You see a test fail and you don't need to debug it, you don't need to look at the test code, you see the name of the test and you know exactly what failed. This increases productivity 10x. 

9. Functional programming is the wave of the future. Learn Haskell.

10. For estimation, use past projects estimates corrected by actual data. You need hard data for this: use the number of screens, database tables, use cases, etc.

11. Version control is your friend.

12. Code should be DRY instead of WET.

 DRY stands for Don't Repeat Yourself, that means remove duplicated code, because repeated code is a maintenance nightmare, when you need to fix bugs, you need to search for all the repeated code, and if you work with more people, they will copy and paste faster than you can solve the bugs.

WET stands for Write Everything Twice and its ugly cousin Write Every Time, meaning the exact opposite of DRY: lots and lots of repeated code.

13. Cache oblivious algorithms.

14. Technical risks are controlled using prototypes.

15. Since all technical problems can be handled, all the projects problems reduce to organizational problems. That is why all the agile methodologies exist: to handle organizational problems. The key for success is "fail fast".

16. Write down the iteration retrospective and act upon it.

17. Write down and number all requirements. Use DSDM requirement scrubbing. Write down and number all design decisions used to solve conceptually all requirements. Create prototypes for each design decision.

18. Get into a gym and go every day. Even 10 minutes of light exercise will make you feel better.

19. Make sure your code runs on different operating systems and on different databases. Use continuous integration for that.

20. You are not being paid to write code, you are paid to write functionality. Code is just cost. There is cost for creating it, cost for debugging it, cost for auditing it, cost for storing it, cost for maintaining it, etc.

PS: Since this got so many good reviews, a bonus list for the true gurus:

1. Write small functions. At most 10 lines of code per function. (otherwise the unit tests are not that good). Uncle Bob says only 5 lines per function.

2. Asynchronous programming is much faster than synchronous programming. See vert.x

3. Manage exceptions appropriately, either propagate or handle. Don't eat exceptions.

4. Don't use threads directly. Use frameworks for handling threads, like work manager.

A way to do this using Java EE: [WorkManager (Java EE 5 SDK)](https://docs.oracle.com/javaee/5/api/javax/resource/spi/work/WorkManager.html "docs.oracle.com"), but this is an overkill for most apps. Is there one simpler than this one?

One simpler: [How to use java.util.concurrent.CountDownLatch](http://markusjais.com/how-to-use-java-util-concurrent-countdownlatch/ "markusjais.com"), but the problem is that I don't want the library to show it is using threads (it should work correctly with or without threads).

5. Learn about multimethods and protocols.