def webhook(request):
        if request.method == 'POST':
            repo = git.Repo('path/to/git_repo') # type: ignore
            origin = repo.remotes.origin
            origin.pull()
            return 'Updated PythonAnywhere successfully', 200
        else:
            return 'Wrong event type', 400