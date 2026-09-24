"""Explanations for the Core Component decks."""
from . import E

EXPLAIN = {
    "core/01-computational-thinking-and-algorithms.pptx": {
        "The four components of computational thinking": E(
            "Computational thinking is the thinking you do before you write code.\n\n"
            "Decomposition: break a problem into smaller parts you can solve one at a time. A game becomes menus, "
            "player movement, scoring and saving.\n\n"
            "Pattern recognition: spot what's similar to problems you've already solved, so you can reuse code.\n\n"
            "Abstraction: ignore detail that doesn't matter and focus on the inputs, the outputs, what varies and "
            "what stays the same.\n\n"
            "Algorithmic design: write the solution as precise, ordered steps a computer can follow.",
            "A cinema booking system: decompose (choose film, pick seats, pay), recognise a pattern (seat choosing is "
            "like any grid), abstract (a seat is just row, number, taken or free), then design the algorithm.",
            [("What is abstraction?", "Removing unnecessary detail to focus on what matters."),
             ("How does pattern recognition save time?", "It lets you reuse solutions to similar problems."),
             ("Decompose a login system into three parts.", "E.g. enter details, check details, grant or refuse access.")]),
        "Three ways to express an algorithm": E(
            "The same algorithm can be written in three ways.\n\n"
            "A flowchart uses standard symbols: terminators for start and end, rectangles for processes, diamonds "
            "for decisions, parallelograms for input and output, joined by arrows. It shows the flow visually but is "
            "slow to draw for big problems.\n\n"
            "A written description lists the steps in order, using numbered or hierarchical markers (1, 1.1, 1.2). "
            "It's quick to write but can be ambiguous.\n\n"
            "Code is precise and can actually be run and tested, but you need to know the language to read it. You "
            "must be able to translate between all three.",
            "'Ask for a number; if it's even, print Even, otherwise print Odd' becomes a flowchart with one diamond, "
            "or Python using if n % 2 == 0.",
            [("Which flowchart symbol is used for input or output?", "A parallelogram."),
             ("Give one drawback of a written description.", "It can be ambiguous."),
             ("Why can code be tested when a flowchart can't?", "Code can actually be run.")]),
        "Actions that control the order of steps": E(
            "Every algorithm uses three actions to control the order of its steps.\n\n"
            "Sequence: steps run one after another, top to bottom.\n\n"
            "Selection: a condition decides which steps run. Python uses if, elif and else, or match case to compare "
            "one value against several options.\n\n"
            "Iteration: steps repeat. A for loop repeats a set number of times or once for each item in a list "
            "(count-controlled). A while loop repeats as long as a condition is true (condition-controlled), so the "
            "condition must eventually become false.",
            "A guessing game: generate a number (sequence), while the guess is wrong keep asking (iteration), if the "
            "guess is too high say 'lower' (selection).",
            [("Which Python loop is count-controlled?", "for."),
             ("What keywords does Python use for selection?", "if, elif, else, and match case."),
             ("What is the risk with a while loop?", "An infinite loop if the condition never becomes false.")]),
        "Working with algorithms": E(
            "You'll need to work with algorithms in four ways.\n\n"
            "Find the purpose and output: trace the algorithm with sample inputs, recording every variable in a trace "
            "table, to see what it does.\n\n"
            "Find and correct errors: look for logic errors such as a wrong comparison, a loop that stops one step "
            "early, or a variable that's never updated.\n\n"
            "Translate: turn a flowchart into code, or code into a written description.\n\n"
            "Design: build your own algorithm from sequence, selection and iteration, starting from the inputs and outputs.",
            "total = 0; for i in range(1, 5): total = total + i gives 10, not 15, because range(1, 5) stops at 4. "
            "The fix is range(1, 6).",
            [("What is a trace table?", "A table recording each variable's value at every step."),
             ("What does range(1, 5) produce?", "1, 2, 3, 4."),
             ("Where should you start when designing an algorithm?", "With the inputs and required outputs.")]),
    },
    "core/02-problem-solving-strategies.pptx": {
        "Three approaches": E(
            "Top-down: start with the whole problem and break it into smaller sub-problems until each is easy to "
            "code. It gives a clear structure.\n\n"
            "Bottom-up: start with small, working pieces, such as functions or libraries you already have, and "
            "combine them. It's quick when good components exist.\n\n"
            "Modularisation: split the program into self-contained modules, each with a clear job, inputs and outputs. "
            "Modules can be written and tested separately, shared across a team and reused in other projects.",
            "A school app is designed top-down (timetable, homework, messages), built from modules, and reuses an "
            "existing login module bottom-up.",
            [("Which approach starts with the whole problem?", "Top-down."),
             ("Give two benefits of modularisation.", "Separate testing, teamwork, reuse."),
             ("When is bottom-up useful?", "When reliable components already exist.")]),
        "Root cause analysis": E(
            "Fixing a symptom lets a bug come back. Root cause analysis finds why it happened.\n\n"
            "Five whys: keep asking 'why?' until you reach a cause you can fix.\n\n"
            "FMEA (Failure Mode and Effects Analysis): list every way part of the system could fail and the effect, "
            "then tackle the most serious.\n\n"
            "Event tree analysis: start from one event and map every outcome.\n\n"
            "Once found, the cause is logged, closed if fixed, or escalated to someone who can fix it.",
            "Users are charged twice. Why? The pay button can be clicked twice. Why? It isn't disabled after the "
            "first click. Why? The requirement was never written. Fix: disable the button and add the requirement.",
            [("What is the aim of the five whys?", "To find the root cause, not just the symptom."),
             ("What does FMEA list?", "Ways something could fail and their effects."),
             ("What happens to a root cause you can't fix yourself?", "It's escalated.")]),
    },
    "core/03-data-types-variables-and-data-structures.pptx": {
        "Standard data types": E(
            "Every value in a program has a data type, which decides what it can hold and what you can do with it.\n\n"
            "An integer is a whole number, such as 17. A float has a decimal part, such as 4.99. A string is text in "
            "quotes, such as 'Ali'. A Boolean is True or False.\n\n"
            "Choosing the right type avoids errors. You can do maths with integers and floats but not strings; "
            "'5' + '5' gives '55', not 10. Data that looks numeric but isn't used in calculations, such as a phone "
            "number, should be a string so leading zeros aren't lost.",
            "age = 17 (integer), price = 4.99 (float), name = 'Ali' (string), logged_in = True (Boolean), "
            "phone = '07700900123' (string).",
            [("What does '5' + '5' give in Python?", "'55'."),
             ("What type should a price be?", "Float."),
             ("Why store a phone number as a string?", "To keep leading zeros and because no maths is done on it.")]),
        "Scope and conversion": E(
            "Scope is where in a program a variable can be used.\n\n"
            "A local variable is created inside a function and only exists there. A global variable is created "
            "outside functions and can be read anywhere. Using mostly local variables makes code safer, because one "
            "function can't accidentally change another's data.\n\n"
            "Type conversion changes a value's type. input() always returns a string, so convert it before doing maths: "
            "int() for whole numbers, float() for decimals, str() to turn a number into text, bool() for True or False.",
            "age = int(input('Age? ')) converts the text '17' into the number 17. Without int(), age + 1 would cause an error.",
            [("What does input() always return?", "A string."),
             ("What is a local variable?", "A variable created inside a function and only usable there."),
             ("Why prefer local variables?", "Functions can't accidentally change each other's data.")]),
        "Data structures": E(
            "Data structures hold many values under one name.\n\n"
            "A list is an ordered, changeable collection: scores = [12, 7, 9]. Items are numbered from 0, so scores[0] "
            "is 12. Methods include append(), insert(), remove(), pop(), sort(), index() and count(), and len() "
            "gives its length.\n\n"
            "An array is an ordered collection of items of the same type, such as a set of sensor readings.\n\n"
            "A dictionary stores key and value pairs, so you look values up by name rather than position: "
            "user = {'name': 'Ali', 'age': 17}; user['age'] gives 17.",
            "A quiz stores questions in a list and each player's score in a dictionary: scores = {'Ali': 7, 'Sam': 9}.",
            [("What index is the first item in a Python list?", "0."),
             ("How do you add an item to the end of a list?", "list.append(item)."),
             ("When is a dictionary better than a list?", "When you want to look values up by a key.")]),
    },
    "core/04-operators-input-output-and-program-flow.pptx": {
        "Operators": E(
            "Arithmetic operators do maths: + - * /, ** for powers, // for integer division (the whole number part) "
            "and % for modulus (the remainder). 17 // 5 is 3 and 17 % 5 is 2.\n\n"
            "Relational operators compare values and give True or False: == (equal), != (not equal), <, >, <= and >=. "
            "Don't confuse = (assign) with == (compare).\n\n"
            "Boolean operators combine conditions: and (both true), or (either true) and not (reverses it).",
            "Is a number even? n % 2 == 0. Can someone vote? age >= 18 and registered. Is a user a guest? not logged_in.",
            [("What does 20 // 6 give?", "3."),
             ("What does 20 % 6 give?", "2."),
             ("What is the difference between = and ==?", "= assigns a value; == compares two values.")]),
        "Working with text files": E(
            "Text files let programs save data between runs.\n\n"
            "open() opens a file in a mode: 'r' to read, 'w' to write (replacing the contents) or 'a' to append "
            "(adding to the end). read() gets everything, readline() one line and readlines() a list of lines. "
            "write() adds text.\n\n"
            "Each line usually ends with a newline, so line.strip() removes it, and line.split(',') breaks a line "
            "into parts.\n\n"
            "Always close() the file, or use 'with open(...)', so data is saved and the file is released.",
            "with open('scores.txt', 'a') as f: f.write('Ali,12\\n') adds a score without deleting the others.",
            [("Which mode adds to a file without deleting it?", "'a' (append)."),
             ("What does line.split(',') do?", "Splits a line into a list at each comma."),
             ("What happens if you open an existing file with 'w'?", "Its contents are replaced.")]),
        "Iteration": E(
            "Iteration repeats code.\n\n"
            "A for loop is count-controlled. for i in range(5) runs five times, with i from 0 to 4. for name in names "
            "runs once for each item in a list. It can't loop forever by accident.\n\n"
            "A while loop is condition-controlled: it repeats as long as its condition is true. Use it when you don't "
            "know how many times, such as asking until a valid answer is entered. Something inside the loop must "
            "change the condition, or it becomes an infinite loop.",
            "while password != 'secret': password = input('Try again: ') keeps asking until the right password is typed.",
            [("How many times does for i in range(5) run?", "Five."),
             ("Which loop suits 'keep asking until valid'?", "A while loop."),
             ("What causes an infinite loop?", "The condition never becoming false.")]),
    },
    "core/05-functions-procedures-and-validation.pptx": {
        "Functions and procedures": E(
            "Subroutines are named blocks of code you can call whenever you need them, so you don't repeat code.\n\n"
            "A function may take parameters and must return a result, which the calling code can use.\n\n"
            "A procedure may take parameters but doesn't return a result; it just does something, such as printing "
            "or saving.\n\n"
            "Parameters are the values passed in. Using subroutines makes code shorter, easier to test and easier "
            "to change: fix the subroutine once and every call benefits.",
            "def vat(price): return price * 0.2 is a function: total = price + vat(price). def welcome(name): "
            "print('Hi', name) is a procedure.",
            [("What must a function do?", "Return a result."),
             ("What is a parameter?", "A value passed into a subroutine."),
             ("Why use subroutines?", "Avoid repeated code; easier to test and change.")]),
        "Where subroutines come from": E(
            "You don't have to write every subroutine yourself.\n\n"
            "User-written subroutines do exactly what you need, but you must write and test them.\n\n"
            "Built-in functions, such as len(), round() and max(), are always available, reliable and fast.\n\n"
            "Standard libraries, such as math and random, are part of Python but need importing: import math, then "
            "math.sqrt(16).\n\n"
            "Third-party libraries, such as pandas and Matplotlib, add powerful features but create dependencies to "
            "install and update, and can introduce security risks.",
            "Rolling a dice: import random, then random.randint(1, 6): one line instead of writing your own "
            "random number generator.",
            [("How do you use a standard library function?", "Import the library, then call it."),
             ("Give one risk of third-party libraries.", "Dependencies to maintain, or security vulnerabilities."),
             ("Name two built-in functions.", "E.g. len(), round(), max(), min().")]),
        "Validation checks": E(
            "Validation checks input is sensible before the program uses it.\n\n"
            "Presence: something was entered (if name != ''). Length: the right number of characters "
            "(if len(password) >= 8). Range: within limits (if 1 <= guests <= 8). Type: the right data type "
            "(if value.isdigit()). Format: matches a pattern, such as containing '@'. Check digit: a calculated digit "
            "at the end confirms the rest, as in barcodes and ISBNs.\n\n"
            "Validation stops crashes and bad data, but it can't tell whether data is true, only that it's reasonable.",
            "while not age.isdigit(): age = input('Please enter a number: ') keeps asking until the input is numeric.",
            [("Write a range check for a mark from 0 to 100.", "if 0 <= mark <= 100:"),
             ("What does a check digit protect against?", "Mistyped digits in codes such as barcodes."),
             ("Can validation prove data is correct?", "No, only that it's reasonable.")]),
    },
    "core/06-programming-practice-and-robust-code.pptx": {
        "Design considerations": E(
            "Good code isn't just code that works.\n\n"
            "Logical order: put actions in the right order so results are correct, such as validating input before "
            "using it.\n\n"
            "Efficiency: choose data structures and steps that save time and memory, such as not repeating a "
            "calculation inside a loop when it could be done once.\n\n"
            "Naming: use meaningful names in one consistent style. Python uses snake_case (total_score); some "
            "languages use camelCase (totalScore).\n\n"
            "Presentation: whitespace, consistent indentation and sensible line lengths make code readable and maintainable.",
            "x = a * b means nothing; area = width * height explains itself. Future you, and your teammates, will thank you.",
            [("Which naming style does Python use?", "snake_case."),
             ("Give one way to make code more efficient.", "E.g. avoid repeating calculations inside a loop."),
             ("Why do meaningful names matter?", "They make code easier to read and maintain.")]),
        "Characteristics of robust code": E(
            "Robust code keeps working when things go wrong.\n\n"
            "It handles unexpected input: validating everything the user types, so letters in a number field don't "
            "crash the program.\n\n"
            "It handles unexpected termination: files that don't exist, lost network connections or full disks are "
            "caught with try and except instead of crashing.\n\n"
            "It gives specific, meaningful error messages that tell the user what went wrong and what to do.\n\n"
            "Debugging, finding and fixing errors, is how code becomes robust.",
            "try: mark = int(input('Mark: ')) except ValueError: print('Please type a whole number, like 72.')",
            [("What does try and except do?", "Catches errors so the program doesn't crash."),
             ("What makes an error message meaningful?", "It says what went wrong and what to do."),
             ("Give an example of unexpected termination.", "E.g. a missing file or lost network connection.")]),
        "Types of error": E(
            "Syntax errors break the language's rules, such as a missing colon or bracket. The program won't run at "
            "all, and the error message usually points to the line.\n\n"
            "Runtime errors happen while the program runs, such as dividing by zero or opening a file that doesn't "
            "exist. The program crashes unless the error is handled.\n\n"
            "Logic errors are the hardest: the program runs but gives the wrong result, such as using < instead of <=. "
            "Find them with tracing, print statements and an IDE's breakpoints.",
            "if score > 50 when the pass mark is 50 or more is a logic error: a score of exactly 50 is wrongly failed.",
            [("Which error stops a program running at all?", "A syntax error."),
             ("Is dividing by zero a syntax, runtime or logic error?", "Runtime."),
             ("How can you find logic errors?", "Tracing, print statements, breakpoints.")]),
    },
    "core/07-searching-and-sorting-algorithms.pptx": {
        "Searching": E(
            "A linear search checks each item in turn from the start until it finds the target or reaches the end. "
            "It works on any list, sorted or not, and is simple, but it's slow on large lists: in the worst case it "
            "checks every item.\n\n"
            "A binary search only works on sorted data. It checks the middle item; if that isn't the target, it "
            "throws away the half that can't contain it and repeats on the other half. Each step halves the search, "
            "so it's very fast on large lists.",
            "Finding 70 in a sorted list of 1,000 numbers: linear might need 1,000 checks; binary needs about 10, "
            "because 2 to the power 10 is 1,024.",
            [("What must be true before a binary search?", "The data must be sorted."),
             ("What is the worst case for linear search?", "Checking every item."),
             ("How much does each binary search step remove?", "Half of the remaining items.")]),
        "Sorting algorithms": E(
            "Bubble sort compares neighbouring items and swaps them if they're in the wrong order, making passes "
            "until a pass makes no swaps. Simple, but slow on big lists.\n\n"
            "Insertion sort takes each item in turn and inserts it into the correct place in the sorted part of the "
            "list. It's efficient for small or nearly sorted lists.\n\n"
            "Merge sort splits the list into single items, then merges pairs back together in order until one "
            "sorted list remains. It's fast on large lists but needs extra memory for the merging.",
            "Sorting [5, 2, 4]: bubble sort swaps 5 and 2 to give [2, 5, 4], then 5 and 4 to give [2, 4, 5]; the next "
            "pass makes no swaps, so it stops.",
            [("How does bubble sort know it has finished?", "A pass makes no swaps."),
             ("Which sort suits nearly sorted data?", "Insertion sort."),
             ("What is merge sort's drawback?", "It needs extra memory.")]),
        "Comparing algorithms": E(
            "Algorithms that do the same job can perform very differently.\n\n"
            "Compare them by execution time (how long they take as the data grows), memory use (merge sort needs "
            "extra space; bubble and insertion sort work in place) and the number of comparisons they make.\n\n"
            "Think about best, worst and average cases. Bubble sort on an already sorted list finishes in one pass "
            "(best case) but on a reversed list needs the maximum number of passes (worst case).\n\n"
            "Choose the algorithm that suits the data size and situation.",
            "Sorting a class list of 30 names: insertion sort is fine. Sorting 5 million transactions overnight: merge sort.",
            [("Name three ways to compare algorithms.", "Execution time, memory use, number of comparisons."),
             ("What is bubble sort's best case?", "Data already sorted: one pass."),
             ("Which sort would you use for millions of records?", "Merge sort.")]),
    },
    "core/08-testing.pptx": {
        "Testing methods": E(
            "Test components separately before combining them, because a bug is far easier to find in a small piece.\n\n"
            "Unit testing checks one function or module; integration testing checks modules working together; system "
            "testing checks the whole program; acceptance testing checks it meets the user's requirements.\n\n"
            "Boundary testing uses edge values. Performance, load and stress testing check speed under normal, heavy "
            "and extreme use. Usability testing checks it's easy to use. Regression testing checks a change hasn't "
            "broken old features. Closed box testing uses only inputs and outputs; open box uses knowledge of the code.",
            "A shop's checkout: unit test the total function, integration test basket plus payment, load test 1,000 "
            "shoppers, then regression test after every change.",
            [("What does unit testing check?", "One function or module on its own."),
             ("Why run regression tests after a change?", "To check old features still work."),
             ("What is the difference between closed and open box testing?", "Closed uses only inputs and outputs; open uses knowledge of the code.")]),
        "Test data": E(
            "Good tests use four kinds of data.\n\n"
            "Valid (normal) data should be accepted. Invalid data is the right type but breaks the rules and should "
            "be rejected. Boundary data sits exactly at the edges, where bugs often hide, such as < instead of <=. "
            "Erroneous data is the wrong type altogether, such as text where a number is expected.\n\n"
            "Test every kind so you know the program handles normal use, mistakes and edge cases without crashing.",
            "A field accepts 1 to 8 guests. Valid: 4. Invalid: 12. Boundary: 1 and 8. Erroneous: 'four'.",
            [("Why test boundary values?", "Bugs often hide at the edges."),
             ("A mark field accepts 0 to 100. Give an erroneous value.", "Any non-number, e.g. 'fifty'."),
             ("What should happen with invalid data?", "It should be rejected with a helpful message.")]),
        "Structure of a test plan": E(
            "A test plan makes testing organised and repeatable. Each test is a row.\n\n"
            "Identify the test (what's being tested), describe its purpose (why), identify the test data (the exact "
            "values), describe the expected result (written before running it) and record the actual result.\n\n"
            "When the actual result differs from the expected, you've found a bug: fix it and retest.\n\n"
            "Tests you run often can be automated with scripts, macros or testing tools, so they rerun after every change.",
            "Test 5: guests upper boundary. Purpose: check 8 is accepted. Data: 8. Expected: accepted. Actual: rejected. "
            "The code uses < 8 instead of <= 8.",
            [("Why write the expected result first?", "So the actual result can be judged fairly."),
             ("What should you do when a test fails?", "Fix the bug and retest."),
             ("How can repeated tests be automated?", "With scripts, macros or testing tools.")]),
    },
    "core/09-emerging-issues-and-technologies.pptx": {
        "Impact of digital technologies": E(
            "Digital technology changes how organisations work: communication moves online, people are expected to "
            "be more productive and available, staff are monitored more, remote and hybrid working are normal, and "
            "automation and AI take over routine tasks.\n\n"
            "It also changes society: some jobs disappear and new skills are needed, fewer decisions involve humans, "
            "privacy is harder to protect and behaviour changes. Access to information and services improves for "
            "many, but people without skills, devices or internet risk being left out. Generative AI and "
            "globalisation are speeding this up.",
            "AI coding assistants speed up routine code, so developers spend more time on design, testing and "
            "checking the AI's output.",
            [("Give two impacts of technology on organisations.", "E.g. remote working, monitoring, automation."),
             ("Give one negative impact on society.", "E.g. job losses, privacy concerns, isolation."),
             ("How is AI changing developers' work?", "Less routine coding, more design, testing and review.")]),
        "Digital inclusion": E(
            "Digital inclusion means everyone can use digital products fairly.\n\n"
            "It needs suitable technology and connectivity, design that follows accessibility best practice, and, "
            "for public sector services, meeting accessibility regulations by law.\n\n"
            "Developers must also check datasets for bias. An AI trained on data that under-represents some groups "
            "will treat those groups unfairly.\n\n"
            "Think about users' age, digital and literacy skills, whether they're staff or the public, culture, and "
            "accessibility needs such as screen readers or limited mobility.",
            "A face-unlock feature trained mostly on lighter skin tones fails more often for darker-skinned users: "
            "biased data, unfair product.",
            [("What is digital inclusion?", "Everyone being able to use digital products fairly."),
             ("Why check datasets for bias?", "Biased data produces unfair software."),
             ("Name two user characteristics that affect inclusion.", "E.g. age, digital skills, accessibility needs.")]),
        "Emerging technologies": E(
            "Several technologies are changing what developers build.\n\n"
            "Quantum computing could solve problems ordinary computers can't. The Internet of Things connects "
            "billions of devices, with edge computing processing data close to where it's collected. AI and machine "
            "learning power recommendations and generative tools. Augmented and virtual reality create new "
            "interfaces. Open source software and blockchain change how code and data are shared. Autonomous "
            "machines, such as self-driving cars, rely on software to make decisions.\n\n"
            "All have environmental costs: rare metals, energy use and disposal.",
            "A smart-farm app combines IoT soil sensors, edge computing on a field hub, and machine learning to "
            "decide when to water.",
            [("What is edge computing?", "Processing data close to where it's collected."),
             ("Give one environmental cost of technology.", "E.g. rare metals, energy use, disposal."),
             ("What does machine learning do?", "Finds patterns in data to make predictions.")]),
    },
    "core/10-legislation-and-guidelines.pptx": {
        "Health and safety for digital work": E(
            "Software developers spend long hours at screens, so health and safety law still matters.\n\n"
            "Under the Health and Safety at Work Act, employers must provide a safe environment, training, welfare "
            "facilities, and information, instruction and supervision.\n\n"
            "Display screen equipment (DSE) rules require workstation assessments (chair, screen height, lighting), "
            "regular breaks from the screen, eye tests on request, and training.\n\n"
            "Without them, developers risk eye strain, headaches, and back, neck and wrist problems.",
            "A developer with wrist pain gets a DSE assessment, leading to a better keyboard position, a mouse "
            "change and scheduled micro-breaks.",
            [("What must employers provide DSE users on request?", "An eye test."),
             ("Name two health risks of long screen use.", "E.g. eye strain, back, neck or wrist pain."),
             ("What does a workstation assessment check?", "E.g. chair, screen height, lighting.")]),
        "Key legislation": E(
            "Developers must build software that respects the law.\n\n"
            "The Data Protection Act and UK GDPR control how personal data is collected, used and kept, under eight "
            "principles such as using data fairly, only for stated purposes, keeping it accurate and secure.\n\n"
            "The Computer Misuse Act 1990 makes unauthorised access, access intending further crimes, and damaging "
            "systems illegal.\n\n"
            "Equality law protects nine characteristics, so software mustn't discriminate. Intellectual property law "
            "protects designs and patents. Some offences fall under international law.",
            "An app that quietly collects users' locations without consent breaks data protection law, however "
            "useful the data is.",
            [("Which law covers personal data?", "The Data Protection Act / UK GDPR."),
             ("What does the Computer Misuse Act make illegal?", "Unauthorised access and damaging systems."),
             ("How many protected characteristics are there?", "Nine.")]),
        "Guidelines": E(
            "Beyond the law, guidelines describe professional practice.\n\n"
            "Codes of conduct from employers, professional bodies such as BCS, the Institution of Analysts and "
            "Programmers and CIISec, and government expect you to follow policy and law, minimise risk to the "
            "public, work with competence and integrity, meet deadlines and keep confidentiality.\n\n"
            "Industry standards include ISO, WCAG (web accessibility), W3C and IETF (web and internet), BS, IEEE and "
            "PCI SSC (card payments).\n\n"
            "Acceptable use policies set rules for using IT, and whistleblowing procedures let staff report "
            "wrongdoing safely.",
            "Following WCAG means adding alt text to images and keyboard navigation, so blind and motor-impaired "
            "users can use your site.",
            [("Which standard covers web accessibility?", "WCAG."),
             ("Name a professional body for developers.", "E.g. BCS, IAP."),
             ("What is whistleblowing?", "Safely reporting wrongdoing in an organisation.")]),
    },
    "core/11-the-business-context.pptx": {
        "The business environment": E(
            "Organisations provide products or services. The private sector (SMEs, large enterprises and NGOs) "
            "usually aims for profit; the public sector is run by government; the voluntary or charity sector is "
            "not for profit.\n\n"
            "Business models describe the customer: B2C sells to consumers, B2B to other businesses, B2M to a mass "
            "market.\n\n"
            "Stakeholders are everyone affected: internal ones (owners, directors, employees) and external ones "
            "(customers, suppliers, shareholders, investors and government). Good software meets their different needs.",
            "A company selling accounting software to small firms is private sector and B2B.",
            [("What does B2C mean?", "Business to consumer."),
             ("Is a supplier an internal or external stakeholder?", "External."),
             ("Which sector is not for profit?", "The voluntary or charity sector.")]),
        "What users expect from software": E(
            "Software must meet users' needs and quality expectations to add value.\n\n"
            "Functionality: it does the job properly. Fewer pain points: fast responses and simple tasks. "
            "Accessibility: usable by everyone. Compatibility: works with older (legacy) systems, future systems and "
            "external services. Availability: minimal downtime. Support: good help for users and easy installation.\n\n"
            "Software that misses these gets abandoned, however clever its code.",
            "A banking app that takes 10 seconds to log in has a pain point. Users switch to a rival even if every feature works.",
            [("What is a pain point?", "Something that frustrates users, e.g. slow response."),
             ("Why does compatibility matter?", "Software must work with other existing and future systems."),
             ("Give two quality expectations.", "Any two: functionality, accessibility, compatibility, availability, support.")]),
        "Risks and impacts": E(
            "Relying on software brings risks: security and privacy breaches, breaking laws or regulations, excluding "
            "users through bias or poor design, being overtaken by rival technology, and systems failing or not "
            "being fit for purpose.\n\n"
            "The impacts can be serious: legal action, fines, reputational damage, losing a licence to operate and losing business.\n\n"
            "Developers reduce these risks through secure, tested, accessible, well-designed code.",
            "A retailer's website leaks card details through an SQL injection flaw: fines, lawsuits and lost customers.",
            [("Name two risks of relying on software.", "E.g. breaches, non-compliance, exclusion, failure."),
             ("Give two impacts of a data breach.", "E.g. fines, legal action, reputational damage."),
             ("How can developers reduce these risks?", "Secure, tested, accessible code.")]),
    },
    "core/12-technical-change-management.pptx": {
        "Triggers for change": E(
            "Organisations change their systems when something pushes them.\n\n"
            "Internal triggers include restructuring, expansion or downsizing, new strategic objectives, and crises "
            "such as a cyber attack.\n\n"
            "External triggers are summed up by PESTLE: Political (new government policy), Economic (recession, "
            "competitors), Social (trends such as remote working), Technological (new technology, zero-day "
            "vulnerabilities), Legal (new laws) and Environmental (sustainability targets).",
            "New accessibility regulations (legal) force a council to redesign its online forms.",
            [("What does PESTLE stand for?", "Political, Economic, Social, Technological, Legal, Environmental."),
             ("Give one internal trigger.", "E.g. expansion, restructuring, a cyber attack."),
             ("Which PESTLE factor is a zero-day vulnerability?", "Technological.")]),
        "The change management process": E(
            "Changing live software safely follows a process.\n\n"
            "Identify the change and have the Change Advisory Board (CAB) review, prioritise and approve it. Set "
            "SMARTER objectives, forecast the impact and allocate resources. Communicate risks and impact to "
            "stakeholders. Configure and fully test the new system in a test environment. Choose an implementation "
            "method. Document everything, plan a rollback, train users, monitor progress, and use version control "
            "software to track every change and return to earlier versions if needed.",
            "Version control means a release that breaks the checkout can be rolled back to yesterday's working "
            "version in minutes.",
            [("What does the CAB do?", "Reviews, prioritises and approves change requests."),
             ("Why plan a rollback?", "To undo the change if it fails."),
             ("How does version control help?", "Tracks every change and lets you return to earlier versions.")]),
        "Implementation methods": E(
            "Direct: switch the old system off and the new one on at once. Fast and cheap, but risky.\n\n"
            "Parallel: run both together for a while. Safe, but staff do double the work.\n\n"
            "Phased: introduce the system one part at a time. Lower risk, but slower.\n\n"
            "Pilot: one team or site tries it first. Problems are found on a small scale before everyone switches.",
            "A new school app is piloted with one year group, fixed based on their feedback, then rolled out to everyone.",
            [("Which method is riskiest?", "Direct."),
             ("Which method means double work for staff?", "Parallel."),
             ("What is a pilot?", "One team or site uses the system first.")]),
    },
    "core/13-data-fundamentals.pptx": {
        "Data, information and knowledge": E(
            "Data is raw facts with no context, such as 15, 22, 9.\n\n"
            "Information is data with context: 'minutes each user spent in the app today'.\n\n"
            "Knowledge is understanding applied to information to make decisions: 'users drop off after 10 minutes, "
            "so simplify the menu'.\n\n"
            "Apps collect data so it can become information and, eventually, knowledge that improves the product.",
            "Data: 3, 3, 3 taps. Information: users tap 'Back' three times to find settings. Knowledge: move "
            "settings to the home screen.",
            [("What turns data into information?", "Context."),
             ("What is knowledge?", "Understanding applied to information to make decisions."),
             ("Is '15, 22, 9' data or information?", "Data.")]),
        "Data taxonomy": E(
            "Quantitative data is structured: numbers and categories that fit neatly in tables. It can be discrete "
            "(whole counts, like downloads), continuous (measurements, like response time) or categorical (fixed "
            "groups, like device type).\n\n"
            "Qualitative data is unstructured: free text, images, audio and video. It's stored as a whole object, or "
            "codified into structured data, for example by tagging reviews as positive or negative.\n\n"
            "The type of data affects how you store, search and analyse it.",
            "App store data: star rating (categorical), number of reviews (discrete), load time (continuous), review "
            "text (qualitative).",
            [("Is 'number of downloads' discrete or continuous?", "Discrete."),
             ("Is a written review quantitative or qualitative?", "Qualitative."),
             ("How can qualitative data be structured?", "By codifying it, e.g. tagging.")]),
        "Data types and formats": E(
            "Data types include integer and real (numbers), character and string (text), Boolean (true or false), "
            "date, and Blob (binary objects such as images).\n\n"
            "Data formats decide how data is saved or sent. CSV stores comma-separated values, one record per line. "
            "JSON stores key and value pairs and is the standard for web APIs. XML wraps data in named tags. Plain "
            "text suits logs. ASCII and UTF-8 are character encodings; UTF-8 supports every language, so it's used "
            "on the web.",
            "The same product as JSON: {\"name\": \"Mug\", \"price\": 6.5, \"in_stock\": true}. As CSV: Mug,6.5,True.",
            [("Which format is used by most web APIs?", "JSON."),
             ("Why use UTF-8?", "It supports characters from every language."),
             ("What is a Blob?", "A binary large object, such as an image.")]),
    },
    "core/14-data-quality-systems-and-analysis.pptx": {
        "The six Vs of Big Data": E(
            "Big Data is data too big or complex for ordinary tools, described by six Vs: volume (amount), variety "
            "(many types), variability (changing meaning and flow), velocity (speed of arrival), veracity (how "
            "trustworthy it is) and value (the insight it gives).\n\n"
            "Data quality is maintained through validation, verification, reliability, consistency, integrity and "
            "redundancy. Maintaining data costs time, skills and money.",
            "A social media platform handles billions of posts a day (volume, velocity) in text, images and video "
            "(variety), some from bots (veracity).",
            [("Which V is about speed?", "Velocity."),
             ("Which V is about trustworthiness?", "Veracity."),
             ("Name one data quality method.", "E.g. validation, verification, consistency.")]),
        "Data wrangling": E(
            "Data wrangling gets raw data ready to use in five steps: structure it into a usable layout, clean it "
            "(fix errors, remove duplicates), validate it against rules, enrich it with useful extra data, and output it.\n\n"
            "Data entry errors cause many problems. Transcription errors are copying mistakes; transposition errors "
            "swap characters (1234 becomes 1243). Validation, double-entry verification, drop-down menus and "
            "pre-filled boxes reduce them.\n\n"
            "In Python, pandas is the usual tool for wrangling a CSV file.",
            "df.drop_duplicates() removes repeated rows; df['country'].replace('U.K.', 'UK') makes values consistent.",
            [("Name the five wrangling steps.", "Structure, clean, validate, enrich, output."),
             ("What is a transposition error?", "Swapping characters, e.g. 1234 to 1243."),
             ("Which Python library is used for wrangling CSV data?", "pandas.")]),
        "Visualisation and data models": E(
            "Data visualisation presents data so people understand it: graphs, charts, tables, reports, dashboards "
            "and infographics. Choose based on the type of data, the audience and the brief. A line graph shows "
            "trends over time; a bar chart compares categories.\n\n"
            "Data models organise stored data. Hierarchical: a tree of parents and children. Network: records with "
            "many links. Relational: tables linked by keys, the most common because it avoids duplicated data and is "
            "easy to query with SQL.",
            "Matplotlib: plt.plot(months, sales); plt.title('Sales by month'); plt.xlabel('Month'); plt.show() "
            "produces a labelled trend line.",
            [("Which chart shows a trend over time?", "A line graph."),
             ("Which data model uses linked tables?", "Relational."),
             ("Why label chart axes?", "So the audience understands what's shown.")]),
    },
    "core/15-hardware-and-software.pptx": {
        "Hardware": E(
            "The processor runs instructions: more cores do more at once, a higher clock speed does each faster, and "
            "cache keeps data close. RAM holds running programs and data but is volatile. ROM holds start-up "
            "instructions. Storage can be magnetic, solid state or optical.\n\n"
            "The motherboard connects everything, the GPU handles graphics and parallel work, network interfaces "
            "connect via PCI or USB, and cooling stops overheating.\n\n"
            "Developers need enough RAM and CPU to run IDEs, emulators and virtual machines smoothly.",
            "Running a phone emulator alongside an IDE needs 16 GB of RAM or more; with 8 GB, everything slows to a crawl.",
            [("Which memory is volatile?", "RAM."),
             ("What does a GPU do?", "Graphics and parallel processing."),
             ("Why do developers need plenty of RAM?", "To run IDEs, emulators and VMs together.")]),
        "Code development tools": E(
            "An IDE (integrated development environment) puts everything a developer needs in one place: an editor "
            "with syntax highlighting and auto-complete, debugging tools such as breakpoints and variable watches, "
            "and often screen design tools.\n\n"
            "Code must be translated into machine code. A compiler translates the whole program in advance into an "
            "executable file, which then runs fast. An interpreter translates and runs code line by line, which is "
            "slower but makes testing and debugging easier.\n\n"
            "Python is usually interpreted; C# is compiled.",
            "Setting a breakpoint in an IDE pauses the program on a chosen line, so you can inspect every variable and "
            "step through the code.",
            [("What is the difference between a compiler and an interpreter?", "A compiler translates the whole program first; an interpreter translates line by line."),
             ("Name two IDE features.", "E.g. editor, debugger, breakpoints, syntax highlighting."),
             ("Is Python usually compiled or interpreted?", "Interpreted.")]),
    },
    "core/16-networks.pptx": {
        "Network types and topologies": E(
            "Networks range from PANs (around one person) and LANs (one site) to MANs (a city) and WANs (countries). "
            "A VPN creates a private, encrypted connection across a public network.\n\n"
            "In a star topology every device connects to a central switch; in a mesh devices connect to many others "
            "for resilience; a tree links stars in a hierarchy.\n\n"
            "In the client-server model, servers provide services such as APIs and databases to clients, which is "
            "how most apps work. In peer-to-peer, devices are equal and share directly.",
            "A mobile app (client) sends requests over a WAN, the internet, to a server running the app's API and database.",
            [("What is a VPN?", "A private, encrypted connection across a public network."),
             ("How do most apps use networks?", "The client-server model."),
             ("What is the internet?", "The largest WAN.")]),
        "Data packets": E(
            "Data is sent in packets. Each has a header (source and destination addresses, packet number, protocol), "
            "a payload (the data) and a trailer with error checking.\n\n"
            "Packets may take different routes and are reassembled in order. A cyclic redundancy check (CRC) detects "
            "damaged packets so they can be resent. Packets can be lost through congestion or faults.\n\n"
            "Bandwidth is how much data can flow; latency is the delay. High latency makes apps feel slow even on a "
            "fast connection.",
            "A multiplayer game sends small, frequent packets. Low latency matters more than high bandwidth, or "
            "players see lag.",
            [("What does a packet header contain?", "Addresses, packet number and protocol."),
             ("What is a CRC for?", "Detecting damaged packets."),
             ("Why does latency matter for games?", "High latency causes lag.")]),
        "Common protocols": E(
            "HTTP transfers web pages and API requests; HTTPS encrypts them. SMTP sends email; POP downloads it; "
            "IMAP keeps it on the server and syncs. RIP and OSPF let routers share routes. FTP transfers files and "
            "SFTP does so securely. DHCP gives devices IP addresses. DNS turns domain names into IP addresses.\n\n"
            "Developers meet HTTPS and DNS constantly: every API call looks up a name and sends an encrypted request.",
            "When an app calls a weather API, DNS first finds the server's IP address, then HTTPS sends the request "
            "and receives the forecast securely.",
            [("Which protocol should APIs use?", "HTTPS."),
             ("What does DNS do?", "Turns domain names into IP addresses."),
             ("What is the difference between FTP and SFTP?", "SFTP is secure (encrypted).")]),
    },
    "core/17-virtual-cloud-and-resilient-environments.pptx": {
        "Virtual environments": E(
            "Virtualisation runs virtual machines (VMs) on one physical computer, managed by a hypervisor. Type 1 "
            "hypervisors run directly on hardware in data centres; Type 2 run on a normal OS, like VirtualBox on a laptop.\n\n"
            "VMs are isolated and portable, so they're cheap at scale, easy to manage, good for disaster recovery "
            "and ideal for testing: developers can test software on different operating systems without extra "
            "hardware.\n\n"
            "Drawbacks: extra load on the hardware, slightly slower running, and performance figures that may not "
            "match real machines.",
            "A developer tests their app on Windows 10, Windows 11 and Ubuntu VMs, all on one laptop.",
            [("What manages virtual machines?", "A hypervisor."),
             ("Why are VMs useful for developers?", "Testing on different systems without extra hardware."),
             ("Give one drawback of virtualisation.", "Extra hardware load or slower running.")]),
        "Cloud delivery models": E(
            "Cloud computing rents computing over the internet, public or private, bringing portability, elasticity, "
            "fewer storage limits and lower costs.\n\n"
            "IaaS: the provider supplies virtual hardware; you manage the OS, runtime, apps and data.\n\n"
            "PaaS: the provider also manages the OS and runtime; you just deploy your code and manage data and users. "
            "It's popular with developers.\n\n"
            "SaaS: the provider runs the whole application; you only manage users and data.",
            "Deploying a Python web app to a platform that handles servers and updates is PaaS. Using Google Docs is SaaS.",
            [("Which model suits a developer who just wants to deploy code?", "PaaS."),
             ("In IaaS, who manages the OS?", "The client."),
             ("What is elasticity?", "Scaling resources up and down with demand.")]),
        "Making environments resilient": E(
            "Resilient systems keep working, or recover fast, when things go wrong. They're more secure, protect "
            "reputation and cut downtime.\n\n"
            "Methods include patching software, replacing hardware on a plan, redundant systems and data, hardening "
            "devices, backups (onsite, offsite and cloud) with tested recovery, hot, warm or cold standby sites, and "
            "standard procedures with trained staff.",
            "An app runs in two cloud regions. When one data centre fails, traffic switches to the other and users "
            "don't notice.",
            [("What is redundancy?", "Duplicates so one failure doesn't stop the service."),
             ("Why test backups?", "To make sure they can be restored."),
             ("What is a hot site?", "A fully ready backup site.")]),
    },
    "core/18-security-threats-and-vulnerabilities.pptx": {
        "Technical threats": E(
            "Many attacks target software directly.\n\n"
            "SQL injection: an attacker types database commands into an input box, and badly written code runs them. "
            "Cross-site scripting: malicious scripts are injected into web pages other users see. Buffer overflow: "
            "input longer than expected overwrites memory. Brute force: trying every password.\n\n"
            "Insecure APIs lack proper authentication or input checks. Man-in-the-middle attacks intercept traffic. "
            "Malware, DDoS attacks from botnets, and social engineering such as phishing are also common.",
            "Typing ' OR '1'='1 into a login box can log an attacker in if the code builds the SQL query by joining "
            "strings together.",
            [("What is SQL injection?", "Inserting database commands through input so the code runs them."),
             ("What makes an API insecure?", "Missing authentication or input validation."),
             ("What is a man-in-the-middle attack?", "Intercepting communication between two parties.")]),
        "Developer defences": E(
            "Developers can prevent many attacks in their code.\n\n"
            "Use parameterised queries so user input is never treated as SQL. Escape output and validate input to "
            "stop cross-site scripting. Check input lengths to prevent buffer overflows. Secure APIs with "
            "authentication, API keys, rate limits and input validation. Prevent brute force with account lockout, "
            "MFA and strong password rules.\n\n"
            "Store passwords only as salted hashes, never in plain text.",
            "cursor.execute('SELECT * FROM users WHERE name = ?', (name,)) keeps the input as data, so injection fails.",
            [("How do you prevent SQL injection?", "Parameterised queries."),
             ("How should passwords be stored?", "As salted hashes."),
             ("Name two ways to secure an API.", "E.g. authentication, API keys, rate limits, validation.")]),
        "Human and physical risks": E(
            "People and places create risk too.\n\n"
            "Human error, such as deleting the wrong data, is reduced by confirmation boxes and training. Malicious "
            "employees are dealt with by removing access quickly. Disguised criminals are stopped by ID checks. Poor "
            "cyber hygiene, such as unlocked screens or reused passwords, is fixed with training and password managers.\n\n"
            "Vulnerabilities include weak encryption, poor password policy, no MFA, out-of-date software with known "
            "or zero-day flaws, poor physical access control, shoulder surfing and natural disasters.",
            "A developer who commits an API key to a public code repository has made a human error that attackers "
            "can exploit within minutes.",
            [("What is a zero-day?", "A flaw exploited before a patch exists."),
             ("How can human error be reduced?", "E.g. confirmation boxes, training."),
             ("Why shouldn't secrets be committed to repositories?", "Anyone who can see the repository can use them.")]),
    },
    "core/19-threat-mitigation-cia-and-iaaa.pptx": {
        "Mitigation techniques": E(
            "Layered defences protect systems.\n\n"
            "Protect devices with security settings, anti-malware, hardening and updates. Control access with access "
            "policies, MFA and password managers. Protect data with encryption: hashing (one way, for passwords), "
            "symmetric (one shared key) and asymmetric (a public and private key pair); and back it up. Protect "
            "networks with intrusion detection, VPNs, air gaps and certified APIs. Vet and train staff, and test "
            "defences with port scanning and ethical penetration testing.",
            "An API protected by HTTPS, API keys, rate limiting and input validation shrugs off most automated attacks.",
            [("Which encryption type is one way?", "Hashing."),
             ("What is ethical hacking?", "Authorised testing to find weaknesses."),
             ("Why use MFA?", "A stolen password alone isn't enough to log in.")]),
        "The CIA triad": E(
            "The CIA triad is the three goals of security.\n\n"
            "Confidentiality: only authorised people can access data, using access control and encryption.\n\n"
            "Integrity: data isn't tampered with, using permissions, hashing and validation. Confidentiality supports integrity.\n\n"
            "Availability: data and systems are there when needed, using backups, redundancy and DDoS protection. "
            "Integrity makes availability worthwhile.",
            "A DDoS attack on an online shop breaks availability; an attacker changing prices breaks integrity; "
            "leaked customer data breaks confidentiality.",
            [("Which property does a DDoS attack target?", "Availability."),
             ("What does integrity mean?", "Data hasn't been tampered with."),
             ("How is confidentiality protected?", "Access control and encryption.")]),
        "The IAAA model": E(
            "IAAA is how systems control users.\n\n"
            "Identification: the user claims an identity, such as a username. Authentication: the system checks it, "
            "with a password, biometrics or MFA. Authorisation: the system decides what the user may do, using roles "
            "or access control lists. Accountability: actions are logged so they can be traced to the user.\n\n"
            "As a developer you build all four into your app's account system.",
            "In a school app: username (identification), password plus code (authentication), teachers can edit "
            "marks but students can't (authorisation), every change is logged (accountability).",
            [("Which stage checks a password?", "Authentication."),
             ("Which stage decides what a user can do?", "Authorisation."),
             ("How is accountability achieved?", "Audit logs.")]),
    },
    "core/20-employer-set-project.pptx": {
        "What is the ESP?": E(
            "The Employer Set Project is worth 40% of the core assessments (100 marks) and takes up to 14 hours 30 "
            "minutes across several sessions.\n\n"
            "It's set and marked externally and responds to a realistic vocational brief, drawing on everything in "
            "the core. You can't use the internet or AI tools during the assessed sessions, so the Python you need "
            "has to be in your head.\n\n"
            "The order and detail of the tasks can change each series, but the number and focus stay the same.",
            "The specimen brief was set in the financial sector: planning, fixing and building software for a "
            "fictional finance company.",
            [("What percentage of the core assessments is the ESP?", "40%."),
             ("Can you use the internet during the ESP?", "No."),
             ("Who marks the ESP?", "It's externally marked.")]),
        "What earns marks": E(
            "Each task rewards specific things.\n\n"
            "Task 2 (fix defects): a documented testing process covering each test, its purpose, the test data "
            "(valid, valid extreme, invalid, invalid extreme and erroneous), expected and actual results, and the "
            "fixes made.\n\n"
            "Task 3 (design): good decomposition, clear algorithms, correct flowchart symbols or code conventions, and "
            "a design detailed enough for a third party to build.\n\n"
            "Task 4a (develop): functions, meaningful names, comments, mostly local variables, constants, exception "
            "handling and a good user experience, including graphs with Matplotlib.",
            "Two programs that work equally well can score very differently: the one with functions, clear names, "
            "comments and error handling scores higher.",
            [("Name the five types of test data in Task 2.", "Valid, valid extreme, invalid, invalid extreme, erroneous."),
             ("What should a Task 3 design allow?", "A third party to build the solution."),
             ("Name three things markers look for in Task 4a code.", "E.g. functions, meaningful names, comments, exception handling.")]),
    },
}
