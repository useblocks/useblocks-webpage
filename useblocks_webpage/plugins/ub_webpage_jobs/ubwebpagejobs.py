import os
from groundwork_web.patterns import GwWebPattern


class UbWebpageJobs(GwWebPattern):
    def __init__(self, *args, **kwargs):
        self.name = self.__class__.__name__
        super().__init__(*args, **kwargs)

    def activate(self):
        self.web.contexts.register("hires",
                                   template_folder=os.path.join(os.path.dirname(__file__), "templates/"),
                                   static_folder=os.path.join(os.path.dirname(__file__), "static/"),
                                   url_prefix="/hires",
                                   description="Context for useblocks job pages")

        self.web.routes.register("/", ["GET"], self.__jobs_view, context="hires", name="hires")

    def __jobs_view(self):
        return self.web.render("jobs.html")
