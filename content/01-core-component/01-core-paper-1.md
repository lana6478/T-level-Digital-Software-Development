# Core Paper 1: Problem Solving, Programming, Emerging Issues and Legislation

*Digital Software Development T Level → Core Component → Core Paper 1*

Core Paper 1 is a 2 hour 15 minute written exam worth 90 marks (30% of the core assessments). It covers four content areas: **Problem solving**, **Introduction to programming**, **Emerging issues**, and **Legislation and regulatory requirements**. Where the specification says "code", it means Python 3.10 or later. This page follows the specification's own numbering so you can cross-reference the official document.

## Content area 1: Problem solving

Students learn to solve digital software development problems, whole solutions or parts of them, expressing solutions as systems, processes, relationships, data organisation or code.

### 1.1 Computational thinking

What it is, when to use it, its benefits/drawbacks, and its four components, each with its own benefits and drawbacks to weigh:

- **Decomposition** - breaking a problem or solution into smaller, more manageable parts: identify the main features, characterise each one, then split it down. Represented using block diagrams, information flow diagrams, flowcharts, code, or written descriptions.
- **Pattern recognition** - finding trends and similarities within and between problems/processes, spotting common features between a new problem and existing solutions, and using patterns to make predictions.
- **Abstraction** - identifying what information is actually needed, filtering out unnecessary detail, and hiding internal workings: working out what inputs are needed, what outputs/outcomes are expected, what varies vs. stays constant, and what key/repeated actions the solution performs.
- Students should be able to judge how the four components relate to each other and how suitable each is for a given problem.

### 1.2 Algorithmic design

Algorithms and their purpose/characteristics; expressed as **flowcharts** (terminators, processes, sub-processes, decisions, inputs/outputs, arrows, labels), **written descriptions** (using hierarchical markers to show sequence), or **code** (see [Python and flowchart notation](../03-appendices/02-flowchart-and-python-notation.md)) - each with its own benefits and drawbacks. Actions that control the order of steps: **sequence**, **selection**, **iteration**. Students must be able to determine an algorithm's purpose and output, identify and correct errors in one, translate between notations, and design algorithms/solutions that use these actions.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Computational Thinking and Algorithms](../05-teaching-resources/slides/core/01-computational-thinking-and-algorithms.pptx) (PowerPoint, 19 slides)
<!-- lesson-slide:end -->

### 1.3 Strategies

Approaches to solving problems: **top-down**, **bottom-up**, **modularisation** (their purpose, when used, benefits/drawbacks). **Root cause analysis** approaches: five whys, failure mode and effects analysis (FMEA), event tree analysis (ETA), with follow-up actions (log, close, or escalate to a manager/specialist/third party). The high-level problem-solving strategy: define the problem, gather information, analyse the information, make a plan of action, implement a solution, review the solution. Students should be able to judge which strategy suits a given digital software development problem.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Problem-Solving Strategies](../05-teaching-resources/slides/core/02-problem-solving-strategies.pptx) (PowerPoint, 13 slides)
<!-- lesson-slide:end -->

## Content area 2: Introduction to programming

Students analyse problems involving software, people, processes and data, and use tools/techniques to build a complete solution or part of one.

### 2.1 Standard data types

Integer, float, string, Boolean - definitions, purpose, and when each is used.

### 2.2 Variables and constants

Definitions and purpose of variables and constants; purpose of data type conversion functions (see [Appendix 2](../03-appendices/02-flowchart-and-python-notation.md)); **scope** and how variables are managed by it (global vs. local). Students must be able to declare and use variables/constants of standard data types, use scope, and use conversion functions.

### 2.3 Data structures

**List**, **array**, **dictionary** - purpose and when each is used. Students must be able to interpret, develop and debug code that uses data structures.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Data Types, Variables and Data Structures](../05-teaching-resources/slides/core/03-data-types-variables-and-data-structures.pptx) (PowerPoint, 16 slides)
<!-- lesson-slide:end -->

### 2.4 Operators

**Arithmetic** (add, subtract, divide, multiply, exponentiation, integer division, modulus), **relational** (equivalence, less than, greater than, not equal, less/greater than or equal to), **Boolean** (not, and, or) - see [Appendix 2](../03-appendices/02-flowchart-and-python-notation.md) for the actual operators. Students must be able to use, interpret, create and debug code using operators.

### 2.5 Input and output

Implementing input/output via keyboard, screen, or text file, including the text-file cycle: open for reading, open for writing, write lines, close the file. Students must be able to interpret, create and debug code using input/output.

### 2.6 Actions

