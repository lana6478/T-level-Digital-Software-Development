"""
Deck content for the lesson slides, one module per area of the course.

Each deck is a dict with:
    area        core | spec   (sets colour and label)
    file        output path under content/05-teaching-resources/slides/
    title       deck title
    unit        short location, e.g. "Core Paper 1"
    spec        specification sections covered, e.g. "1.1, 1.2"
    pages       content/ pages the deck is linked from (first = main page)
    objectives  3 to 4 learning objectives
    starter     starter question
    slides      teaching slides (see render.py for the slide types)
    quiz        list of (question, answer)
    activity    {title, time, format, steps, success, notes}
    exit        3 exit-ticket prompts

Never use em or en dashes in deck text; the build refuses them.
"""
SITE = {
    "name": "Digital Software Development T Level",
    "short": "Digital Software Development",
    "url": "https://lana6478.github.io/T-level-Digital-Software-Development/",
    "author": "Samuel O'Connell",
    "awarding_body": "Pearson",
    "spec_url": "https://qualifications.pearson.com/content/dam/pdf/TLevels/digital-software-development/"
                "2025/specification-and-sample-assessment-materials/digital-dsd-specification.pdf",
    # pages listed under "Related pages" on the Lesson Slides index
    "related": [
        "01-core-component/00-overview.md",
        "02-occupational-specialism/00-overview.md",
        "04-help-and-about/01-help.md",
    ],
}

# Areas of the course: label shown on slides, accent colour (hex), and
# light_text for accents dark enough to need white numbers on them.
AREAS = {
    "core": {"label": "Core Component", "accent": "F2B705"},
    "spec": {"label": "Occupational Specialism", "accent": "33C17A"},
}

from . import core_p1, core_p2, specialism  # noqa: E402

ALL_DECKS = core_p1.DECKS + core_p2.DECKS + specialism.DECKS

AREA_ORDER = [
    {"key": "core", "heading": "Core Component",
     "blurb": "Core Paper 1, Core Paper 2 and the Employer Set Project."},
    {"key": "spec", "heading": "Occupational Specialism",
     "blurb": "The eight content areas of the Digital Software Development specialism."},
]
