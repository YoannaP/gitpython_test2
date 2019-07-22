import git

# path_in = "C:/MyDoc/Schroders/Year2/repos/in"
path_out = "C:/MyDoc/Schroders/Year2/repos/out/"
REPO_PATH = 'C:/MyDoc/Schroders/Year2/repos'

repo = git.Repo(REPO_PATH)

repo.git.checkout('-b', 'output_run')

file = open(path_out + "dummy.txt", "w")

repo.git.add(A=True)
repo.git.commit(m='added output in branch again')
repo.git.push('origin', 'output_run')


file.write("hello!")


file.close()
