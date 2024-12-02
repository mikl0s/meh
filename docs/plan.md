# Project Plan: MEH - Machine Eye Heuristics

## Epics and Stories

---

### Epic 1: Repository Setup and Initial Commit

**Summary:** Initialize the repository and set up the initial project structure.

- [x] **Story 1.1: Adapt `.gitignore` to exclude `venv` and unnecessary files**
    *Testing Focus:* Check that `venv` and other unwanted files are correctly ignored.
- [x] **Story 1.2: Generate professional logo for the project**
    *Testing Focus:* Ensure the logo is appropriate and visually appealing.
- [x] **Story 1.3: Update `README.md` with modern design, icons, badges, and logo**
    *Testing Focus:* Confirm that `README.md` displays correctly with all enhancements.
- [x] **Story 1.4: Commit and push everything with tag `0.0.1`**
    *Testing Focus:* Verify that the commit everything from `git status` is properly tagged and pushed to the repository.

---

### Epic 2: Dual-Pane Text-Based GUI for Filesystem Browsing

**Summary:** Develop a dual-pane text-based GUI for file navigation.

- [ ] **Story 2.1: Set up basic text-based GUI framework**
    *Testing Focus:* Ensure the GUI framework initializes without errors.
- [ ] **Story 2.2: Implement directory navigation with arrow keys**
    *Testing Focus:* Verify users can navigate directories using arrow keys.
- [ ] **Story 2.3: Enable file selection with `Enter` key**
    *Testing Focus:* Check that files and folders open upon pressing `Enter`.
- [ ] **Story 2.4: Implement pane switching using `Tab` key**
    *Testing Focus:* Confirm that panes switch focus when `Tab` is pressed.
- [ ] **Story 2.5: Filter displayed files to show only `ffmpeg`-supported video formats**
    *Testing Focus:* Ensure only supported video files are displayed.
- [ ] **Story 2.6: Apply ANSI coloring to enhance GUI visuals**
    *Testing Focus:* Verify that ANSI colors render correctly in the GUI.
- [ ] **Story 2.7: Include icons for files and directories**
    *Testing Focus:* Check that icons are correctly displayed and enhance usability.

---

### Epic 3: Video Quality Comparison Functionality

**Summary:** Enable users to select two video files and compare their perceptual quality.

- [ ] **Story 3.1: Allow user to select two video files from GUI**
    *Testing Focus:* Confirm two video files can be selected without issues.
- [ ] **Story 3.2: Implement perceptual video quality assessment algorithm**
    *Testing Focus:* Validate the accuracy and reliability of the quality assessment.
- [ ] **Story 3.3: Simulate viewing conditions of a 65" 4K/UHD OLED TV**
    *Testing Focus:* Ensure the simulation parameters match specified conditions.
- [ ] **Story 3.4: Calculate perceptual quality scores for each video**
    *Testing Focus:* Check that individual scores are correctly calculated.
- [ ] **Story 3.5: Compute perceptual quality difference between videos (0-100 scale)**
    *Testing Focus:* Verify the difference score is accurate and within the correct scale.

---

### Epic 4: Export Functionality

**Summary:** Provide options to export the comparison results in various formats.

- [ ] **Story 4.1: Accept up to three filename inputs, with third determining export format**
    *Testing Focus:* Ensure input parsing correctly identifies filenames and formats.
- [ ] **Story 4.2: Determine export format based on third input's file extension**
    *Testing Focus:* Confirm the export format matches the file extension provided.
- [ ] **Story 4.3: Display detailed report on screen when no third input is given**
    *Testing Focus:* Verify the on-screen report is detailed and formatted correctly.
- [ ] **Story 4.4: Sanitize report for export to exclude colors and icons**
    *Testing Focus:* Ensure exported reports are clean and free of GUI-specific formatting.
- [ ] **Story 4.5: Implement export functionality for Markdown format**
    *Testing Focus:* Check that the Markdown report is correctly generated.
- [ ] **Story 4.6: Implement export functionality for JSON format**
    *Testing Focus:* Validate the JSON structure and data accuracy.
- [ ] **Story 4.7: Implement export functionality for YAML format**
    *Testing Focus:* Ensure the YAML report adheres to proper syntax and structure.
- [ ] **Story 4.8: Implement export functionality for XML format**
    *Testing Focus:* Confirm the XML output is well-formed and valid.

---

### Epic 5: Configuration and Logging

**Summary:** Add configuration options and logging capabilities.

- [ ] **Story 5.1: Create `meh.conf` configuration file with adjustable settings**
    *Testing Focus:* Verify the configuration file is read and applied correctly.
- [ ] **Story 5.2: Provide an example configuration file**
    *Testing Focus:* Ensure the example file is helpful and correctly formatted.
- [ ] **Story 5.3: Implement reading of configuration settings in the program**
    *Testing Focus:* Check that program behavior changes according to config settings.
