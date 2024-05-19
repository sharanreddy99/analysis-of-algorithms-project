<p align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" alt="project-logo">
</p>
<p align="center">
    <h1 align="center">ANALYSIS-OF-ALGORITHMS-PROJECT</h1>
</p>
<p align="center">
    <em>Unleashing Efficiency in Algorithmic Analysis!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/commit-activity/m/sharanreddy99/analysis-of-algorithms-project" alt="last-commit">
	<img src="https://img.shields.io/github/created-at/sharanreddy99/analysis-of-algorithms-project" alt="created_at">
   <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/sharanreddy99/analysis-of-algorithms-project">
   <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/sharanreddy99/analysis-of-algorithms-project">
   <img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/sharanreddy99/analysis-of-algorithms-project">

</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
</details>
<hr>


##  Overview

The analysis-of-algorithms-project offers a comprehensive platform for analyzing algorithm efficiency through tasks like optimal house painting and matrix computations. It leverages diverse modules to handle task comparisons, input generation, and result visualization, ensuring optimal solutions for various algorithmic challenges. The project's values lie in its streamlined execution of algorithm analysis tasks, from validating house painting sequences to finding optimal matrix bounding indices. Through its structured architecture and dynamic function calls, it enables efficient assessment and comparison of algorithm performance across different scenarios.

---

##  Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a modular architecture with separate modules for different tasks in the analysis of algorithms. It uses Flask for handling task execution and file operations via routes. The project's structure enhances efficiency in analyzing and visualizing algorithm results. |
| 🔩 | **Code Quality**  | The codebase demonstrates good code quality with clear function naming and structure. It follows Python best practices and maintains consistent style throughout the project. There is an emphasis on readability and maintainability. |
| 📄 | **Documentation** | The project offers extensive documentation, including descriptions for each task module, helper functions, and script files. It provides insights into the purpose and functionality of each component, aiding developers in understanding and extending the project. |
| 🔌 | **Integrations**  | Key integrations include Flask for handling web operations, Pandas for data manipulation, and Makefile for task automation. These integrations enhance the project's capabilities in executing and analyzing algorithm tasks efficiently. |
| 🧩 | **Modularity**    | The codebase exhibits high modularity, with distinct modules for different algorithm tasks. This design enables code reusability and easy maintenance. It allows for independent development and testing of each task module, promoting scalability and flexibility. |
| 🧪 | **Testing**       | The project utilizes testing frameworks such as Pytest for unit testing and functional testing. It ensures the reliability and accuracy of algorithm implementations by verifying their functionality against expected outcomes. |
| ⚡️  | **Performance**   | The project emphasizes efficiency in algorithm analysis, achieving optimal solutions for various tasks with different time and space complexities. It leverages priority queues, dynamic programming, and memoization to optimize speed and resource utilization. |
| 🛡️ | **Security**      | The project does not explicitly mention data protection measures. However, since it involves algorithm analysis and data processing, potential security considerations may include input validation, access control, and securing data storage and transmission. |
| 📦 | **Dependencies**  | Key external libraries and dependencies include Flask, Pandas, and Makefile. These libraries enhance the project's functionality in handling web operations, data manipulation, and task automation. |

---

##  Repository Structure

```sh
└── analysis-of-algorithms-project/
    ├── Project 1
    │   ├── .gitignore
    │   ├── Makefile
    │   ├── TASK1.py
    │   ├── TASK2.py
    │   ├── TASK3.py
    │   ├── TASK4.py
    │   ├── TASK5.py
    │   ├── helpers
    │   ├── main.py
    │   ├── script.sh
    │   ├── scriptsingle.sh
    │   └── server.py
    └── Project 2
        ├── .gitignore
        ├── Makefile
        ├── TASK1.py
        ├── TASK2.py
        ├── TASK3.py
        ├── TASK4.py
        ├── TASK5A.py
        ├── TASK5B.py
        ├── TASK6.py
        ├── TASK7A.py
        ├── TASK7B.py
        ├── helpers
        ├── main.py
        └── script.sh
```

---

##  Modules

<details closed><summary>Project 1</summary>

