from app.models import wordselector

# ------------------------------------user----------------------------------- #
usuario = {}

def getUserData(usuario='dev'):
    user = {}
    user['views'] = [
        {'nm':'wordselector','view':['wordselector','selector']},
        {'nm':'battleracing','view':['battleracing','tester']},
    ]
    user['user'] = usuario
    user['app'] = user['views'][0]
    return user