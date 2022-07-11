# cz_int_jira

> Commitizen committer for all projects

## Usage with pre-commit and commitizen:

1.  Install [pre-commit](https://pre-commit.com)
2.  Install the package:

        pip3 install git+ssh://git@github.com/sadra/cz-conventional-integrated-with-jira.git@cz_int_jira

3.  Add the commitizen hook to your `.pre-commit-config.yaml`:

        repos:
        - repo: https://github.com/commitizen-tools/commitizen
          rev: v2.28.0 # automatically updated by Commitizen
          hooks:
            - id: commitizen
              additional_dependencies:
                - 'git+ssh://git@github.com/sadra/cz-conventional-integrated-with-jira.git@cz_int_jira'
              stages: [commit-msg]

4.  Update the hook if necessary:

    Until we start tagging components, you might need to clear your pre-commit cache and reinstall the hooks to ensure the latest version is installed:

        pre-commit clean
        pre-commit install --install-hooks

5.  Use `cz_int_jira` as the committer in `.cz.yaml`:

        commitizen:
            name: cz_int_jira
            update_changelog_on_bump: true
            version: 0.0.0