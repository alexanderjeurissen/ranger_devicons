# Contributing to Ranger Devicons

Please take a moment to review this document in order to make the contribution
process easy and effective for everyone involved.

Following these guidelines helps to communicate that you respect the time of
the developers managing and developing this open source project. In return,
they should reciprocate that respect in addressing your issue or assessing
patches and features.

## Using the issue tracker

The issue tracker is the preferred channel for [bug reports](#bugs),
[features requests](#features) and [submitting pull
requests](#pull-requests), but please respect the following restrictions:

* Please **do not** use the issue tracker for personal support requests (use the
  [Community Forum](https://github.com/alexanderjeurissen/ranger_devicons/discussions/categories/personal-support) to ask the Ranger Devicons Community for help).

* Please **do not** derail or troll issues. Keep the discussion on topic and
  respect the opinions of others.
  
* Please **adhere** to the issue template provided for bugs / feature requests and provide an answer to all posed questions.

<a name="bugs"></a>
## Bug reports

A bug is a _demonstrable problem_ that is caused by the code in the repository.
Good bug reports are extremely helpful - thank you!

Guidelines for bug reports:

1. **Use the GitHub issue search** &mdash; check if the issue has already been
   reported.

2. **Check if the issue has been fixed** &mdash; try to reproduce it using the
   latest `main` branch in the repository.

3. **Isolate the problem** &mdash; make sure that the code in the repository is
_definitely_ responsible for the issue.

4. **Adhere to the issue template** &mdash; Ensure your issue meets the [issue template](https://github.com/alexanderjeurissen/ranger_devicons/blob/main/.github/ISSUE_TEMPLATE/bug_report.md). Issues that do not match the template will be closed automatically.

A good bug report shouldn't leave others needing to chase you up for more
information. Please try to be as detailed as possible in your report.

<a name="features"></a>
## Feature requests

Feature requests are welcome. But take a moment to find out whether your idea
fits with the scope and aims of the project. It's up to *you* to make a strong
case to convince the Ranger Devicons developers of the merits of this feature. Please
provide as much detail and context as possible.

Guidelines for feature requests:

1. **Adhere to the issue template** &mdash; Ensure your issue meets the [issue template](https://github.com/alexanderjeurissen/ranger_devicons/blob/main/.github/ISSUE_TEMPLATE/feature_request.md). Issues that do not match the template will be closed automatically.

<a name="pull-requests"></a>
## Pull requests

Good pull requests - patches, improvements, new features - are a fantastic
help. They should remain focused in scope and avoid containing unrelated
commits.

**Please ask first** before embarking on any significant pull request (e.g.
implementing features, refactoring code), otherwise you risk spending a lot of
time working on something that the developers might not want to merge into the
project.

Please adhere to the coding conventions used throughout the project (indentation,
comments, etc.).

Adhering to the following this process is the best way to get your work
merged:

1. [Fork](http://help.github.com/fork-a-repo/) the repo, clone your fork,
   and configure the remotes:

   ```bash
   # Clone your fork of the repo into the current directory
   git clone https://github.com/<your-username>/<repo-name>
   # Navigate to the newly cloned directory
   cd <repo-name>
   # Assign the original repo to a remote called "upstream"
   git remote add upstream https://github.com/<upsteam-owner>/<repo-name>
   ```

2. If you cloned a while ago, get the latest changes from upstream:

   ```bash
   git checkout <main-branch>
   git pull upstream <main-branch>
   ```

3. Create a new topic branch (off the main project branch) to
   contain your feature, change, or fix:

   ```bash
   git checkout -b <topic-branch-name>
   ```

4. Commit your changes in logical chunks. Please adhere to these [git commit
   message guidelines](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)
   or your code is unlikely be merged into the main project. Use Git's
   [interactive rebase](https://help.github.com/articles/interactive-rebase)
   feature to tidy up your commits before making them public.

5. Locally merge (or rebase) the upstream main branch into your topic branch:

   ```bash
   git pull [--rebase] upstream <main-branch>
   ```

6. Push your topic branch up to your fork:

   ```bash
   git push origin <topic-branch-name>
   ```

10. [Open a Pull Request](https://help.github.com/articles/using-pull-requests/)
    with a clear title and description.
