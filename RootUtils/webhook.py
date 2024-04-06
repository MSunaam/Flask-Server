def webhook(request, appConfig):
        if request.method == 'POST':
            repo = git.Repo(appConfig['REPO_PATH']) # type: ignore
            origin = repo.remotes.origin
            origin.pull()
            return 'Updated PythonAnywhere successfully', 200
        else:
            return 'Wrong event type', 400