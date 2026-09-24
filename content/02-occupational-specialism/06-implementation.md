# Implement a Solution Using at Least Two Appropriate Languages

*Digital Software Development T Level → Occupational Specialism → Implementation*

This is Content Area 6, the core coding content area of the specialism. It covers choosing and using programming languages to build front-end and back-end solutions, building a working user interface, connecting code to data, and deploying the finished product. Students must select and use **at least two** languages for their software project.

## 6.1 Selecting and using languages appropriate to the project

Students choose at least two appropriate languages from this list to build front-end and back-end solutions:

- Python 3 (version 3.10 or later)
- C#
- SQL
- JavaScript
- PHP

**Tools, APIs, packages, modules and libraries.** Students need to be able to select and use these to add functionality and compatibility, covering things like:

- generating dynamic page content
- containerisation
- stateful vs. stateless components
- form handling
- file and data handling (local files; create/open/read/write/delete/close files on a server; sending/receiving cookies; adding, deleting and modifying data in a database)
- interface components and media content
- adaptive/responsive layout
- working with existing applications, operating systems, cloud-based and traditional platforms
- working with specific devices
- communication over a network
- infrastructure as code
- security features (controlling user access, encrypting data)

**Packaging the product.** Students should be able to package and organise front-end and back-end code into a single usable product - for example using HTML, CSS and related frameworks to deploy a solution, then compiling/encapsulating it as a single executable file.

**Continuous integration.** Students need to understand what continuous integration - continuous deployment (CI/CD) means, and the common stages of a CI/CD pipeline:

- source code control
- build automation
- unit test automation
- deployment automation
- monitoring

**Coding conventions.** Students should use common coding conventions: naming conventions, code annotations/commenting, modularisation, structure/indentation, and version control.

**Good practice (the 12-factor principles).** Students should apply good practice when developing digital products, based on the "12 factor app" principles:

1. Use one codebase tracked in revision control, with many deploys.
2. Explicitly declare and isolate dependencies.
3. Store configuration in the environment.
4. Treat backing services as attached resources.
5. Strictly separate build and run stages.
6. Execute the app as one or more stateless processes.
7. Export services via port binding.
8. Scale out via the process model.
9. Maximise robustness with fast startup and graceful shutdown.
10. Keep development, staging and production as similar as possible.
11. Treat logs as event streams.
12. Run admin/management tasks as one-off processes.

*(Signposted competencies: E5, M1-M8, M10, D1-D4, D6.)*

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Languages, CI/CD and Good Practice](../05-teaching-resources/slides/specialism/11-languages-ci-cd-and-good-practice.pptx) (PowerPoint, 10 slides)
<!-- lesson-slide:end -->

## 6.2 Selecting tools and features for a UX-driven user interface

**User interface features.** Students select and use appropriate features such as images and animation, audio, visual effects, and interactions (user input; output/feedback that can be textual, graphical, audio or haptic), plus data visualisation like dashboards, graphing and data presentation.

**User interface techniques.** This covers layout grids, use of space, font selection and typesetting, letter spacing, line spacing, justification, use of colour and contrast, input focus, and hover controls.

**Design decisions.** Students must weigh up: browser support, target device/platform, user characteristics, available bandwidth, style and branding, accessibility, and the user's input method (voice, text, touch screen, or mouse).

*(Signposted competencies: E5, M1, M4, M7, M8, M10, D1, D2, D6.)*

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [UX and UI Design](../05-teaching-resources/slides/specialism/09-ux-and-ui-design.pptx) (PowerPoint, 9 slides)
<!-- lesson-slide:end -->

## 6.3 Connecting code to data sources

Students create data sources to support their software (using a database) and connect to them through different methods:

- **API (Application Programming Interface)** - types of requests and request methods, endpoints, retrieving/parsing/displaying data, and API keys.
- **JDBC (Java Database Connectivity)** - the core API, driver manager, connection statement, prepared statement, result set, and SQL queries.
- **ODBC (Open Database Connectivity)** - the application, driver manager, driver, data source, and connection method (database name/data source, credentials, optional parameters).

Once connected, students should be able to extract, store, update and delete data, and connect to network resources using tools within their development environment. Students must be able to select the data source and connection method that's actually appropriate to the context and market they're developing for, not just default to one approach.

*(Signposted competencies: E5, M4, M5, M6, M10, D1, D3, D4, D5, D6.)*

## 6.4 Selecting deployment methods

Students select and use deployment methods appropriate to the project, such as:

- local installation
- network/server installation
- mobile platforms
- web-based platforms
- cloud-based platforms
- containerisation
- container-scheduling platforms

*(Signposted competencies: E5, M5, M6, M10, D1, D4, D6.)*

<!-- lesson-slide:start -->
> **Lesson slides for this section:** [Connecting to Data and Deploying Software](../05-teaching-resources/slides/specialism/12-data-connections-and-deployment.pptx) (PowerPoint, 9 slides)
<!-- lesson-slide:end -->

<!-- teaching-resources:start -->
## Teaching resources

Ready-made lesson slides for this topic. Each PowerPoint includes learning objectives, a starter, teaching slides, a quiz with answers, an activity and an exit ticket, with teacher notes on every slide. Download it and adapt it for your class.

| Lesson slides | Covers | Slides |
|---|---|---|
| [UX and UI Design (PowerPoint)](../05-teaching-resources/slides/specialism/09-ux-and-ui-design.pptx) | 4.3 (UX and UI), 6.2 | 9 |
| [Languages, CI/CD and Good Practice (PowerPoint)](../05-teaching-resources/slides/specialism/11-languages-ci-cd-and-good-practice.pptx) | 6.1 | 10 |
| [Connecting to Data and Deploying Software (PowerPoint)](../05-teaching-resources/slides/specialism/12-data-connections-and-deployment.pptx) | 6.3, 6.4 | 9 |

See [all lesson slides](../05-teaching-resources/01-lesson-slides.md) for every topic.
<!-- teaching-resources:end -->

## Key terms

- **CI/CD** - continuous integration / continuous deployment; automating the build, test and release of software.
- **12-factor app** - a widely-used set of principles for building software-as-a-service apps that are portable and scalable.
- **API** - Application Programming Interface, a defined way for one piece of software to request data/functionality from another.
- **JDBC / ODBC** - standard interfaces for connecting an application to a database (JDBC for Java, ODBC as a more general cross-platform standard).
- **Containerisation** - packaging an application with everything it needs to run into an isolated, portable unit (e.g. Docker).

## Related pages

- [Occupational Specialism overview](00-overview.md)
- [Analyse a Problem](01-analyse-a-problem.md)
- [Ethics and Risk](02-ethics-and-risk.md)
- [Sources of Knowledge](03-sources-of-knowledge.md)
- [Design](04-design.md)
- [Social and Collaborative Environment](05-social-and-collaborative-environment.md)
- [Testing](07-testing.md)
- [Change, Maintain and Support](08-change-maintain-support.md)
- [Scheme of Assessment](09-scheme-of-assessment.md)
