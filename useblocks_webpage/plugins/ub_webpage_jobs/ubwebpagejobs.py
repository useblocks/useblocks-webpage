import os
from groundwork_web.patterns import GwWebPattern


class UbWebpageJobs(GwWebPattern):
    def __init__(self, *args, **kwargs):
        self.name = self.__class__.__name__
        super().__init__(*args, **kwargs)

        self.jobs = [
            {
                "id": "dev_emb",
                "name": "Embedded SW Developer",
                "url": "embedded_sw_developer",
                "logo": "heart_binary_black.png",
                "long_name": "Software Developer for embedded projects in international automotive companies",
                "description": "As embedded software developer you work on hardware near projects of internation "
                               "automotive companies. You will be part of an international cross company team and"
                               "be responsible from the first idea to the final product.",
                "skills": {
                    "coding": {
                        "C": 5,
                        "C++": 4,
                        "Python": 3,
                    },
                    "project": {
                        "Team lead": 3,
                        "Time management": 3,
                        "English skills": 5,
                    }
                },
                "tasks": [
                    "Writing and testing software",
                    "Document software",
                    "Define and document processes",
                    "Rapid prototyping for different solution",
                    "Analyse prototypes",
                    "Test software in vehicles",
                    "Participate on international vehicle test days"
                ]
            },
            {
                "id": "dev_py",
                "name": "Python SW Developer",
                "url": "python_sw_developer",
                "logo": "heart_binary_black.png",
                "long_name": "Software Developer for Python projects in international automotive companies",
                "description": "As Python developer ypu help engineers to developt their projects faster and with an "
                               "higher quality. You are deeply integrated into teams....",
                "skills": {
                    "coding": {
                        "C": 5,
                        "C++": 4,
                        "Python": 3,
                    },
                    "project": {
                        "Team lead": 3,
                        "Time management": 3,
                        "English skills": 5,
                    }
                },
                "tasks": [
                    "Writing and testing software",
                    "Document software",
                    "Define and document processes",
                    "Rapid prototyping for different solution",
                    "Analyse prototypes",
                    "Test software in vehicles",
                    "Participate on international vehicle test days"
                ]
            }
        ]

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
                return self.web.render("job.html", job=job, jobs=self.jobs)

        return self.web.render("job_unknown.html", job_url=job_url, jobs=self.jobs)
