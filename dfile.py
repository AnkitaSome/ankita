from git import Repo, remote 
#importing git module
import os
#ankita  
def clone_github(git_url,repo_dir):
    repo=Repo.clone_from(git_url, repo_dir)
    print(repo)
    print(repo.git.status())
#printing the git status sd
    print(repo.git.log())
#printing the git log 
    return repo



if __name__=="__main__":
    usr_name=input("\nEnter the name of github user: ")
    repo=input("\nInput the name of particular repository :")
    path_to_file=input("Enter the path to local repo ")
    git_url="https://github.com/"+usr_name+"/"+repo+".git"
#github remote repository http url
    repo_dir=path_to_file
#path to your local repository where you want to clone your remote repository
   
    #for fetching perticuler file
    a=clone_github(git_url,repo_dir)
    origin=a.remote(name='origin')
    origin.fetch()
    
    entries = os.listdir('/home/hp/project/ankita/')
    for entry in entries:
        print(entry)
    
