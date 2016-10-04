import os
from groundwork_web.patterns import GwWebPattern


class UbWebpageIntroduction(GwWebPattern):
    def __init__(self, *args, **kwargs):
        self.name = self.__class__.__name__
        super().__init__(*args, **kwargs)

    def activate(self):
        self.web.contexts.register("demo",
                                   template_folder=os.path.join(os.path.dirname(__file__), "templates/"),
                                   static_folder=os.path.join(os.path.dirname(__file__), "static/"),
                                   url_prefix=None,
                                   description="Context fpr demo pages")

        self.web.routes.register("/", ["GET"], self.__introduction_view, context="demo")

    def __introduction_view(self):
        return self.web.providers.render("introduction.html")


