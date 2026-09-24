"""
Where each deck's inline link goes on each page.

Maps deck file -> {page: [targets]}. A target is either:
  - a specification number such as "2.4", matched against the number (or
    number range) at the start of a page's ## or ### heading;
  - "top", placing the link after the page's introduction (for a deck that
    covers the whole page);
  - any other string, matched against the start of a heading's text.

The link goes at the end of the section's text. If a deck's sections are not
next to each other on the page, the link appears after each group.
"""

CP1 = "01-core-component/01-core-paper-1.md"
CP2 = "01-core-component/02-core-paper-2.md"
ESP = "01-core-component/03-employer-set-project.md"
NOTATION = "03-appendices/02-flowchart-and-python-notation.md"
SP = "02-occupational-specialism/"
ANALYSE = SP + "01-analyse-a-problem.md"
ETHICS = SP + "02-ethics-and-risk.md"
SOURCES = SP + "03-sources-of-knowledge.md"
DESIGN = SP + "04-design.md"
COLLAB = SP + "05-social-and-collaborative-environment.md"
IMPL = SP + "06-implementation.md"
TESTING = SP + "07-testing.md"
CHANGE = SP + "08-change-maintain-support.md"


def _r(a, b):
    """Numbers a to b inclusive within one content area, e.g. _r('6.1', '6.6')."""
    area, start = a.split(".")
    return [f"{area}.{n}" for n in range(int(start), int(b.split(".")[1]) + 1)]


PLACEMENT = {
    "core/01-computational-thinking-and-algorithms.pptx": {CP1: ["1.1", "1.2"], NOTATION: ["Flowchart symbols"]},
    "core/02-problem-solving-strategies.pptx": {CP1: ["1.3"]},
    "core/03-data-types-variables-and-data-structures.pptx": {
        CP1: _r("2.1", "2.3"), NOTATION: ["Data structures"]},
    "core/04-operators-input-output-and-program-flow.pptx": {CP1: _r("2.4", "2.6"), NOTATION: ["Text files"]},
    "core/05-functions-procedures-and-validation.pptx": {CP1: ["2.7", "2.8"]},
    "core/06-programming-practice-and-robust-code.pptx": {CP1: ["2.9", "2.10"]},
    "core/07-searching-and-sorting-algorithms.pptx": {CP1: ["2.11"]},
    "core/08-testing.pptx": {CP1: ["2.12"]},
    "core/09-emerging-issues-and-technologies.pptx": {CP1: ["3.1", "3.2"]},
    "core/10-legislation-and-guidelines.pptx": {CP1: ["4.1", "4.2"]},
    "core/11-the-business-context.pptx": {CP2: _r("5.1", "5.3")},
    "core/12-technical-change-management.pptx": {CP2: ["5.4"]},
    "core/13-data-fundamentals.pptx": {CP2: _r("6.1", "6.6")},
    "core/14-data-quality-systems-and-analysis.pptx": {CP2: _r("6.7", "6.12")},
    "core/15-hardware-and-software.pptx": {CP2: ["7.1", "7.2"]},
    "core/16-networks.pptx": {CP2: ["7.3"]},
    "core/17-virtual-cloud-and-resilient-environments.pptx": {CP2: _r("7.4", "7.6")},
    "core/18-security-threats-and-vulnerabilities.pptx": {CP2: ["8.1", "8.2"]},
    "core/19-threat-mitigation-cia-and-iaaa.pptx": {CP2: ["8.3", "8.4"]},
    "core/20-employer-set-project.pptx": {ESP: ["top"]},
    "specialism/01-sdlc-and-requirements.pptx": {ANALYSE: ["1.1", "1.4"]},
    "specialism/02-team-roles-and-project-methodologies.pptx": {ANALYSE: ["1.2", "1.3"]},
    "specialism/03-emerging-technologies-and-skills.pptx": {ANALYSE: ["1.5", "1.6"]},
    "specialism/04-legal-and-ethical-development.pptx": {ETHICS: ["2.1"]},
    "specialism/05-identifying-and-managing-risk.pptx": {ETHICS: ["2.2"]},
    "specialism/06-sources-of-knowledge-and-evaluation.pptx": {SOURCES: ["top"]},
    "specialism/07-design-approaches.pptx": {DESIGN: ["4.1"]},
    "specialism/08-platforms-version-control-and-collaboration.pptx": {DESIGN: ["4.2"], COLLAB: ["top"]},
    "specialism/09-ux-and-ui-design.pptx": {DESIGN: ["4.3"], IMPL: ["6.2"]},
    "specialism/10-designing-data-assets-and-integration.pptx": {DESIGN: ["4.3"]},
    "specialism/11-languages-ci-cd-and-good-practice.pptx": {IMPL: ["6.1"]},
    "specialism/12-data-connections-and-deployment.pptx": {IMPL: ["6.3", "6.4"]},
    "specialism/13-testing-a-software-solution.pptx": {TESTING: ["top"]},
    "specialism/14-change-maintain-and-support.pptx": {CHANGE: ["top"]},
}
