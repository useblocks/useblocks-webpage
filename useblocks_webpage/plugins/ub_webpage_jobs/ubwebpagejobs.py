import os
import json
from groundwork_web.patterns import GwWebPattern


class UbWebpageJobs(GwWebPattern):
    def __init__(self, *args, **kwargs):
        self.name = self.__class__.__name__
        super().__init__(*args, **kwargs)

        with open(os.path.join(os.path.dirname(__file__), "jobs.json")) as job_file:
            self.jobs = json.load(job_file)
            for job in self.jobs:
                if job["active"] is not True:
                    self.jobs.remove(job)

        with open(os.path.join(os.path.dirname(__file__), "contact.json")) as contact_file:
            self.contact = json.load(contact_file)

    def activate(self):
        self.web.contexts.register("hires",
                                   template_folder=os.path.join(os.path.dirname(__file__), "templates/"),
                                   static_folder=os.path.join(os.path.dirname(__file__), "static/"),
                                   url_prefix="/hires",
                                   description="Context for useblocks job pages")

        self.web.routes.register("/", ["GET"], self.__jobs_view, context="hires", name="hires")
        self.web.routes.register("/<job_url>", ["GET"], self.__job_view, context="hires", name="hires_job")

    def __jobs_view(self):
        return self.web.render("jobs.html", jobs=self.jobs)

    def __job_view(self, job_url):
        for job in self.jobs:
            if job["url"] == job_url:
                if job["style"] not in ["yellow", "blue", "green"]:
                    job["style"] = "yellow"
                if job["author"] in self.contact.keys():
                    contact = self.contact[job["author"]]
                else:
                    contact = self.contact["woste"]

                return self.web.render("job.html", job=job, jobs=self.jobs, contact=contact)

        return self.web.render("job_unknown.html", job_url=job_url, jobs=self.jobs, contact=self.contact["woste"])
