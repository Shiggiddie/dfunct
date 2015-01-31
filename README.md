# dfunct
Django-based Functional Test Platform

## Dependencies

- Homebrew installed version of PostgreSQL version 9.4.0
- Python 2.7.#
- virtualenv

### Philosophy

Functionally testing web applications is tedious and nearly impossible using modern unit testing frameworks.
Navigating through a web application, the tester may wish to validate various actions on a page, ensure certain content is displayed, etc.  Each of these various validations would denote "assertions" in unit testing frameworks, and yet if any of these assertions were to fail, the entire test case would be deemed a failure and the testing framework would relinquish control over to the test runner.

#### Let us explore this concept by example:

Website `foo.org` serves up paths `/1.html`, `/2.html`, and `/3.html` with `<h1>` elements with text `1`, `2`, and `3`, respectively.  These pages are served in numerical order based on user interaction on each page.  In addition to confirming that the user interaction itself behaves correctly, the tester wishes to confirm that the `<h1>` elements are properly displayed on each page.

In sudo code, the unit test would look something like:
sudo test code
```
navigate to foo.org
assert /1.html is served
assert <h1> element's content is "1"
complete user interaction to move forward to /2.html
assert /2.html is served
assert <h1> element's content is "2"
complete user interaction to move forward to /3.html
assert /3.html is served
assert <h1> element's content is "3"
```

We see that there are 6 asserts in the above unit test.  If any one of those asserts were to fail, the entire unit test would be considered a failure.

In the situation when any of the `assert /#.html is served` were to fail, we may very well wish to have the unit test fail, as this may be indicative of a fundamental failure in the back end's routing code.  However for the case of the `assert <h1> element's content is "#"` assertions, we may not want to halt all testing as this failure isn't indicative of a functionality error, and may be easily corrected in some front end code.  We still want to be notified of the failure of that assertion, but we do not want to end the entire test case if that assertion fails.

#### The Proposed Solution

A functional test framework must be able to discern between "assertions that should end the test case" and "assertions that are important to notify, but do not break the current test case".  That is where *dfunct* comes in, and it does so by differentiating `TestCase`s from `TestResult`s and `Validation`s.

A `TestCase` is an individual running test code against a website that has a single `TestResult` which will denote whether that running of test code was successful.  Throughout a `TestCase`, an unlimited number of `Validation`s may run, all of which will have their own assertions much akin to traditional unit test test cases.  If a `TestCase`'s `TestResult` is not a failure by virtue of that test's test code not running to fruition, the `TestResult` becomes the culmination of the various `Validations` that ran throughout the `TestCase`.

Finally, a set of `TestCase`s comprise a total `TestRun` from which individual `TestCase`s derive.

### Solution in Action

Many unit test framework conventions must be thrown out to realize this functional test framework, yet many unit test conventions are maintained at the `Validation` level.  In lieu of a trandition unit test framework, a Django ORM PostgreSQL DB test runner is adopted.

This is it...don't get scared now...