**Sequence**, **selection** (if / else if / else / match-case), and **loops** - count-controlled and condition-controlled, i.e. **iteration** via count-controlled `for` loops and condition-controlled `while` loops, with their benefits/drawbacks. Students must be able to interpret, develop and debug code using sequence, selection and iteration.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Operators, Input, Output and Program Flow](../05-teaching-resources/slides/core/04-operators-input-output-and-program-flow.pptx) (PowerPoint, 16 slides)
<!-- lesson-slide:end -->

### 2.7 Functions and procedures

**Functions** may or may not take parameters but must return a result; **procedures** may or may not take parameters but must not return a result. Both can be user-written, pre-written/built into the language, pre-written in language libraries, or pre-written in third-party libraries, each with benefits/drawbacks. Students must be able to interpret, develop and debug code using both.

### 2.8 Validation

Presence, length, range, type, format and check-digit checks - definition and purpose. Students must be able to interpret, develop and debug code using validation.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Functions, Procedures and Validation](../05-teaching-resources/slides/core/05-functions-procedures-and-validation.pptx) (PowerPoint, 15 slides)
<!-- lesson-slide:end -->

### 2.9 Design considerations and programming practices

Determining logical order of actions and operations (for accuracy and to avoid errors), choosing data structures and action order for efficient execution time/memory use, **naming conventions** (meaningful names, camelCase, snake_case) and their impact on readability alongside whitespace and line length. Students must judge an algorithm's suitability against requirements, efficiency, appropriateness of data structures/types/variables/constants, presentation and maintainability.

### 2.10 Robust code

Characteristics of robust code: handles unexpected inputs, handles unexpected terminations, produces specific/meaningful error messages. **Debugging** (locating and correcting errors) and its role in producing robust solutions. Students must be able to locate and correct errors in code.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Programming Practice and Robust Code](../05-teaching-resources/slides/core/06-programming-practice-and-robust-code.pptx) (PowerPoint, 15 slides)
<!-- lesson-slide:end -->

### 2.11 Common algorithms

**Searching**: linear search, binary search. **Sorting**: bubble sort, insertion sort, merge sort. Students need the benefits/drawbacks of each, metrics to compare algorithms (memory use, execution time, number of comparisons), and best/worst/average case reasoning (Big O not required), then must judge which searching/sorting algorithm suits a given situation.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Searching and Sorting Algorithms](../05-teaching-resources/slides/core/07-searching-and-sorting-algorithms.pptx) (PowerPoint, 15 slides)
<!-- lesson-slide:end -->

### 2.12 Testing

Why individual components (software, hardware, data, interfaces, the resulting service) are tested before final integration. **Testing methods**: concept, unit, boundary, integration, performance, system, acceptance, usability, regression, load/stress, closed box, open box - purpose, benefits, drawbacks, when used. **Automation**: macros, scripts, functional testing tools. **Test data types**: valid, invalid, boundary, erroneous. A **test plan**'s structure: identify tests, describe their purpose, identify test data, describe expected results, record actual results.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Testing](../05-teaching-resources/slides/core/08-testing.pptx) (PowerPoint, 15 slides)
<!-- lesson-slide:end -->

## Content area 3: Emerging issues

### 3.1 Impact of digital technologies

How increased reliance on digital systems affects **organisational culture** (communication method changes, productivity/availability expectations, staff monitoring, remote/hybrid working, automation including AI) and **society** (job loss, shifting skills, less human decision-making, privacy, changing behaviours, wider social/online access, potential isolation, improved information access, generative AI, globalisation/access to global media). **Digital inclusion**: fair access (suitable tech, connectivity, checking dataset bias, best-practice codes, public sector accessibility regulations). How **end-user characteristics** (age, digital/literacy skills, internal vs. external audience, cultural issues/bias, additional/accessibility needs) affect inclusivity. Benefits of professional development (competence, employability, standards knowledge).

### 3.2 Emerging technologies

Impact of developments in storage media, processing (quantum computing), the Internet of Things (edge computing; industrial/smart city/domestic use), AI (generative AI, machine learning), extended reality (AR/VR), open source software, blockchain, environmental factors (rare metals, energy to produce systems, disposal impact), and autonomous machines (self-driving cars, robotic assembly lines) - on organisations, individuals and society. Students must judge the interrelationships and impacts of these technologies in a digital software development context.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Emerging Issues and Technologies](../05-teaching-resources/slides/core/09-emerging-issues-and-technologies.pptx) (PowerPoint, 15 slides)
<!-- lesson-slide:end -->

## Content area 4: Legislation and regulatory requirements

### 4.1 Legislation

