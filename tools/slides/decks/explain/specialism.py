"""Explanations for the occupational specialism decks."""
from . import E

EXPLAIN = {
    "specialism/01-sdlc-and-requirements.pptx": {
        "The SDLC": E(
            "The software development lifecycle (SDLC) is the set of stages a project moves through.\n\n"
            "Research and familiarisation: understand the brief, the market, existing solutions and your own skills "
            "gaps. Planning and requirement analysis: define the scope, requirements, KPIs, schedule, costs, language "
            "and risks. User analysis: understand users with user stories, activity diagrams and ERDs. Design: "
            "interfaces, algorithms and data, checking any AI-generated code carefully. Develop and test: build a "
            "prototype and test it. Deploy: install, configure, document and version-control it. Maintain: support "
            "users, fix bugs and release updates.",
            "A bakery ordering app: research competitors, plan features and costs, write user stories, design "
            "screens, build and test, launch on app stores, then fix bugs and add features.",
            [("Name the stage where user stories are written.", "User analysis."),
             ("Why review AI-generated code?", "To make sure it really meets the requirements."),
             ("What happens during maintenance?", "Support, bug fixes, training and updates.")]),
        "Functional and non-functional requirements": E(
            "Functional requirements say what the system does: the inputs it takes, the data it needs, the "
            "processing it performs, its logic and the platforms it runs on.\n\n"
            "Non-functional requirements say how well it does it: security, accessibility, scalability, and measurable "
            "KPIs for responsiveness, load and reliability, plus user acceptance criteria.\n\n"
            "Secure by design means security shapes both from the start. Spike testing is a short experiment early "
            "on to explore a problem and work out the scope of the solution.",
            "Functional: 'the user can add items to a basket'. Non-functional: 'the basket page loads in under 2 "
            "seconds for 500 simultaneous users'.",
            [("Is 'the app must work with a screen reader' functional or non-functional?", "Non-functional."),
             ("What is secure by design?", "Building security in from the start."),
             ("What is spike testing?", "An early experiment to explore a problem and its scope.")]),
        "User analysis tools": E(
            "User analysis makes sure you build what users actually need.\n\n"
            "User stories describe a need from the user's view: 'As a [user], I want [goal], so that [reason]'.\n\n"
            "Activity and process diagrams show the steps a user or system goes through. Mind maps explore ideas. "
            "Product road maps plan which features arrive in which release. Entity relationship diagrams (ERDs) show "
            "the data the system stores and how it links.",
            "'As a busy parent, I want to reorder my usual items in one tap, so that ordering takes seconds.'",
            [("What is the format of a user story?", "As a [user], I want [goal], so that [reason]."),
             ("What does an ERD show?", "The data stored and how it links."),
             ("What is a product road map?", "A plan of which features arrive in which release.")]),
    },
    "specialism/02-team-roles-and-project-methodologies.pptx": {
        "Roles in the digital team": E(
            "Software is built by teams with distinct roles.\n\n"
            "The product owner or client sets the requirements. The scrum master keeps the team working well and "
            "removes obstacles. The technical lead gives technical guidance. The project manager handles budget, "
            "scope, schedule, risk and quality.\n\n"
            "In the development team, the systems analyst writes requirements, the UX/UI designer researches users "
            "and designs the interface, developers build it, operations engineers keep it stable and security "
            "engineers keep it secure. Testers assure quality throughout.",
            "A bug in production: the tester finds it, the developer fixes it, the operations engineer deploys the "
            "fix, and the product owner decides how urgent it is.",
            [("Who sets the product's requirements?", "The product owner or client."),
             ("What does a scrum master do?", "Keeps the team cohesive and removes obstacles."),
             ("What does a UX/UI designer do?", "Researches users and designs the interface.")]),
        "Agile and Waterfall": E(
            "Agile delivers software in small increments: sprints, epics (large features), stories and spikes "
            "(research tasks). Users see working software every iteration, requirements can change, and even a "
            "cancelled project leaves usable code. Documentation is lighter. Scaled Agile extends this to large teams.\n\n"
            "Waterfall moves through fixed stages in order. Progress is measured by completed documents, costs are "
            "high up front and returns slow, users see little until the end, and a project cancelled early may leave "
            "nothing usable. It suits projects with fixed, well-understood requirements.",
            "A start-up app with uncertain needs suits Agile; a safety-critical system with fixed regulations may suit Waterfall.",
            [("What is an epic in Agile?", "A large feature made up of many stories."),
             ("Why might a cancelled Waterfall project leave nothing usable?", "Working software only arrives at the end."),
             ("When does Waterfall suit a project?", "When requirements are fixed and well understood.")]),
        "Other methodologies": E(
            "Rapid Application Development (RAD) builds prototypes quickly and improves them systematically. It "
            "values features over polish, reuses a lot of existing code and suits small to medium projects.\n\n"
            "Lean cuts waste such as unneeded features, repeated tasks and poor communication, delays decisions to "
            "the last responsible moment, and delivers in short cycles. It suits small teams with limited resources.\n\n"
            "User Centred Design (UCD) keeps users at the centre. It's empathetic, iterative and interdisciplinary: "
            "understand the context, specify requirements, design, then assess against requirements, and repeat.",
            "A charity building an accessible website for older users would use UCD: testing each design with real "
            "older users before moving on.",
            [("Which methodology relies heavily on reusing code?", "RAD."),
             ("What does Lean aim to cut?", "Waste."),
             ("What are the characteristics of UCD?", "Empathetic, iterative, interdisciplinary.")]),
    },
    "specialism/03-emerging-technologies-and-skills.pptx": {
        "Emerging technologies": E(
            "Developers increasingly build for new technologies.\n\n"
            "AI and virtual intelligence include conversational and generative AI, machine learning, object "
            "recognition and computer vision. Operational technology (OT) and the Internet of Things (IoT) connect "
            "physical equipment to software. Biometrics identify people by fingerprints or faces. Robotics and "
            "automation replace manual tasks. Cloud platforms, data lakes and data warehouses store and process data "
            "at scale. Drones and 3D printing are controlled by software, and 5G networks make fast mobile "
            "connections widespread.",
            "A warehouse app uses computer vision to read labels, IoT sensors to track stock, and cloud services to "
            "store the data.",
            [("What is computer vision?", "AI that interprets images and video."),
             ("What is operational technology?", "Systems that monitor and control physical equipment."),
             ("How does 5G affect app design?", "Faster mobile connections allow richer real-time features.")]),
        "Identifying and addressing training needs": E(
            "No developer knows everything, so a key skill is spotting what you don't know.\n\n"
            "First identify what knowledge and skills a project needs. Then judge honestly whether you can currently "
            "do the work. If there's a gap, close it through coaching from a professional or peer, learning on the "
            "job, self-study, professional online forums, or online workshops.\n\n"
            "Keeping your skills current is essential because languages, frameworks and tools change constantly.",
            "A developer asked to add payments to an app has never used a payment API. They work through the "
            "provider's tutorial, ask a colleague to review their code, then build it.",
            [("What should you do before starting a project?", "Identify the skills needed and check you have them."),
             ("Give three ways to close a skills gap.", "Any three: coaching, on-the-job learning, self-study, forums, workshops."),
             ("Why must developers keep learning?", "Technologies change constantly.")]),
    },
    "specialism/04-legal-and-ethical-development.pptx": {
        "Legal and regulatory considerations": E(
            "Software must follow the law in the context and market it's built for.\n\n"
            "Consider intellectual property rights and licences, copyright and patents; consumer protection and "
            "advertising law; age ratings and gambling legislation; data protection and privacy; staff and "
            "employment responsibilities; territorial restrictions on where software can be sold; system security; "
            "and equality and diversity.\n\n"
            "Different products trigger different rules: a children's game raises age and gambling issues, a health "
            "app raises data protection issues.",
            "Loot boxes in a children's game may fall under gambling law and consumer protection, and collecting "
            "children's data brings strict privacy rules.",
            [("Which laws might apply to loot boxes?", "Gambling legislation and consumer protection."),
             ("Why do territorial restrictions matter?", "Laws differ between countries."),
             ("Name two legal areas for a health app.", "E.g. data protection, privacy, security.")]),
        "Standards and ethics": E(
            "Standards guide how software is built. ISO/IEC/IEEE 90003:2018 gives guidance on applying quality "
            "management to software engineering. W3C sets web standards, so sites work across browsers and devices.\n\n"
            "Ethics goes beyond the law: following a professional code of conduct, working professionally, respecting "
            "software licences (for example open-source licence terms) and designing for inclusion and diversity.\n\n"
            "Something can be legal but still unethical, such as a design that tricks users into subscriptions.",
            "Using an open-source library means following its licence, which may require crediting the authors or "
            "sharing your changes.",
            [("What does W3C set standards for?", "The web."),
             ("Give an example of something legal but unethical.", "E.g. tricking users into subscriptions."),
             ("Why follow software licences?", "They set legal terms for using others' code.")]),
    },
    "specialism/05-identifying-and-managing-risk.pptx": {
        "Risks to identify": E(
            "Software projects face many kinds of risk.\n\n"
            "Security: data or systems damaged maliciously or by accident. Compatibility with other systems. Delivery: "
            "development taking too long, or failing to meet requirements and KPIs. Legal and ethical problems. "
            "Users: poor engagement or limited reach.\n\n"
            "Each risk is assessed by weighing its likelihood against its seriousness and potential impact.",
            "A food delivery app risks: a data breach (security), failing on older phones (compatibility), missing "
            "launch day (delivery), and users not returning (engagement).",
            [("Name three types of project risk.", "E.g. security, compatibility, delivery, legal, engagement."),
             ("How is a risk assessed?", "Likelihood weighed against seriousness and impact."),
             ("Give an example of a compatibility risk.", "E.g. failing on older devices or other systems.")]),
        "Managing risk": E(
            "Risk management is a cycle.\n\n"
            "Identify the risks for your specific context and market. Assess each for likelihood and seriousness. "
            "Mitigate: reduce the likelihood or impact. Plan contingencies: what you'll do if the risk happens. "
            "Monitor: keep checking, because risks change.\n\n"
            "Organisations support this with policies for backup, security, the CIA triad, staff skills and "
            "training, business continuity and disaster recovery. Good decisions weigh risk against reward.",
            "Risk: the payment provider goes down. Mitigation: use a reliable provider. Contingency: a second "
            "provider ready to switch to. Monitoring: uptime alerts.",
            [("What is a contingency plan?", "What you'll do if a risk happens."),
             ("Why keep monitoring risks?", "Risks change over time."),
             ("Name two organisational policies that reduce risk.", "E.g. backup, security, business continuity.")]),
    },
    "specialism/06-sources-of-knowledge-and-evaluation.pptx": {
        "Is the source reliable?": E(
            "Developers constantly look things up: search engines, wikis, blogs, academic papers, peers, forums, "
            "code comments and code repositories.\n\n"
            "Judge each source on reputation (is the author credible?), bias (do they have an angle?), evidence "
            "(what backs it up?), cross-referencing or triangulation (do other independent sources agree?) and "
            "currency (when was it last updated, and does it match your language version?).",
            "A 2014 forum answer using Python 2 syntax may not work in Python 3.10. The official documentation is "
            "more current and authoritative.",
            [("What is currency?", "How up to date a source is."),
             ("What is triangulation?", "Checking against several independent sources."),
             ("Why prefer official documentation?", "It's authoritative and current.")]),
        "Gathering data to evaluate a solution": E(
            "To know whether software works for users, gather evidence.\n\n"
            "Qualitative techniques capture opinions and experiences: verbal feedback, user observation with records, "
            "focus groups representing the target audience, interviews, peer mentoring and appraisals.\n\n"
            "Quantitative techniques capture numbers: surveys and questionnaires, performance data and usage data "
            "such as analytics.\n\n"
            "Combining both shows what is happening and why.",
            "Analytics show 60% of users abandon sign-up at step 3 (quantitative); interviews reveal the password "
            "rules are confusing (qualitative).",
            [("Give one qualitative technique.", "E.g. interviews, observation, focus groups."),
             ("Give one quantitative technique.", "E.g. surveys, usage data, performance data."),
             ("Why combine both?", "To see what's happening and why.")]),
    },
    "specialism/07-design-approaches.pptx": {
        "Design approaches (1)": E(
            "Function-oriented (top-down) design breaks a system into functions, using data flow diagrams to show "
            "how each changes the data: divide and conquer.\n\n"
            "Object-oriented design builds programs from classes and objects. Encapsulation keeps an object's data "
            "private; abstraction hides complexity; inheritance lets classes reuse a parent's code; polymorphism lets "
            "different objects respond to the same method in their own way. Design patterns (creational, structural, "
            "behavioural) are proven solutions.\n\n"
            "Data model design plans the data using conceptual, logical and physical models, E-R models and UML.",
            "A game has a Character class. Wizard and Knight inherit from it; both have an attack() method but it "
            "works differently for each (polymorphism).",
            [("What is inheritance?", "A class reusing a parent class's code."),
             ("What is encapsulation?", "Keeping an object's data private inside it."),
             ("Which tools support data model design?", "E-R models and UML.")]),
        "Test-driven development (TDD)": E(
            "In test-driven development, tests are written before the code.\n\n"
            "Add a test describing what a new feature should do. Run all the tests: the new one fails, because the "
            "feature doesn't exist yet. Write just enough code to make it pass. Run the tests again and refactor "
            "(tidy the code) while keeping them passing. Repeat for the next feature.\n\n"
            "This keeps code focused on requirements, catches regressions immediately, and leaves a full set of "
            "automated tests behind.",
            "Test: grade(85) should return 'A'. It fails. Write the grade function. It passes. Add the next test: "
            "grade(40) returns 'U'.",
            [("In TDD, what is written first?", "The test."),
             ("Why should a new test fail at first?", "The feature doesn't exist yet."),
             ("What is refactoring?", "Tidying code without changing what it does.")]),
        "BDD and functional design": E(
            "Behaviour-driven development (BDD) describes the required behaviour before coding. Each behaviour must "
            "have business value and map to a requirement, and is written with a title, a narrative and acceptance "
            "criteria, often as 'Given... When... Then...'.\n\n"
            "Functional design structures a program as modules that each perform one function. It uses features such "
            "as recursion (a function calling itself), closures, first-class and higher-order functions (functions "
            "passed as values), anonymous functions (lambdas) and currying.",
            "BDD: Given a user has items in their basket, When they click Checkout, Then they see the payment page.",
            [("What format do BDD scenarios often use?", "Given... When... Then..."),
             ("What is recursion?", "A function that calls itself."),
             ("What is a higher-order function?", "A function that takes or returns another function.")]),
    },
    "specialism/08-platforms-version-control-and-collaboration.pptx": {
        "Workflow management": E(
            "Version control tools such as Git let teams work on the same code using branches.\n\n"
            "GitFlow uses long-lived main and develop branches, plus feature, release and hotfix branches. It suits "
            "software released on a schedule.\n\n"
            "GitHubFlow keeps one main branch that's always ready to deploy. Developers create short feature branches "
            "and merge them through pull requests after review. It suits teams that deploy continuously.\n\n"
            "Development platforms may be proprietary or open source; choose by audience, budget, features, skills, "
            "speed, security, reliability, performance and compatibility.",
            "With GitHubFlow, a developer branches, fixes a bug, opens a pull request, a teammate reviews it, it's "
            "merged into main and deployed the same day.",
            [("What is a branch?", "A separate line of development."),
             ("Which workflow keeps main always deployable?", "GitHubFlow."),
             ("What is a pull request?", "A request to merge changes after review.")]),
        "Why collaborate?": E(
            "Teams build software faster and better than individuals working alone.\n\n"
            "Work happens in parallel, which cuts development time. Communication improves, knowledge is shared and "
            "everyone's skills grow.\n\n"
            "Code reviews catch bugs and share good practice. They include paired programming (two developers at "
            "one computer), informal walkthroughs and formal inspections.\n\n"
            "Collaboration isn't always best, though: some focused tasks are quicker done alone.",
            "In pair programming, one developer types (the driver) while the other reviews each line and thinks "
            "ahead (the navigator), then they swap.",
            [("Name three types of code review.", "Paired programming, informal walkthroughs, formal inspections."),
             ("Give two benefits of collaborating.", "E.g. faster development, shared knowledge, better communication."),
             ("When might working alone be better?", "For small, focused tasks.")]),
        "Collaborative technologies": E(
            "Teams rely on technology to work together.\n\n"
            "Communication: email and instant messaging. Resource management: cloud storage, backup and "
            "synchronisation. Knowledge sharing: collaboration hubs, wikis, forums and news sites. Documentation for "
            "technical and non-technical readers.\n\n"
            "Development-specific tools: code collaboration platforms, version control (tracking every change to "
            "files), source control (managing the source code itself) and IDEs, some of which support live shared editing.",
            "A team uses a chat app for quick questions, a wiki for setup guides, Git for code, and a shared IDE "
            "session to debug together.",
            [("What is the difference between version control and source control?", "Version control tracks changes to any files; source control manages source code specifically."),
             ("Give an example of a knowledge-sharing tool.", "E.g. a wiki."),
             ("Why document for non-technical readers too?", "Clients and users also need to understand the software.")]),
    },
    "specialism/09-ux-and-ui-design.pptx": {
        "UX design principles": E(
            "User experience (UX) design is about how using the product feels.\n\n"
            "Consistency: the product looks and behaves the same throughout and fits the brand. Information "
            "hierarchy: content is organised so it's easy to navigate. Visual hierarchy: the most important things "
            "stand out. Confirmation: users know what their action did. User control: users can navigate efficiently "
            "and fix mistakes, such as with undo. Accessibility: it works for as many people as possible.\n\n"
            "UI design uses wireframes (layout sketches), style guides (colours, fonts, components) and clickable prototypes.",
            "After tapping 'Send', a message showing 'Payment sent to Sam' (confirmation) with an 'Undo' option "
            "(user control) builds trust.",
            [("Which principle means users know what their action did?", "Confirmation."),
             ("What is a wireframe?", "A simple layout sketch of a screen."),
             ("Give an example of user control.", "E.g. an undo button.")]),
        "UI features and techniques": E(
            "User interface features include images and animation, audio, visual effects, and interactions: user "
            "input and feedback that can be text, graphics, sound or haptic (vibration). Data can be shown with "
            "dashboards and graphs.\n\n"
            "Techniques include layout grids, use of space, font choice, letter and line spacing, justification, "
            "colour and contrast, input focus (showing which field is active) and hover controls.\n\n"
            "Design decisions depend on browser support, target devices, users' characteristics, bandwidth, "
            "branding, accessibility and how users give input: voice, text, touch or mouse.",
            "Buttons for a touch screen need to be large enough for a finger. Hover effects don't work on touch "
            "devices, so they can't be the only clue.",
            [("What is haptic feedback?", "Feedback through vibration."),
             ("Why does colour contrast matter?", "Low contrast is hard to read, especially for visually impaired users."),
             ("Why design touch targets larger?", "Fingers are less precise than a mouse pointer.")]),
    },
    "specialism/10-designing-data-assets-and-integration.pptx": {
        "Assets and AI": E(
            "Assets are the graphics, audio, video and code a solution uses.\n\n"
            "When selecting them, consider the file type, file size and compression, how audio and video are "
            "streamed or encoded, metadata, the quality needed, the available bandwidth and storage, and the target "
            "platform. A 20 MB image might look great but will crawl on a mobile connection.\n\n"
            "When using AI to generate content or assets, work legally and ethically: check licences and ownership, "
            "don't pass off others' work, and review the output.",
            "Swapping a 4 MB PNG hero image for a 300 KB compressed WebP makes a mobile page load in 1 second instead of 6.",
            [("Name three factors when selecting an image asset.", "E.g. file type, size, compression, quality, bandwidth."),
             ("Why does asset size matter on mobile?", "Large files load slowly on limited bandwidth."),
             ("What should you check when using AI-generated assets?", "Licences, ownership and quality.")]),
        "Designing a database": E(
            "Databases support user management, e-commerce (stock, orders, personalisation), diagnostics and "
            "performance analysis.\n\n"
            "Design starts with a data dictionary listing every field, its data type, size and validation rules. An "
            "entity relationship diagram (ERD) shows the entities (such as Customer, Order, Product) and the "
            "relationships between them.\n\n"
            "Normalisation to third normal form removes duplicated data by splitting it into linked tables using "
            "primary and foreign keys, so each fact is stored once.",
            "Instead of storing a customer's address on every order, store it once in Customer and link each Order "
            "with a CustomerID foreign key.",
            [("What is a data dictionary?", "A list of every field with its type and rules."),
             ("What does normalisation remove?", "Duplicated data."),
             ("What is a foreign key?", "A field linking to the primary key of another table.")]),
        "Platforms and integration": E(
            "Target platforms shape design: the operating system, file system, physical or virtual servers, the "
            "language stack, and whether it's a mobile or web app.\n\n"
            "Network integration asks which data is processed locally (such as a player's input in a game) and which "
            "remotely (such as all players' positions in a multiplayer game), how data moves between them (such as "
            "remote system calls), how the systems connect, where the system's boundaries are, and which external "
            "systems to integrate with.",
            "A fantasy football app processes team selection on the phone, stores teams on its server, and pulls "
            "live scores from an external sports-data feed.",
            [("What is processed locally in a multiplayer game?", "E.g. the player's own input."),
             ("What is a system boundary?", "Where your system ends and external systems begin."),
             ("Give an example of an external system to integrate with.", "E.g. a sports-data feed or payment provider.")]),
    },
    "specialism/11-languages-ci-cd-and-good-practice.pptx": {
        "Languages in the specification": E(
            "You must use at least two languages, for front-end and back-end work.\n\n"
            "Python 3.10+ suits back-end logic, data processing and scripting. C# builds desktop apps, games and "
            "services. SQL queries and changes databases. JavaScript makes web pages interactive, and can run "
            "back ends too. PHP builds server-side web pages.\n\n"
            "Tools, APIs, packages and libraries add functionality: dynamic content, form handling, files, cookies, "
            "responsive layouts, networking, containerisation, infrastructure as code and security features such as "
            "access control and encryption.",
            "A booking site: JavaScript for the interactive calendar (front end), Python for the booking logic (back "
            "end), SQL for the database.",
            [("Which language queries databases?", "SQL."),
             ("How many languages must your project use?", "At least two."),
             ("What does JavaScript usually do on a website?", "Makes pages interactive (front end).")]),
        "CI/CD pipeline": E(
            "Continuous integration and continuous deployment (CI/CD) automates the path from code to users.\n\n"
            "Source code control: all code lives in a repository. Build automation: every change is built "
            "automatically. Unit test automation: tests run on every change, so bugs are caught immediately. "
            "Deployment automation: code that passes is released automatically. Monitoring: the live system is "
            "watched for problems.\n\n"
            "The result is small, frequent, reliable releases instead of big, risky ones.",
            "A developer pushes a fix. Within ten minutes it's built, 200 tests pass, and it's live, with no manual steps.",
            [("Name the five CI/CD stages.", "Source control, build, unit test, deploy, monitor."),
             ("Why run tests automatically on every change?", "To catch bugs immediately."),
             ("Why are small frequent releases safer?", "Each change is small and easy to fix or roll back.")]),
        "The 12-factor app (highlights)": E(
            "The 12-factor app is a set of good practices for building apps that deploy and scale reliably.\n\n"
            "Keep one codebase in version control. Declare and isolate dependencies. Store configuration, such as "
            "passwords and URLs, in the environment, not the code. Treat databases and other backing services as "
            "attachable resources. Keep build, release and run separate. Run the app as stateless processes, export "
            "services by port binding and scale by adding processes. Start fast and shut down gracefully. Keep "
            "development and production alike. Treat logs as event streams, and run admin tasks as one-off processes.",
            "Storing the database password in an environment variable, not the code, means it never ends up in the "
            "repository and can differ between test and live.",
            [("Where should configuration be stored?", "In the environment."),
             ("Why keep development and production alike?", "So code behaves the same in both."),
             ("What is a stateless process?", "One that keeps no data between requests.")]),
    },
    "specialism/12-data-connections-and-deployment.pptx": {
        "Connecting to data": E(
            "Software connects to data sources in several ways.\n\n"
            "An API is accessed with requests (GET to read, POST to create and so on) to endpoints (specific URLs). "
            "The response, usually JSON, is parsed and displayed. API keys identify and authorise your app.\n\n"
            "JDBC connects Java programs to databases using a driver manager, a connection, statements or prepared "
            "statements, SQL queries and result sets.\n\n"
            "ODBC is a standard any application can use: the app talks to a driver manager and driver, which connect "
            "to a data source using its name and credentials.",
            "A weather app sends a GET request to the forecast endpoint with its API key. The JSON reply is parsed "
            "into a Python dictionary and today's temperature is displayed.",
            [("What is an API endpoint?", "A specific URL where requests are sent."),
             ("What does a prepared statement protect against?", "SQL injection."),
             ("What format do most APIs return?", "JSON.")]),
        "Deployment methods": E(
            "Deployment gets software to users.\n\n"
            "Local installation puts it on one machine. Network or server installation deploys it across an "
            "organisation. Mobile platforms distribute through app stores. Web and cloud platforms make it available "
            "in a browser with easy updates.\n\n"
            "Containerisation packages the app with everything it needs, so it runs identically anywhere. "
            "Container-scheduling platforms run and scale many containers automatically.\n\n"
            "Choose based on the users, the platform and how often it will be updated.",
            "A web app deployed in containers on a cloud platform can scale from 10 to 10,000 users by adding "
            "containers automatically.",
            [("Why use containers?", "The app runs identically anywhere and scales easily."),
             ("How are mobile apps usually distributed?", "Through app stores."),
             ("Give one advantage of web deployment.", "Easy updates and access from any browser.")]),
    },
    "specialism/13-testing-a-software-solution.pptx": {
        "Types of testing": E(
            "Different tests check different things.\n\n"
            "Functional testing checks the software does what it should: unit (one piece), smoke (a quick check that "
            "the main features work), integration (pieces together) and system (the whole).\n\n"
            "Non-functional testing checks how well: availability, compatibility, configuration and load.\n\n"
            "Front-end testing checks performance, browser and OS compatibility, rendering, loading times and "
            "responsiveness.\n\n"
            "Security testing uses vulnerability scanning, static analysis (examining code without running it), "
            "dynamic analysis (testing it running) and integration analysis.",
            "Before release: smoke test the main features, run the site in Chrome, Firefox and Safari, load test 1,000 "
            "users, and run a vulnerability scan.",
            [("What is a smoke test?", "A quick check that the main features work."),
             ("What is static analysis?", "Checking code for problems without running it."),
             ("Give one front-end test.", "E.g. browser compatibility, loading time, responsiveness.")]),
        "Testing techniques": E(
            "Acceptance testing checks the software meets the client's requirements. Alpha testing is early "
            "internal testing; beta testing gives a limited group of real external users the software before full "
            "release.\n\n"
            "Closed box (black box) testing uses only inputs and outputs, without looking at the code. Open box "
            "(white box) testing designs tests from the code's structure, so every path is exercised.\n\n"
            "Tests can be manual or automatic, and AI tools can help generate tests.",
            "A game is alpha tested by staff, then beta tested by 500 players who report bugs before launch.",
            [("What is the difference between alpha and beta testing?", "Alpha is internal; beta uses real external users."),
             ("What does open box testing use?", "Knowledge of the code's structure."),
             ("What does acceptance testing check?", "That the software meets the client's requirements.")]),
        "Test data": E(
            "Each test needs a purpose, test data, any prerequisites and an expected result.\n\n"
            "Test data comes in five kinds. Valid: normal data that should be accepted. Invalid: should be rejected. "
            "Valid extreme: at the very edge but still allowed. Invalid extreme: just outside the limit. Erroneous: "
            "the wrong type entirely.\n\n"
            "After testing, update the plan with actual results, any changes made, and re-tests or regression tests.",
            "For ages 11 to 18: valid 15, valid extreme 11 and 18, invalid extreme 10 and 19, invalid 30, erroneous 'fifteen'.",
            [("For a range 1 to 100, give an invalid extreme value.", "0 or 101."),
             ("What is a prerequisite?", "Something that must be set up before a test can run."),
             ("What should be recorded after fixing a bug?", "The change made and the re-test or regression test.")]),
    },
    "specialism/14-change-maintain-and-support.pptx": {
        "Why products change": E(
            "Software keeps changing after release, for three reasons.\n\n"
            "Preventing: dealing with foreseeable issues, such as new regulations, new devices, business changes or "
            "a new product.\n\n"
            "Correcting: fixing unforeseen errors, such as zero-day vulnerabilities, targeted attacks, data corruption "
            "or system failures.\n\n"
            "Iterating: keeping the product relevant, in response to user feedback, new technology, competitors, the "
            "need for efficiency, or future-proofing.",
            "A banking app updates for new security rules (preventing), patches a login bug (correcting), and adds "
            "dark mode because users asked (iterating).",
            [("Fixing a zero-day is which type of change?", "Correcting."),
             ("Adding a feature users requested is which type?", "Iterating."),
             ("Give an example of a preventing change.", "E.g. updating for new regulations.")]),
        "Software change management": E(
            "Changing live software is managed in stages.\n\n"
            "Identify the changes needed from feedback or review. Document the developments. Communicate with "
            "technical and non-technical audiences. Plan the changes. Schedule them. Regression test to make sure "
            "nothing else broke. Control and release the update, whether it's planned or an emergency fix.",
            "An emergency security fix skips the usual monthly release, but it's still documented, regression tested "
            "and announced in release notes.",
            [("Why regression test a change?", "To check nothing else broke."),
             ("Who needs to be told about changes?", "Technical and non-technical audiences."),
             ("Can emergency fixes skip documentation?", "No, they still need documenting and testing.")]),
        "Resolving user issues": E(
            "When users report problems, follow a systematic process.\n\n"
            "Identify or replicate the issue, so you can see it happen. Investigate the possible cause: user error, "
            "system error, application error or a security breach. Apply testing to find the error, make the change, "
            "confirm the error doesn't return and that no new issues appeared. Communicate how and when it was "
            "resolved to the right people. Document the lessons learned.\n\n"
            "Communicate in the right tone for the audience: release notes and FAQs for users, technical notes for developers.",
            "A user says the app crashes on photo upload. The developer replicates it with a large photo, finds no "
            "size check, adds one, retests and updates the FAQ.",
            [("What is the first step in resolving an issue?", "Identify or replicate it."),
             ("Name two possible causes of a user issue.", "E.g. user error, system error, application error, security breach."),
             ("Why document lessons learned?", "To prevent similar issues and help others.")]),
    },
}
