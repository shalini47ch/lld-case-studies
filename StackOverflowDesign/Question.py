class Question:
    def __init__(self,id,title,content,createdBy,tags,followers,answers,upvotes,downvotes,score,creationDate,modificationDate,status):
        self.id=id
        self.title=title
        self.content=content
        self.createdBy=createdBy
        self.tags=tags
        self.followers=followers
        self.answers=answers
        self.upvotes=upvotes
        self.downvotes=downvotes
        self.score=score
        self.creationDate=creationDate
        self.modificationDate=modificationDate
        # self.status=status
    
    def add_commment(self,comment):
        pass
    
    def add_bounty(self,bounty):
        pass

    