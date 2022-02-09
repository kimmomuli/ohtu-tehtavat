from json import tool
from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_dictionary = toml.loads(content)

        dependencies = []
        dev_dependencies = []

        for x, y in toml_dictionary['tool']['poetry']['dependencies'].items():
            dependencies.append(x)


        for x, y in toml_dictionary['tool']['poetry']['dev-dependencies'].items():
                    dev_dependencies.append(x)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            toml_dictionary['tool']['poetry']['name'],
            toml_dictionary['tool']['poetry']['description'],
            dependencies,
            dev_dependencies
        )
