from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from Config.db import meta,engine
from datetime import datetime

posts = Table("post",meta,
Column("id",Integer,primary_key=True),
Column("user",String(50)),
Column("post",String(250)),
Column("created_at",DateTime,default=datetime.now())
)

meta.create_all(engine)