from os import mkdir
from pathlib import  Path
import pathlib

class Site():

    def __init__(self,source,dest):
        self.source=Path(source)
        self.dest=Path(dest)

    def create_dir(self,path):
        directory=self.dest / Path.relative_to(self.source)
        mkdir(parents=True,exist_ok=True)

    def build(self):
        mkdir(self.dist,parents=True,exist_ok=True)
        for i in self.source.rglob('*'):
            pass
            