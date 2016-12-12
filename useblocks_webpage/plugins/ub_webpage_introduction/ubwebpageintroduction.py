import os
from groundwork_web.patterns import GwWebPattern


class UbWebpageIntroduction(GwWebPattern):
    def __init__(self, *args, **kwargs):
        self.name = self.__class__.__name__
        super().__init__(*args, **kwargs)

    def activate(self):
        self.web.contexts.register("ub",
                                   template_folder=os.path.join(os.path.dirname(__file__), "templates/"),
                                   static_folder=os.path.join(os.path.dirname(__file__), "static/"),
                                   url_prefix="/ub",
                                   description="Context for useblocks pages")

        self.web.routes.register("/", ["GET"], self.__introduction_view, context="ub")

    def __introduction_view(self):
        return self.web.render("introduction.html")
