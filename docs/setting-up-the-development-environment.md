# Development Environment Set-up

To create a development environment follow the steps outlined below.

---
## Setting Up Your Fork

When working with a fork, follow these steps to set up your local development environment:

- **Fork the repository:** Create your own copy of the repository on GitHub, following [this GitHub tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository).
- **Clone your fork:** Download your forked repository to your local machine as outlined in [this section of the tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#cloning-your-forked-repository).
- **Add the upstream remote:** Connect your local repository to the original repository to fetch updates as described in [this section](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#configuring-git-to-sync-your-fork-with-the-upstream-repository>).
- **Prevent accidental pushes to upstream:** After setting up your fork and configuring the original repository as an upstream remote, it's a good practice to prevent accidental pushes to the upstream repository. You can do this by explicitly setting the push URL of the upstream remote to no_push. To do this, navigate to your local repository and run:
``` bash
git remote set-url --push upstream no_push
```
- Verify the change with:
``` bash
git remote -v
```
You should see something like this:
``` bash
origin    https://github.com/your-username/repository.git (fetch)
origin    https://github.com/your-username/repository.git (push)
upstream  https://github.com/original-owner/repository.git (fetch)
upstream  no_push (push)
```
With this configuration, you can still fetch updates from the upstream repository but won’t be able to accidentally push changes to it.

---
## Creating Your Virtual Environment

The ocean4dvarnet-contrib is an extension of the ocean4dvarnet package. ocean4dvarnet require a CUDA / pytorch / pytorch-lignthing environment.

- Create and activate  a virtual environment with a python
    - For a full `CUDA / pytorch / pytorch-lignthing` environment,  follow the ocean4dvarnet documenmentation.
    - You can also use a virtual environment with a python version  >=3.10, and <3.12.
- Navigate to the repository you cloned, to the contribution directory you want to install the dependencies. ie for contribution `my_contrib` navigate to :
``` bash
cd contrib/my_contrib
```
- Install dependencies:
``` bash
pip install -r requirements.txt
```

