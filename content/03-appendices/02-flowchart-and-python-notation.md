# Flowchart Symbols and Python Command Reference

*Digital Software Development T Level → Appendices → Flowchart Symbols and Python Commands*

This appendix gives extra detail on two things students are expected to know throughout the Core and Occupational Specialism content: the flowchart notation used to express algorithms, and a reference list of Python commands and libraries. Students may explore Python in more depth than shown here if they choose it as one of their two implementation languages for the Occupational Specialism (see [Implementation](../02-occupational-specialism/06-implementation.md)). This page is a guide and reference, not a replacement for the specification itself.

## Python command reference

A working list of the Python built-ins, keywords and library functions students are expected to know, grouped by purpose.

### Input, output, type conversions

`input()` &middot; `print()` &middot; `int()` &middot; `str()` &middot; `float()` &middot; `bool()`

### Selection

`if` &middot; `elif` &middot; `else` &middot; `match case` &middot; `try except`

### Iteration

`while` &middot; `for`

### Functions

`def`

### Standard libraries

- `import`
- **math**: `math.floor()`, `math.ceil()`, `math.trunc()`, `math.sqrt()`, `math.pow()`, `math.pi`
- **random**: `random.random()`, `random.randint()`, `random.uniform()`, `random.sample()`

### Built-in functions

`range()` &middot; `round()` &middot; `max()` &middot; `min()` &middot; `count()` &middot; `chr()` &middot; `ord()` &middot; `len()`

### String handling

`isupper()` &middot; `islower()` &middot; `upper()` &middot; `lower()` &middot; `isalpha()` &middot; `split()` &middot; `len()` &middot; `find()` &middot; `index()` &middot; `isalnum()` &middot; `isdigit()` &middot; `replace()` &middot; `strip()` &middot; `format()` &middot; concatenation using `+`

### Data structures (lists, arrays, dictionaries)

`index()` &middot; `append()` &middot; `insert()` &middot; `remove()` &middot; `count()` &middot; `pop()` &middot; `sort()` &middot; `in` &middot; `not in` &middot; `len()`

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Data Types, Variables and Data Structures](../05-teaching-resources/slides/core/03-data-types-variables-and-data-structures.pptx) (PowerPoint, 16 slides)
<!-- lesson-slide:end -->

### Text files

`open()` &middot; `write()` &middot; `close()` &middot; `read()` &middot; `readline()` &middot; `readlines()` &middot; `line.strip()` &middot; `line.split()`

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Operators, Input, Output and Program Flow](../05-teaching-resources/slides/core/04-operators-input-output-and-program-flow.pptx) (PowerPoint, 16 slides)
<!-- lesson-slide:end -->

### Working with times and dates

`datetime.now()` &middot; `strftime()` &middot; `strptime()`

## Additional libraries (Employer Set Project)

For Employer Set Project questions, students also need a working knowledge of two data-focused libraries:

### pandas

Used to perform data analysis on a given `.csv` file. Students should be able to:

- import data from a provided `.csv` file;
- create and manipulate data frames using all or part of the imported data, as required;
- perform mathematical operations and statistical analysis on a data frame (or associated variable) - e.g. identifying trends/patterns over time, calculating a total or average from a range of data, or counting occurrences of a specific item of data.

### Matplotlib

Used alongside pandas to format and output data as part of analysing a `.csv` file. Students should be able to:

- select data and output it to appropriate graphs that meet a brief's requirements;
- format graph outputs so they're meaningful and easy to use (axis labels, colour schemes, legends, etc.).

## Flowchart symbols

Flowcharts are used throughout this qualification to express algorithms and processes. The standard symbols are:

| Symbol shape | Meaning |
|---|---|
| Rounded rectangle / terminator | Denotes the start and end of an algorithm. |
| Rectangle | Denotes a process to be carried out. |
| Rectangle with double-struck sides | Denotes a sub-process. |
| Diamond | Denotes a decision to be made. |
| Parallelogram | Denotes input or output. |
| Circle (connector) | Denotes a connection to part of a flowchart that can't easily be linked with an unbroken flow arrow. |
| Arrow | Shows the logical flow of the program. |

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Computational Thinking and Algorithms](../05-teaching-resources/slides/core/01-computational-thinking-and-algorithms.pptx) (PowerPoint, 19 slides)
<!-- lesson-slide:end -->

<!-- teaching-resources:start -->
## Teaching resources

Ready-made lesson slides for this topic. Each PowerPoint includes learning objectives, a starter, teaching slides, a quiz with answers, an activity and an exit ticket, with teacher notes on every slide. Download it and adapt it for your class.

| Lesson slides | Covers | Slides |
|---|---|---|
| [Computational Thinking and Algorithms (PowerPoint)](../05-teaching-resources/slides/core/01-computational-thinking-and-algorithms.pptx) | 1.1, 1.2 | 19 |
| [Data Types, Variables and Data Structures (PowerPoint)](../05-teaching-resources/slides/core/03-data-types-variables-and-data-structures.pptx) | 2.1, 2.2, 2.3 | 16 |
| [Operators, Input, Output and Program Flow (PowerPoint)](../05-teaching-resources/slides/core/04-operators-input-output-and-program-flow.pptx) | 2.4, 2.5, 2.6 | 16 |

See [all lesson slides](../05-teaching-resources/01-lesson-slides.md) for every topic.
<!-- teaching-resources:end -->

## Key terms

- **Data frame** - a pandas structure for holding and manipulating tabular data imported from a file such as a `.csv`.
- **Connector (flowchart)** - a symbol used to link two points on a flowchart when a direct arrow would be impractical (e.g. across a page break).

## Related pages

- [Competency frameworks and command words](01-competency-frameworks.md)
- [Core Paper 1](../01-core-component/01-core-paper-1.md)
- [Implementation](../02-occupational-specialism/06-implementation.md)
