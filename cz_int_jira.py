import os
import re
from collections import OrderedDict
from commitizen import cmd, git
from commitizen.config import BaseConfig
from commitizen.cz import exceptions
from commitizen.cz.conventional_commits import ConventionalCommitsCz
from commitizen.defaults import Questions
from commitizen import defaults

def parse_jira_ref(text):
    if not text:
        return ""

    matched = re.match("[A-Z]+-\d+", text)
    if not bool(matched):
        raise exceptions.AnswerRequiredError("Invalid JIRA reference.")

    return text

class CzIntegeratedJira(ConventionalCommitsCz):
    def __init__(self, config: BaseConfig):
        super().__init__(config)

    bump_pattern = defaults.bump_pattern
    bump_map = defaults.bump_map
    commit_parser = defaults.commit_parser
    change_type_order = ["BREAKING CHANGE",
                         "feat", "fix", "refactor", "perf", "build"]

    version_parser = defaults.version_parser
    change_type_map = {
        "feat": "Features",
        "fix": "Bug Fixes",
        "refactor": "Code Refactor",
        "perf": "Performance improvements",
        "build": "Build"
    }

    def questions(self) -> Questions:
        questions = super().questions()
        issue_key = None

        if git.is_git_project():
            branch_name = cmd.run('git branch --show-current')
            if branch_name.out:
                m = re.search('[A-Z]+-\d+', branch_name.out)
                issue_key = m[0] if m is not None else None

        if issue_key:
            questions.append({
                "type": "input",
                "name": "jira_ref",
                "default": issue_key,
                "message": (
                    "Jira reference\n"
                ),
                "filter": parse_jira_ref
            })
        else:
            questions.append({
                "type": "input",
                "name": "jira_ref",
                "message": (
                    f"Jira reference (press [enter] to skip)\n"
                ),
                "filter": parse_jira_ref
            })

        return questions

    def message(self, answers: dict) -> str:
        message = super().message(answers)

        footer = answers["footer"]
        jira_ref = answers["jira_ref"]
        if jira_ref:
            if footer:
                message = f"{message}\nJira-ref: {jira_ref}"
            else:
                message = f"{message}\n\nJira-ref: {jira_ref}"

        return message

    def example(self) -> str:
        return (
            "fix: correct minor typos in code\n\n"
            "Jira-ref: SPACE-1122"
        )

    def schema(self) -> str:
        return (
            "<type>(<scope>): <subject>\n"
            "<BLANK LINE>\n"
            "<body>\n"
            "<BLANK LINE>\n"
            "<footer>(Jira-ref: #<issue-id>)"
        )


discover_this = CzIntegeratedJira  # used by the plug-in system
