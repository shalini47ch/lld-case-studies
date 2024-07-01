class Answer:
    def __init__(self,id,content,postedBy,followers,comments,flagCount,upvotes,downvotes,isAccepted,creationDate):
        self.id=id
        self.content=content
        self.postedBy=postedBy
        self.followers=followers
        self.comments=comments
        self.flagCount=flagCount
        self.upvotes=upvotes
        self.downvotes=downvotes
        self.isAccepted=isAccepted
        self.creationDate=creationDate
         
    def addComment(self,comment):
        pass