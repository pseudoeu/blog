from BlogDocumentTree.handler import DocumentHander, BASE_DIR

START_COMMAND = ('<!--',)
STOP_COMMAND = ('-->',)

KNOW_COMMANDS = {
    'footer': lambda argument: False,
    'post': lambda argument: False
}

def make_footer(sessions_list: list) -> str:
    footer = ''
    for session in sessions_list:
        footer += '[{}]({}) '.format(session['alias'], session['url'])
    return footer

def process_post(argument: str):
    pass


if __name__ == '__main__':
    handler = DocumentHander()
    documents = handler.documents()
    print(sorted(documents,key=lambda x:x['time'],reverse=False))
    subblogs =  [ {'alias': 'Home', 'url': "{}/readme.md".format(BASE_DIR)}] + \
                [ {'alias': el['file'], 'url': "{}/{}/readme.md".format(BASE_DIR, el['file'])
                    } for el in documents if el['time'] == 0
    ]
    print(make_footer(subblogs))