#!/usr/bin/env python3
"""
Use secretlint to find secrets in sources
https://github.com/secretlint/secretlint
"""

import os

from megalinter import Linter


class SecretLintLinter(Linter):

    # Called before linting files
    def before_lint_files(self):
        # Use .gitignore as .secretlintignore
        # only if --secretlintignore is not defined and .secretlintignore not found
        if "--secretlintignore" not in self.cli_lint_user_args and (
            os.path.isfile(os.path.join(self.workspace, ".gitignore"))
            and (not os.path.isfile(os.path.join(self.workspace, ".secretlintignore")))
        ):
            self.cli_lint_extra_args += ["--secretlintignore", ".gitignore"]
