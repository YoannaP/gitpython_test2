import git

# path_in = "C:/MyDoc/Schroders/Year2/repos/in"
path_out = "C:/MyDoc/Schroders/Year2/repos/out/"

repo = git.Repo('C:/MyDoc/Schroders/Year2/repos')

repo.git.checkout('-b', 'output_run4')

file = open(path_out + "dummy.txt", "w")

repo.git.add(A=True)
repo.git.commit(m='added output in branch')
repo.git.push('origin', 'output_run4')

file.write("hello!")


file.close()
