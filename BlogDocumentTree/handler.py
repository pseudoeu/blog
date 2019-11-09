from pathlib import Path

BASE_DIR = '.'
EXTENSION = ('.md',)
IGNORE_DIR = ('.git', 'src', 'venv')

class DocumentHander:
    def documents(self, workdir: str = BASE_DIR):
        limb = []
        path = Path(workdir)
        for node in path.iterdir():
            if node.is_file():
                if node.suffix in EXTENSION:
                    limb.append({'file': node.relative_to(BASE_DIR), 'time': node.lstat().st_atime_ns})
            elif node.is_dir():
                if node.name in IGNORE_DIR:
                    pass
                leaf = self.documents(workdir=node)
                if leaf:
                    limb.append({'file': node.name, 'content': leaf, 'time': 0})
        return limb