| File                                                                                                                         | Summary                                                                                                                                                                                                                                                                                                               |
| ---                                                                                                                          | ---                                                                                                                                                                                                                                                                                                                   |
| [script.sh](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/script.sh)             | Generates plots, tables, and test data for Project 1 tasks. Dynamically creates input, runs tasks, and visualizes algorithm analysis results based on specified parameters.                                                                                                                                           |
| [TASK2.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/TASK2.py)               | Validates and selects latest houses to paint based on optimal available intervals. Identifies the number of houses painted considering different scenarios. Achieves efficiency in selecting houses to be painted, offering an optimal solution for longer initial intervals.                                         |
| [server.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/server.py)             | Handles task execution and file operations via Flask routes; processes tasks and generates input/output files dynamically for analysis across various algorithms in the project structure.                                                                                                                            |
| [scriptsingle.sh](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/scriptsingle.sh) | Generates various plots and a table based on algorithm analysis results. Supporting tasks 1, 2, 3, and 4, it visualizes data regarding availability of painters, number of houses, response length, and execution time to aid in performance assessment.                                                              |
| [TASK1.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/TASK1.py)               | Analyzes the intervals to paint houses efficiently. Identifies houses to paint based on availability, achieving optimal solutions for unique startDays. May yield suboptimal results if initial houses have longer intervals.                                                                                         |
| [main.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/main.py)                 | Handles task comparison, input generation, and result plotting based on user arguments. Sorts input, prepares function calls, and displays optimal tasks. Integrates individual task modules for efficiency in analysis of algorithms project.                                                                        |
| [TASK4.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/TASK4.py)               | Defines a max house painting algorithm based on early endDays. Utilizes a priority queue to select houses for painting on the earliest endDay, optimizing for time and space complexities. Ensures optimum results for diverse test cases.                                                                            |
| [Makefile](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/Makefile)               | Facilitates running main.py for various tasks, inputs, and test generation. Supports multiple/single inputs, test case generation, plotting outputs, and generating tables. Enhances Project 1s ability to efficiently execute and analyze algorithm tasks.                                                           |
| [TASK5.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/TASK5.py)               | Analyzes house painting intervals to maximize painted houses based on earliest end dates. Prioritizes sorting by end date, then start date, and index. Key function extracts unique start days for efficient interval processing. Achieves O(m*logm) time complexity and O(m) space complexity for optimal solutions. |
| [TASK3.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/TASK3.py)               | Optimal painting sequence. Achieves optimal outcome when initial intervals are shorter than subsequent ones. May not yield best solution if larger intervals are overshadowed by many smaller ones.                                                                                                                   |

</details>

<details closed><summary>Project 1.helpers</summary>

| File                                                                                                                                           | Summary                                                                                                                                                                                                                                      |
| ---                                                                                                                                            | ---                                                                                                                                                                                                                                          |
| [plothelper.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/helpers/plothelper.py)               | Generates plots for algorithm analysis results with customizable axes labels, colors, and styles. Organizes data by tasks and outputs bar graphs with labeled bars for easy comparison.                                                      |
| [timehelpers.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/helpers/timehelpers.py)             | Calculates execution time for tasks in the algorithm analysis project. Implements time tracking functions.                                                                                                                                   |
| [iohelpers.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/helpers/iohelpers.py)                 | Handles input/output operations and data generation for algorithm tasks.-Includes functions for displaying output, reading input, generating dummy data, and plotting data using Pandas.-Ensures proper directory creation for data storage. |
| [randomlogichelper.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/helpers/randomlogichelper.py) | Generates random data for tasks 1 to 4 by creating sets of contiguous integer ranges (n, m), representing specific conditions and constraints. Supports various scenarios with different data distributions.                                 |
| [helpers.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 1/helpers/helpers.py)                     | Generates function calls and compares tasks based on input data. Facilitates task execution comparison, output to files, input file generation, and running tasks from the test file.                                                        |

</details>

<details closed><summary>Project 2</summary>

