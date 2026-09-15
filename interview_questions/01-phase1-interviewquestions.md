Phase 1 : Interview Preparation

I should be able to explain the following concepts after completing Phase 1.

Question 1: Why did you use a virtual environment?
Answer

I used a Python virtual environment to isolate the project's dependencies from the system Python installation and from other projects. This makes the environment reproducible and prevents dependency conflicts.

Question 2: Why didn't you put the API key directly in your Python code?
Answer

API keys are sensitive credentials. Hardcoding them in source code could expose them through Git history or a public repository. I used an environment variable and a local .env file, while adding .env to `.gitignore.

Question 3: What is the difference between .env and .env.example?
Answer

.env contains the actual local configuration values and is kept private. .env.example contains placeholder values and documents the configuration required to run the application, so it can safely be committed to GitHub.

Question 4: Why is .venv not committed to GitHub?
Answer

The virtual environment contains locally installed packages and environment-specific files. It can be recreated from the project's dependency file, so committing it would unnecessarily increase the repository size and reduce portability.

Question 5: What is requirements.txt?
Answer

It records the Python dependencies required by the project so that another developer can recreate the project's environment using those dependencies.

Question 6: What is Git and how is it different from GitHub?
Answer

Git is a distributed version-control system that tracks changes to source code. GitHub is a hosting and collaboration platform where Git repositories can be stored remotely and shared.

Question 7: Explain your Git workflow.
Answer

I first inspect changes using git status and git diff, stage the intended files with git add, create a descriptive commit with git commit, and push the commit to the GitHub remote using git push.
