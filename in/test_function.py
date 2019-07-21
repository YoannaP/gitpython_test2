import git

# path_in = "C:/MyDoc/Schroders/Year2/repos/in"
path_out = "C:/MyDoc/Schroders/Year2/repos/out/"

repo = git.Repo('C:/MyDoc/Schroders/Year2/repos')

repo.git.checkout('-b', 'output_run2')

file = open(path_out + "dummy.txt", "w")

repo.git.add(A=True)
repo.git.commit(m='added output in branch')
repo.git.push('--set-upstream', 'origin', current)

file.write("hello!")


file.close()
