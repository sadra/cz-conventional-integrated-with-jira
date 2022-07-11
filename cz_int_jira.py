from commitizen.cz.base import BaseCommitizen
from commitizen.defaults import Questions

class CzIntegeratedJira(BaseCommitizen):
    # Questions = Iterable[MutableMapping[str, Any]]
    # It expects a list with dictionaries.
    def questions(self) -> Questions:
        """Questions regarding the commit message."""
        questions = [
            {
                'type': 'input',
                'name': 'title',
                'message': 'Commit title'
            },
            {
                'type': 'input',
                'name': 'issue',
                'message': 'Jira Issue number:'
            },
        ]
        return questions

    def message(self, answers: dict) -> str:
        """Generate the message with the given answers."""
        return '{0} (#{1})'.format(answers['title'], answers['issue'])

    def example(self) -> str:
        """Provide an example to help understand the style (OPTIONAL)

        Used by `cz example`.
        """
        return 'Problem with user (#321)'

    def schema(self) -> str:
        """Show the schema used (OPTIONAL)

        Used by `cz schema`.
        """
        return '<title> (<issue>)'

    def info(self) -> str:
        """Explanation of the commit rules. (OPTIONAL)

        Used by `cz info`.
        """
        return 'We use this because is useful'


discover_this = CzIntegeratedJira  # used by the plug-in system
