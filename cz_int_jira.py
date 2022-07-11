import os
import re
from collections import OrderedDict
from commitizen import cmd, git
from commitizen.config import BaseConfig
from commitizen.cz import exceptions
from commitizen.cz.conventional_commits import ConventionalCommitsCz
from commitizen.defaults import Questions
from commitizen import defaults


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

        return questions

    def message(self, answers: dict) -> str:
        message = super().message(answers)
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
