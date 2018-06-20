import os
import json
from groundwork_web.patterns import GwWebPattern


class UbWebpage(GwWebPattern):
    def __init__(self, *args, **kwargs):
        self.name = self.__class__.__name__
        super().__init__(*args, **kwargs)

        # jobs
        self.jobs = []
        jobs_path = os.path.join(os.path.dirname(__file__), "..", "..", "data", "jobs")

        for file in os.listdir(jobs_path):
            if file.endswith(".json"):
                file_path = os.path.join(jobs_path, file)
                with open(file_path, encoding='utf-8') as job_file:
                    job = json.load(job_file)
                    if job["active"] is True:
                        self.jobs.append(job)

        # contact
        with open(os.path.join(os.path.dirname(__file__), "..", "..", "data", "contacts.json")) as contact_file:
            self.contacts = json.load(contact_file)

        # tools
        with open(os.path.join(os.path.dirname(__file__), "..", "..", "data", "tools.json")) as tools_file:
            self.tools = json.load(tools_file)
        self.active_tools = []
        for item in self.tools:
            if item["active"]:
                self.active_tools.append(item)

        # press
        with open(os.path.join(os.path.dirname(__file__), "..", "..", "data", "press.json")) as press_file:
            self.press = json.load(press_file)
        self.active_press = []
        for item in self.press:
            if item["active"]:
                self.active_press.append(item)

        # presentations
        with open(os.path.join(os.path.dirname(__file__), "..", "..", "data", "presentations.json")) as presentations_file:
            self.presentations = json.load(presentations_file)
        self.active_presentations = []
        for item in self.presentations:
            if item["active"]:
                self.active_presentations.append(item)

    def activate(self):
        self.web.contexts.register("ub",
                                   template_folder=os.path.join(os.path.dirname(__file__), "templates/"),
                                   static_folder=os.path.join(os.path.dirname(__file__), "static/"),
                                   url_prefix="/ub",
                                   description="Context for useblocks pages")

        self.web.routes.register("/", ["GET"], self.__introduction_view, context="ub")

        self.web.routes.register("/hires", ["GET"], self.__jobs_view, context="ub", name="hires")
        self.web.routes.register("/hires/<job_url>", ["GET"], self.__job_view, context="ub", name="hires_job")

        self.web.routes.register("/datenschutz", ["GET"], self.__datenschutz_view, context="ub", name="datenschutz")
        self.web.routes.register("/impressum", ["GET"], self.__impressum_view, context="ub", name="impressum")

    def __introduction_view(self):
        return self.web.render("introduction.html", jobs=self.jobs,
                               contacts=self.contacts, tools=self.active_tools,
                               presentations=self.active_presentations, press=self.active_press)

    def __jobs_view(self):
        return self.web.render("jobs.html", jobs=self.jobs)

    def __job_view(self, job_url):
        for job in self.jobs:
            if job["url"] == job_url:
                if job["style"] not in ["yellow", "blue", "green"]:
                    job["style"] = "yellow"
                if job["author"] in self.contacts.keys():
                    contact = self.contacts[job["author"]]
                else:
                    contact = self.contacts["woste"]

                return self.web.render("job.html", job=job, jobs=self.jobs, contact=contact)

        return self.web.render("job_unknown.html", job_url=job_url, jobs=self.jobs, contact=self.contacts["woste"])

    def __datenschutz_view(self):
        return self.web.render("datenschutz.html")

    def __impressum_view(self):
        return self.web.render("impressum.html")

