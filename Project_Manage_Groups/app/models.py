from sqlalchemy import Enum as SqlEnum, Boolean, Column, ForeignKey, Integer, String, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship
from sqlalchemy.sql import expression
from .database import Base
from enum import Enum

class StatusEnum(Enum):
    accepted = "accepted"
    pending = "pending"
    declined = "declined"


class User(Base):
    __tablename__ = "user"  

    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    user_name = Column(String(50), nullable=False)
    hashed_password = Column(String(300), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    blogs = relationship("Blog", back_populates="author")
    comment = relationship("Comment", back_populates="user")
    react = relationship("React", back_populates="user")
    group_member = relationship("GroupMember", back_populates ="member")
    join_group_request = relationship("JoinGroupRequests", back_populates= "user")
    group_invitation = relationship("GroupInvitation", back_populates="user")

class Group(Base):
    __tablename__ = "group" 

    id = Column(Integer, primary_key=True)
    group_name = Column(String(100), nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now())  
    description = Column(Text)
    blogs = relationship("Blog", back_populates="group")
    group_member = relationship("GroupMember", back_populates="group")
    join_group_request = relationship("JoinGroupRequests", back_populates= "group")
    group_invitation = relationship("GroupInvitation", back_populates="group")

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    category_name = Column(String(100), nullable=False)
    blogs = relationship("Blog", back_populates="category")

class Blog(Base):
    __tablename__ = "blog"  

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False, index=True)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("user.id"))  
    group_id = Column(Integer, ForeignKey("group.id"))  
    category_id = Column(Integer, ForeignKey("category.id")) 
    created_date = Column(TIMESTAMP, server_default=func.now())  
    updated_date = Column(TIMESTAMP, onupdate =func.now())
    is_published = Column(Boolean, nullable=False, server_default=expression.true())
    author = relationship("User", back_populates="blogs")
    group = relationship("Group", back_populates="blogs")
    category = relationship("Category", back_populates="blogs")
    comment = relationship("Comment", back_populates="blog")
    react = relationship("React", back_populates="blog")

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    blog_id = Column(Integer, ForeignKey("blog.id"))
    content = Column(Text, nullable=False) 
    created_date = Column(TIMESTAMP, server_default=func.now())
    user = relationship("User", back_populates="comment") 
    blog = relationship("Blog", back_populates="comment") 

class React(Base):
    __tablename__ = "react"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    blog_id = Column(Integer, ForeignKey("blog.id"))
    user = relationship("User", back_populates="react")
    blog = relationship("Blog", back_populates="react")

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True)
    rolename = Column(String(100), nullable=False)
    group_member = relationship("GroupMember", back_populates="role")

class GroupMember(Base):
    __tablename__ = "group_member"

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey("user.id"))
    group_id = Column(Integer, ForeignKey("group.id"))
    role_id = Column(Integer, ForeignKey("role.id"))
    status = Column(Boolean, nullable=False, default=True)
    member = relationship("User", back_populates="group_member")
    group = relationship("Group", back_populates="group_member")
    role = relationship("Role", back_populates="group_member")

class JoinGroupRequests(Base):
    __tablename__ = "join_group_requests"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))  
    group_id = Column(Integer, ForeignKey("group.id")) 
    status = Column(SqlEnum(StatusEnum), nullable = False, server_default=StatusEnum.pending.value)
    user = relationship("User", back_populates="join_group_request")
    group = relationship("Group", back_populates="join_group_request")

class GroupInvitation(Base):
    __tablename__ = "group_invitation"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("group.id"))
    to_user_id = Column(Integer, ForeignKey("user.id"))
    status = Column(SqlEnum(StatusEnum), nullable = False, server_default=StatusEnum.pending.value)
    user = relationship("User", back_populates="group_invitation")
    group = relationship("Group", back_populates="group_invitation")