- [ ] **Story 5.4: Implement logging of input filenames**
    *Testing Focus:* Confirm that input filenames are accurately logged.
- [ ] **Story 5.5: Implement logging of output filenames**
    *Testing Focus:* Verify that output filenames are correctly recorded.
- [ ] **Story 5.6: Log perceptual video quality results (excluding detailed report)**
    *Testing Focus:* Ensure that only the summary results are logged.

---

### Epic 6: Code Quality and Testing Tools

**Summary:** Set up tools to enforce code quality and implement testing.

- [ ] **Story 6.1: Set up `pytest` for unit testing**
    *Testing Focus:* Confirm that `pytest` is properly installed and configured.
- [ ] **Story 6.2: Write unit tests for existing functionality**
    *Testing Focus:* Ensure all current code is covered by unit tests.
- [ ] **Story 6.3: Integrate `mypy` for type checking**
    *Testing Focus:* Check that type annotations are correct and `mypy` passes.
- [ ] **Story 6.4: Integrate `flake8` for linting**
    *Testing Focus:* Verify the codebase is free of linting errors.
- [ ] **Story 6.5: Integrate `black` for code formatting**
    *Testing Focus:* Ensure code is consistently formatted by `black`.

---

### Epic 7: Pre-commit Hooks

**Summary:** Automate code checks before commits.

- [ ] **Story 7.1: Set up pre-commit hook to run `mypy`**
    *Testing Focus:* Confirm that commits are blocked if `mypy` checks fail.
- [ ] **Story 7.2: Set up pre-commit hook to run `flake8`**
    *Testing Focus:* Ensure commits are prevented when linting issues are present.
- [ ] **Story 7.3: Set up pre-commit hook to run `black`**
    *Testing Focus:* Verify code is auto-formatted before commit is finalized.

---

### Epic 8: User Documentation and README Enhancement

**Summary:** Improve user documentation and make setup easy.

- [ ] **Story 8.1: Update `README.md` with setup instructions**
    *Testing Focus:* Ensure setup instructions are clear and accurate.
- [ ] **Story 8.2: Add usage examples to `README.md`**
    *Testing Focus:* Verify that usage examples work as documented.
- [ ] **Story 8.3: Include badges for build status, license, etc.**
    *Testing Focus:* Check that badges display correctly and reflect current status.

---

### Epic 9: General Improvements and User Experience

**Summary:** Refine the program for better usability and maintainability.

- [ ] **Story 9.1: Refactor code for readability and maintainability**
    *Testing Focus:* Ensure code changes improve readability without breaking functionality.
- [ ] **Story 9.2: Implement logging using the `logging` module**
    *Testing Focus:* Confirm that logging works and logs are appropriately detailed.
- [ ] **Story 9.3: Ensure functions and methods are small and focused**
    *Testing Focus:* Verify that each function has a single responsibility.
- [ ] **Story 9.4: Avoid hardcoding values; use configuration or environment variables**
    *Testing Focus:* Check that configurable values are no longer hardcoded.
- [ ] **Story 9.5: Keep dependencies updated and avoid deprecated packages**
    *Testing Focus:* Confirm all dependencies are up-to-date and compatible.
- [ ] **Story 9.6: Document all public methods and classes with docstrings**
    *Testing Focus:* Ensure all public interfaces are properly documented.
- [ ] **Story 9.7: Use descriptive variable and function names**
    *Testing Focus:* Verify that naming conventions improve code clarity.
- [ ] **Story 9.8: Perform code reviews before merging any pull requests**
    *Testing Focus:* Establish code review process and adherence.

---

### Epic 10: Deployment and Release Management

**Summary:** Prepare the project for deployment and manage releases.

- [ ] **Story 10.1: Set up feature branches for development**
    *Testing Focus:* Confirm that branching strategy is implemented correctly.
- [ ] **Story 10.2: Ensure code passes all tests and checks before merging**
    *Testing Focus:* Verify that merging is only possible when all checks pass.
- [ ] **Story 10.3: Tag releases appropriately in Git**
    *Testing Focus:* Check that release tags follow semantic versioning.
- [ ] **Story 10.4: Update `README.md` and documentation with each release**
    *Testing Focus:* Ensure documentation reflects the latest changes.

---

### Epic 11: Continuous Improvement of Test Coverage

**Summary:** Maintain and improve test coverage over time.

- [ ] **Story 11.1: Analyze current test coverage using `pytest --cov`**
    *Testing Focus:* Verify that coverage reports are generated and accurate.
- [ ] **Story 11.2: Write additional unit tests to cover uncovered code**
    *Testing Focus:* Ensure new tests increase overall coverage.
- [ ] **Story 11.3: Integrate coverage checks into pre-commit hooks**
    *Testing Focus:* Confirm that commits are blocked if coverage drops below threshold.
- [ ] **Story 11.4: Regularly review and update tests as code changes**
    *Testing Focus:* Ensure tests remain relevant and effective over time.

---
