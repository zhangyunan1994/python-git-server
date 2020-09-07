import git


git_repo = git.Repo("/Users/zhangyunan/PycharmProjects/pygs")

print(git_repo.bare)

print(git_repo.is_dirty())

print(git_repo.untracked_files)
print(git_repo.head)
print(git_repo.git.status())
print(git_repo.git.log())
print(git)
