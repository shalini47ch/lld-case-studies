#we will use the education,experience and skill and use that in the profile section
from Experience import Experience
from Education import Education
from Skill import Skill
#similarly import Achievements and Analytics
from Achievement import Achievement
from Analytics import Analytics


class Profile:
    def __init__(self, headline, about, gender, profile_picture, cover_photo):
        self.headline=headline
        self.about=about
        self.gender=gender
        self.profile_picture=profile_picture
        self.cover_photo=cover_photo
        self.experiences=[]
        self.education=[]
        self.skills=[]
        self.achievements=[]
        self.analytics=Analytics(0,0,0,0)
    
    def add_experience(self,experience):
        if isinstance(experience,Experience):
            self.experiences.append(experience)
        else:
            raise TypeError("Expected an instance of experience")
    
    #similarly add education,skills
    def add_education(self,education):
        if isinstance(education,Education):
            self.education.append(education)
        else:
            raise TypeError("Expected an instance of education")
    #adding  the skills section
    def add_skills(self,skill):
        if isinstance(skill,Skill):
            self.skills.append(skill)
        else:
            raise TypeError("Expected an instance of skill")
    #here addding achievements
    
    def add_achivements(self,achievement):
        if isinstance(achievement,Achievement):
            self.achievements.append(achievement)
        else:
            raise TypeError("Expected an instance of the achivement")
    
    #now here we are creating some getter functions to get the implementations 
    def get_experience(self):
        return self.experiences
    
    def get_education(self):
        return self.education
    
    def get_skills(self):
        return self.skills
    
    def get_achievements(self):
        return self.achievements



    
    
    
    
    