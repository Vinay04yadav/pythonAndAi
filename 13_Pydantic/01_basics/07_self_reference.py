# think about comments. we have a comment model and inside that we have comment model (someone makes a comment and people reply to that comment and so on)


from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id : int
    content : str

    # A comment can contain a list of replies.
    # Each reply is itself another Comment object.
    # This is called a self-referencing (recursive) model.
    # Optional means replies can also be None.
    # 'Comment' is written as a string because the class is still being defined when this reference is encountered.
    replies : Optional[List['Comment']] = None


# Resolves the forward reference 'Comment' after the class is fully defined.
# Pydantic now knows that replies contains a list of Comment objects.
# model_rebuild() is useful when Pydantic couldn't resolve the reference
# during the initial class definition.

Comment.model_rebuild()

# We use 'Comment' in quotes because the class is still being defined.
# List[Comment] would try to reference Comment before its definition is complete.
# 'Comment' is a forward reference, resolved later using model_rebuild().



comment = Comment(
    id= 1,
    content= "First Comment",
    replies=[
        Comment(id=2, content="Reply 1"),
        Comment(id=3, content="Reply 2", replies=[
            Comment(id=4, content="nested reply")
        ])
    ]
)

print(comment)