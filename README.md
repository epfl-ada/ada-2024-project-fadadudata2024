# ada-2024-project-fadadudata2024

## Instruction
In Milestone P2, together with your team members, you will agree on and refine your project proposal. Your first task is to select a project. Even though we provide the datasets for you to use, at this juncture, it is your responsibility to perform initial analyses and verify that what you propose is feasible given the data (including any additional data you might bring in yourself), which is crucial for the success of the project.

The goal of this milestone is to intimately acquaint yourself with the data, preprocess it, and complete all the necessary descriptive statistics tasks. We expect you to have a pipeline in place, fully documented in a notebook, and show us that you have clear project goals.

When describing the relevant aspects of the data, and any other datasets you may intend to use, you should in particular show (non-exhaustive list):

That you can handle the data in its size.
That you understand what’s in the data (formats, distributions, missing values, correlations, etc.).
That you considered ways to enrich, filter, transform the data according to your needs.
That you have a reasonable plan and ideas for methods you’re going to use, giving their essential mathematical details in the notebook.
That your plan for analysis and communication is reasonable and sound, potentially discussing alternatives to your choices that you considered but dropped.
We will evaluate this milestone according to how well these steps have been done and documented, the quality of the code and its documentation, the feasibility and critical awareness of the project. We will also evaluate this milestone according to how clear, reasonable, and well thought-through the project idea is. Please use the second milestone to really check with us that everything is in order with your project (idea, feasibility, etc.) before you advance too much with the final Milestone P3! There will be project office hours dedicated to helping you.

You will work in a public GitHub repository dedicated to your project, which can be created by following this link. The repository will automatically be named ada-2023-project-. By the Milestone P2 deadline, each team should have a single public GitHub repo under the [epfl-ada GitHub organization](https://github.com/epfl-ada), containing the project proposal and initial analysis code.

P2 deliverable (done as a team): GitHub repository with the following:

Readme.md file containing the detailed project proposal (up to 1000 words). Your README.md should contain:
Title
Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
Research Questions: A list of research questions you would like to address during the project.
Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
Methods
Proposed timeline
Organization within the team: A list of internal milestones up until project Milestone P3.
Questions for TAs (optional): Add here any questions you have for us related to the proposed project.
GitHub repository should be well structured and contain all the code for the initial analyses and data handling pipelines. For structure, please use this repository as a template
Notebook presenting the initial results to us. We will grade the correctness, quality of code, and quality of textual descriptions. There should be a single Jupyter notebook containing the main results. The implementation of the main logic should be contained in external scripts/modules that will be called from the notebook.

## Project structure
The directory structure of new project looks like this:
├── data                        <- Project data files
│
├── src                         <- Source code
│   ├── data                            <- Data directory
│   ├── models                          <- Model directory
│   ├── utils                           <- Utility directory
│   ├── scripts                         <- Shell scripts
│
├── tests                       <- Tests of any kind
│
├── results.ipynb               <- a well-structured notebook showing the results
│
├── .gitignore                  <- List of files ignored by git
├── pip_requirements.txt        <- File for installing python dependencies
└── README.md