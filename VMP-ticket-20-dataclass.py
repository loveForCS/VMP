
class Data:
    name = 'Data'

    # accroding to data table to creat data class
    def __init__(self, id, autor_user_id, name, Link_to_article, is_public, is_for_static, is_for_dynamic, algo_type,
                 algo_auto_decription, created, updated):
        # type(id)=number
        self.id = id
        # type(autpr_user_id)=(FK),number
        self.autor_user_id = autor_user_id
        # type(Link)=String(formally URL)
        self.Link = Link_to_article
        # type(public)=Boolean
        self.public = is_public
        # type(static)=Boolean
        self.static = is_for_static
        # type(dynamic)=Boolean
        self.dynamic = is_for_dynamic
        # type(type)=(FK),number
        self.type = algo_type
        # type(desctiption)=Tect
        self.description = algo_auto_decription
        # type(created)=DateTime
        self.created = created
        # type(Updated)=DateTime
        self.updated = updated
