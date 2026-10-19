# An assisted workspace for ATS3

Informal requirements — initial discussion draft

## Purpose

Build a system that helps users get started with ATS3 and develop ATS3
projects. Overleaf is an inspiration for an accessible, integrated workspace;
the exact hosting model and implementation remain open.

Eventually, the system should serve both newcomers and experienced ATS3 users.
The first version should be small and useful, with assistance such as locating
templates and starting projects from them.

## Two first-class interfaces

The system should provide a GUI for human users and an interface suited to AI
operators, such as a CLI. Both interfaces should expose the same underlying
project and template operations wherever applicable.

An AI is a “SUPERUSER” in the sense that it can operate the system directly and
effectively on a user's behalf. This term does not, by itself, require system
administrator privileges or unrestricted access to the host machine.

The AI interface is a core requirement. An AI should be able to discover and
invoke operations without navigating the GUI. A built-in chatbot is optional;
an external AI agent should also be able to use the interface.

## Proposed lightweight first version

Start with a small curated template catalog and the ability to create a project
from a template. Provide these capabilities through both a simple GUI and an
AI-oriented CLI. Avoid requiring a complete browser IDE to make this useful.

### Find and inspect templates

- Users can list and search available templates by task, keyword, or ATS3 concept.
- Each template has a stable identifier, a short description, and enough
  information to judge when to use it.
- Users can inspect the template's files and usage instructions before choosing it.
- Templates identify relevant compiler requirements, dependencies, and build or
  run instructions where applicable.
- A template may be a small teaching example or a starting point for a larger
  project. Its intended purpose should be clear.

Initially, a local catalog with simple keyword search is sufficient. AI-assisted
selection can use this catalog without requiring semantic search in the system.

### Start a project

- Users can create a named project from a selected template.
- The resulting files are accessible to ordinary editors and external AI tools.
- Creating a project preserves the source template and does not silently
  overwrite an existing project.
- The system records which template the project came from, including its version
  or revision when available.
- The result tells the user where the project is and how to proceed.

### Human interface

The first GUI should support browsing or searching the catalog, inspecting a
template, and creating a project. It should show understandable results and
errors. A full editor, terminal, or chat interface is not required initially.

### AI-oriented interface

- Core operations can run without interactive prompts, with all required inputs
  supplied explicitly.
- Commands offer discoverable help describing arguments and expected results.
- Commands support structured output, such as JSON, with consistent fields and
  useful exit codes.
- Errors distinguish cases such as an unknown template, invalid input, or an
  existing destination, and provide actionable details when possible.
- Results identify created or changed resources so the AI can take the next step.
- Read-only operations are clearly distinguishable from operations that change
  state. Repeating a command should have predictable behavior.
- The CLI uses the same underlying logic as the GUI, including validation and
  access rules if access control is introduced.

Illustrative commands, with naming still to be decided:

```sh
atswork template search "list traversal" --json
atswork template inspect list-basic --json
atswork project create demo --template list-basic --json
```

## Working with an AI

A human should be able to describe a task to an AI, have the AI locate a suitable
template, inspect it, and create a project through the provided interface.

The human should then be able to inspect the same project. Work created through
one interface should be usable through the other, without separate project
formats or hidden AI-only state.

As editing capabilities are added, changes should be inspectable and recoverable.
AI authority should follow the user's task and the system's access rules; routine
authorized operations should not require repeated confirmations.

## Likely next capabilities

These are candidates for later iterations, rather than commitments for the first
version:

- Compile or check a project and return diagnostics through both interfaces.
- Run supported examples and show their output.
- Help explain compiler errors and locate relevant examples or documentation.
- Add project editing, change review, and version history.
- Validate templates against supported compiler versions to keep them usable.
- Let users contribute, share, and maintain templates.
- Support richer project search and navigation for experienced users.

If compilation and execution are hosted, the system will need suitable resource
limits and isolation for user code.

## Outside the initial scope

Real-time collaborative editing, a complete browser IDE, public project hosting,
complex account administration, and autonomous maintenance of the shared catalog
are not necessary to establish the first useful workflow.

## What would count as a successful first version?

A human can use the GUI to find a template, understand its purpose, and create a
project. An external AI can accomplish the same task using the CLI alone, using
structured results to determine whether each operation succeeded. Both produce
projects that the human can inspect and continue working on.

A small set of good templates and a dependable interface are sufficient for this
milestone; broad template coverage is not required.

## Open questions

- Should the first version run locally, on a server, or support both?
- Which ATS3 templates would make the initial catalog most useful?
- How should templates be packaged, versioned, and updated?
- Should compilation be part of the first milestone or the next one?
- What is the smallest useful GUI, and how should it hand projects to an editor?
- Which existing ATS3 tools and repository conventions should the system reuse?

These questions should guide the next planning discussion. The command names,
storage layout, and implementation technologies are intentionally undecided.