| File                                                                                                             | Summary                                                                                                                                                                                                                                                                                       |
| ---                                                                                                              | ---                                                                                                                                                                                                                                                                                           |
| [script.sh](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/script.sh) | Generates plots and tables for algorithm performance analysis by varying input parameters. Automates data generation, processing, and visualization to analyze and compare execution times. Supports multiple test cases and axes for comprehensive evaluation.                               |
| [TASK5B.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/TASK5B.py) | Implements a dynamic programming algorithm for finding a square region in a given matrix where all plots, except corners, require a minimum number of trees to be planted. Achieves Θ(m * n) time complexity using tabulation for Problem2 in the repository.                                 |
| [TASK2.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/TASK2.py)   | Implements an algorithm to find the bounding indices of a square area meeting minimum tree planting requirements in a matrix. Achieves a time complexity of Θ(m^2 * n^2).                                                                                                                     |
| [TASK1.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/TASK1.py)   | Implements a brute force algorithm to find the bounding indices of a square area in a matrix where each plot requires a minimum number of trees. Achieves Θ(m^3 * n^3) time complexity.                                                                                                       |
| [TASK7A.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/TASK7A.py) | Implements a Dynamic Programming algorithm for finding square regions within a matrix where plot requirements meet a condition. Employs memoization for efficient computation. Handles exemptions and computes optimal solutions.                                                             |
| [main.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/main.py)     | Executes, orchestrates, and manages tasks based on input commands. Integrates functions for task comparison, data generation, file execution, and visualization. Facilitates efficient task planning and analysis in a structured manner.                                                     |
| [TASK4.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/TASK4.py)   | Implements algorithm to find square area in matrix meeting tree requirements. Utilizes dynamic programming for efficient computation. Validates regions for maximal squares with corner exemptions. Achieves Θ(m * n^2) complexity.                                                           |
| [Makefile](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/Makefile)   | Executes various Python scripts through specific make commands for running, testing, and generating outputs within Project 2. Simplifies the process by providing predefined actions like running multiple tasks, generating test cases, plotting outputs, and more using the main.py script. |
| [TASK5A.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/TASK5A.py) | Implements and optimizes dynamic programming for finding the largest square area with minimum tree requirements in a matrix. Achieves Θ(m*n) time complexity using memoization, determining bounding indices efficiently.                                                                     |
| [TASK3.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/TASK3.py)   | Implements a Dynamic Programming algorithm to find bounding indices of a square area in a matrix. Determines the maximal square plot satisfying a minimum tree requirement, achieving a time complexity of O(m * n) and space complexity of O(n) within the repositorys architecture.         |
| [TASK7B.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/TASK7B.py) | Implements a dynamic programming algorithm to find the square area in a matrix where the tree count meets a minimum requirement under defined exemptions. Achieves Θ(m * n * k) time complexity with tabulation.                                                                              |
| [TASK6.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/TASK6.py)   | Implements a brute force algorithm to find a square area in a matrix where plots meet specific tree planting requirements, within set constraints. This algorithm aims to optimize time complexity in the broader analysis-of-algorithms project structure.                                   |

</details>

<details closed><summary>Project 2.helpers</summary>

| File                                                                                                                                           | Summary                                                                                                                                                                                                                                                                                   |
| ---                                                                                                                                            | ---                                                                                                                                                                                                                                                                                       |
| [plothelper.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/helpers/plothelper.py)               | Generates visual plots from data in the output directory, offering customization for line and bar graphs based on specified attributes. Organizes data by tasks and visualizes trends when certain metrics remain constant, facilitating analysis of algorithm performance for Project 2. |
| [timehelpers.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/helpers/timehelpers.py)             | Implements a timer utility for measuring execution time. Incorporated into Project 2 for profiling algorithms.                                                                                                                                                                            |
| [iohelpers.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/helpers/iohelpers.py)                 | Generates, reads, and displays various inputs while aiding in data visualization for Project 2 tasks. The helpers/iohelpers.py file assists in managing data for executing and analyzing algorithms efficiently within the repositorys architecture.                                      |
| [randomlogichelper.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/helpers/randomlogichelper.py) | Sizes, heights, and matrices. Enables dynamic task creation within Project 2s algorithm analysis framework.                                                                                                                                                                               |
| [helpers.py](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/master/Project 2/helpers/helpers.py)                     | Implements task comparison and result validation for Project 2 with dynamic function calls. Handles multi-input comparisons and single-input validations to ensure optimal task results. Supports generating random input files and executing tasks from test files.                      |

</details>

---

##  Getting Started

###  Installation

###  Usage

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/issues)**: Submit bugs found or log feature requests for the `analysis-of-algorithms-project` project.
- **[Submit Pull Requests](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/sharanreddy99/analysis-of-algorithms-project.git/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/sharanreddy99/analysis-of-algorithms-project.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com/sharanreddy99/analysis-of-algorithms-project.git/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=sharanreddy99/analysis-of-algorithms-project">
   </a>
</p>
</details>

---