- **Health and safety**: the Health and Safety at Work Act (safe environment, trained staff, welfare, information/instruction/supervision) and display screen equipment rules (workstation assessments, breaks, eye tests, training) - plus the risks of digital work and how to mitigate them (training, safe environment/practices).
- **Data security and protection**: the Data Protection Act / UK GDPR, its purpose, and its eight principles.
- **Computer misuse**: the Computer Misuse Act (CMA) 1990's principles, consequences for company/employee, employee awareness, and the types of crime it covers.
- **Equality legislation**: the nine protected characteristics, types of discrimination (direct, indirect, harassment, victimisation), where individuals are protected, and time limits for claims.
- **Intellectual property**: unregistered designs, registered designs, patents.
- **International law**: that it applies to some offences, e.g. in cyberspace and surveillance.

Students must judge how digital software development interacts with this legislation and its impact on organisations, society and individuals.

### 4.2 Guidelines

- **Codes of conduct** sources: organisational, professional (British Computer Society, The Institution of Analysts and Programmers, Chartered Institute of Information Security), governmental - and how they shape professional behaviour (following policy/legislation, minimising public risk, competence/integrity, meeting deadlines, communication, confidentiality/trust).
- **Digital industry standards** sources: ISO, WCAG, W3C, IETF, British Standard (BS), IEEE, PCI SSC.
- **Acceptable use policies (AUP)**: purpose and typical content (permitted/prohibited activities, working practices, communication etiquette, sanctions).
- The importance of **whistleblowing** procedures.

Students must judge how guidelines interact with digital software development and their impact on organisations, society and individuals.

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Legislation and Guidelines](../05-teaching-resources/slides/core/10-legislation-and-guidelines.pptx) (PowerPoint, 15 slides)
<!-- lesson-slide:end -->

<!-- teaching-resources:start -->
## Teaching resources

Ready-made lesson slides for this topic. Each PowerPoint includes learning objectives, a starter, teaching slides, a quiz with answers, an activity and an exit ticket, with teacher notes on every slide. Download it and adapt it for your class.

| Lesson slides | Covers | Slides |
|---|---|---|
| [Computational Thinking and Algorithms (PowerPoint)](../05-teaching-resources/slides/core/01-computational-thinking-and-algorithms.pptx) | 1.1, 1.2 | 19 |
| [Problem-Solving Strategies (PowerPoint)](../05-teaching-resources/slides/core/02-problem-solving-strategies.pptx) | 1.3 | 13 |
| [Data Types, Variables and Data Structures (PowerPoint)](../05-teaching-resources/slides/core/03-data-types-variables-and-data-structures.pptx) | 2.1, 2.2, 2.3 | 16 |
| [Operators, Input, Output and Program Flow (PowerPoint)](../05-teaching-resources/slides/core/04-operators-input-output-and-program-flow.pptx) | 2.4, 2.5, 2.6 | 16 |
| [Functions, Procedures and Validation (PowerPoint)](../05-teaching-resources/slides/core/05-functions-procedures-and-validation.pptx) | 2.7, 2.8 | 15 |
| [Programming Practice and Robust Code (PowerPoint)](../05-teaching-resources/slides/core/06-programming-practice-and-robust-code.pptx) | 2.9, 2.10 | 15 |
| [Searching and Sorting Algorithms (PowerPoint)](../05-teaching-resources/slides/core/07-searching-and-sorting-algorithms.pptx) | 2.11 | 15 |
| [Testing (PowerPoint)](../05-teaching-resources/slides/core/08-testing.pptx) | 2.12 | 15 |
| [Emerging Issues and Technologies (PowerPoint)](../05-teaching-resources/slides/core/09-emerging-issues-and-technologies.pptx) | 3.1, 3.2 | 15 |
| [Legislation and Guidelines (PowerPoint)](../05-teaching-resources/slides/core/10-legislation-and-guidelines.pptx) | 4.1, 4.2 | 15 |

See [all lesson slides](../05-teaching-resources/01-lesson-slides.md) for every topic.
<!-- teaching-resources:end -->

## Key terms

- **Computational thinking** - the four-part approach (decomposition, pattern recognition, abstraction, algorithmic design) to breaking down and solving problems.
- **Scope** - the region of a program where a variable is accessible (global or local).
- **Robust code** - code that handles unexpected inputs/terminations gracefully and gives meaningful errors.
- **Threshold competence** - having enough knowledge/skill to be ready to build full occupational competence on the job.

## Related pages

- [Core Component overview](00-overview.md)
- [Core Paper 2](02-core-paper-2.md)
- [Employer Set Project](03-employer-set-project.md)
- [Core scheme of assessment](04-core-scheme-of-assessment.md)
- [Python and flowchart notation](../03-appendices/02-flowchart-and-python-notation.md)
- [Occupational Specialism overview](../02-occupational-specialism/00-overview.md)
