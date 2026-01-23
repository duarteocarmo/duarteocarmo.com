title: How to police your agents
description: We're building more than ever. But how do we manage the complexity? We police our agents.
date: 23rd of January 2026
status: published
audio: true
thumbnail: images/94/cover.png



<img src="{static}/images/94/police-agents.jpg" alt="Monahan the Police Chief" style="max-width:100%;border-radius: 2px;">


Let's face it. It *might just be* the year of agents. If you work in tech and your workflow hasn't changed in the last year or so - you're probably doing something wrong. For those of you who have. It's fun. We're building more than ever before!

But there's a dark cloud in the sky. It's the pile of trash, it's the amount of unmaintainable complexity we're putting out there. Let's get the record straight — if you're writing something to throw away — you shouldn't care about any of this, but the ones that do this professionally probably should. At the end of the day - we'll have to stick around, maintain it, make sure it performs, make sure it doesn't break in unexpected ways.

Either it's a training run, a large ML pipeline, a search eval. We need to guarantee the *quality* of what we're shipping: We need to police our agents.

Now how do you do that? I do it in three ways.

## The Constitution

My global `AGENTS.md` [ref]Or `CLAUDE.md`, it doesn't matter. They are all symlinked. [Claude Code](https://claude.ai/code), [OpenCode](https://opencode.ai/), [Codex](https://developers.openai.com/codex/cli/), or even [pi](https://shittycodingagent.ai/), they all use the same set of rules.[/ref] is where I define the most important laws I want my agents to follow. These are closely related to my personality and taste. It's a file with scars of everything I've seen wrong from the start of my career.

The file has 55 lines of Markdown and grows daily. "About Your User," "Your Behavior," "Principles," "Code Search," or "Languages" are just some of the sections it has. The idea behind it is simple: whatever I’m working on should adhere to my way of working. Also, I'm peculiar about how I want my agents to interact with me. For example, I don't want it to speak Chinese to me, I don’t want it to assume I know things I know nothing about.

Here are some highlights from my `AGENTS.md`

```markdown
...
## Documentation and plans
- If docs were touched, make sure you update them with latest changes. You can run some quick ripgreps with md files to confirm if needed.
- For docs: Be concise and durable - point to source code for specifics rather than hardcoding values that will get out of sync
- Every time the user starts repeating something very specific about a project, consider adding a rule to the AGENTS.md or CLAUDE.md of that project if one exists.
...

## Languages
- I understand portuguese, french, italian, spanish, and english. Everything else, you should show the original AND the translation
- Outputing in any other language is useless, and show come with a corresponding translation

## Principles
- Every line of code is a liability - we should strive to make our code simple and concise
- I prefer my functions to be small in interface but long in functionality 
- We don't MOCK in tests. We use real data and real APIs. I absolutely hate mocking
...
```

It's a series of *very* specific rules I want my agents to respect. You might like a different set of rules — and that's fine — I don't expect us to like the same things. But I don't believe you don't have preferences. So make sure to create one as well.

This file is the Constitution. And the rules of the Constitution apply to anything I'm doing. But every project has *quirks*.

## The rules of the game

Every project has something specific and annoying. More likely if you're working with a team. They can be anything: A weird commit convention, a particular way of running tests, a specific server that needs to be run, an unconventional way of making a release.

Your project's `AGENTS.md` defines the rules of the game. That's where you inform the agents about the quirks of the project. A cool little trick I use is to prompt my global `AGENTS.md` file to update my project level `AGENTS.md` file if anything I am doing is very repetitive.

```markdown
... Global AGENTS.md
- Every time the user starts repeating something very specific about a project, consider adding a rule to the AGENTS.md or CLAUDE.md of that project if one exists.
```

Here's an example snippet of a real world project `AGENTS.md`. This one is for a Machine Learning pipeline built using AWS CDK:

```markdown
...Local AGENTS.md
- For database queries, when the user is asking questions (not for code implementations), use `aws rds-data execute-statement` with the Aurora resource ARN and Secrets Manager secret ARN.
- Code artifacts should be placed in ./code_artifacts/ directory
- Scripts should be placed in the ./scripts/ directory and should be uv scripts (https://docs.astral.sh/uv/guides/scripts/)
- If name has an acronym, like `ML`, `OIDC` only capitalise the first letter, e.g. `Ml`, `Oidc`.
- Adhere to CDK Best Practices https://docs.aws.amazon.com/cdk/v2/guide/best-practices.html
- Ensure comments are added only when they are natural and consistent with the rest of the file
- Include defensive checks or try/catch blocks only when they align with the norms of that area of the codebase (especially if not called by trusted / validated codepaths)
- Maintain consistency with the style used throughout the file
- Add comments when we are doing something non-obvious or complex, not to separate every line of code
...
```

*Note: You might also consider using something like [Skills](https://code.claude.com/docs/en/skills) to solve this level of policing. Some people prefer them. I use a mix.*

This ensures that whoever is building here, will generally follow the same guidelines. And these rules can go a long way to making your life easier — but they still don't *enforce* anything — for that, we need **the police**.  

## The police

Policing is all about enforcing rules. What better way to enforce rules for code, than with static code analysis? Before agents, I used to find these annoying. But nowadays, if there are 154 line-length issues in the project, I can just spin off an agent to solve it.

And so, I am *very* picky when policing agents. Let's go through a Python example.

Everything starts (as always) with a `Makefile`. This is where I define the main commands to be run. I always include a `format` and a `check` command. Remember, we are policing, we are picky, we are annoying: ruff, Pyright, deptry, we run it all.

```Makefile
.PHONY: format
format: # Format the codebase with ruff
 uv lock --check
 uv run ruff check . --fix
 uv run ruff format .

.PHONY: check
check: # Run linting and check
 uv lock --check
 uv run ruff format --check .
 uv run ruff check .
 uv run pyright
 uv run deptry .
```

We are so annoying, that we enforce more rules that we would enforce to ourselves. So, for example, for ruff, we extend the rules to avoid our agent dropping a sneaky TODO comment instead of implementing something that should be there.

```toml
[tool.ruff.lint]
extend-select = [
  "F",   # Pyflakes rules
  "W",   # PyCodeStyle warnings
  "E",   # PyCodeStyle errors
  "I",   # Sort imports properly
  "UP",  # Warn if certain things can changed due to newer Python versions
  "C4",  # Catch incorrect use of comprehensions, dict, list, etc
  "FA",  # Enforce from __future__ import annotations
  "ISC", # Good use of string concatenation
  "ICN", # Use common import conventions
  "RET", # Good return practices
  "SIM", # Common simplification rules
  "TID", # Some good import practices
  "TC",  # Enforce importing certain types in a TYPE_CHECKING block
  "PTH", # Use pathlib instead of os.path
  "TD",  # Be diligent with TODO comments
  "NPY", # Some numpy-specific things
]
# Note: Shamelessly stolen from reddit user
```

It's a nice, programmatic, and deterministic way of enforcing rules without having to write each one into an `AGENTS.md` and hope the agent follows them. With that, every time the agent writes some code, it runs `make format` and then `make check`. If anything fails, it fixes it.

## Final thoughts

We are becoming faster and faster at producing software. By now, that’s not *a possibility*, that’s a fact. But the problem was never writing the code. It was always about two things: (1) knowing what code *not* to write and (2) managing complexity. And what better way of managing complexity than by diligently *policing* your agents?

Vibe, but not too close to the sun.

---
