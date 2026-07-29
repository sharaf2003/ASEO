from ai_engine.git_manager import (
    RepositoryManager,
    CommitManager,
    VersionManager
)



repo = RepositoryManager()



commit = CommitManager()



version = VersionManager()



result = {


    "repository":

        repo.initialize(

            "ecommerce_api"

        ),



    "commit":

        commit.create_commit(

            "Initial commit"

        ),



    "version":

        version.create_version()

}



print(result)