import typer
from ssg.site import Site


def main(source='content',dest='dist'):
    config={"source":source,"dest":dest}
    siteObj=Site(**config)
    siteObj.build()

typer.run(main)
