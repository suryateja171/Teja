# """
# Mini Instagram Clone — single-file FastAPI app (SQLite)
<<<<<<< HEAD
=======

>>>>>>> junior
# Features:
# - Register & Login (JWT auth)
# - Create Post (caption + image_url)
# - Feed (posts with like count & comments)
# - Like/Unlike a post
# - Comment on a post

# How to run:
# 1) Create a venv (recommended) and install deps:
#    pip install fastapi "uvicorn[standard]" SQLAlchemy passlib[bcrypt] PyJWT python-multipart pydantic
# 2) Start server:
#    uvicorn app:app --reload
# 3) Open docs:
#    http://127.0.0.1:8000/docs

# Notes:
# - This is an educational MVP. No email verification, rate limiting, media uploads, or follow graph.
# - Images are referenced by URL. Use any image URL to test.
# """

# from datetime import datetime, timedelta
# from typing import List, Optional

# from fastapi import FastAPI, Depends, HTTPException, status, UploadFile, File, Form
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel, Field, HttpUrl

# from sqlalchemy import (Column, Integer, String, DateTime, ForeignKey, Text, create_engine,
#                         Boolean, UniqueConstraint)
# from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session

# from passlib.context import CryptContext
# import jwt
# import os

# # --------------------------- Config --------------------------- #
# SECRET_KEY = os.getenv("APP_SECRET", "dev-secret-change-me")
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24h

# DATABASE_URL = "sqlite:///./mini_ig.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

# # --------------------------- Models --------------------------- #
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50), unique=True, index=True, nullable=False)
#     password_hash = Column(String(255), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)

#     posts = relationship("Post", back_populates="author", cascade="all, delete-orphan")
#     likes = relationship("Like", back_populates="user", cascade="all, delete-orphan")
#     comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")

# class Post(Base):
#     __tablename__ = "posts"
#     id = Column(Integer, primary_key=True, index=True)
#     caption = Column(Text, default="")
#     image_url = Column(Text, nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

#     author = relationship("User", back_populates="posts")
#     likes = relationship("Like", back_populates="post", cascade="all, delete-orphan")
#     comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")

# class Like(Base):
#     __tablename__ = "likes"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
#     post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     __table_args__ = (UniqueConstraint('user_id', 'post_id', name='uq_user_post_like'),)

#     user = relationship("User", back_populates="likes")
#     post = relationship("Post", back_populates="likes")

# class Comment(Base):
#     __tablename__ = "comments"
#     id = Column(Integer, primary_key=True)
#     text = Column(Text, nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
#     post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)

#     user = relationship("User", back_populates="comments")
#     post = relationship("Post", back_populates="comments")

# # --------------------------- Schemas --------------------------- #
# class UserCreate(BaseModel):
#     username: str = Field(min_length=3, max_length=50)
#     password: str = Field(min_length=6, max_length=128)

# class UserOut(BaseModel):
#     id: int
#     username: str
#     created_at: datetime
#     class Config:
#         from_attributes = True

# class Token(BaseModel):
#     access_token: str
#     token_type: str = "bearer"

# class PostCreate(BaseModel):
#     caption: Optional[str] = ""
#     image_url: HttpUrl

# class CommentCreate(BaseModel):
#     text: str = Field(min_length=1, max_length=500)

# class CommentOut(BaseModel):
#     id: int
#     text: str
#     user_id: int
#     username: str
#     created_at: datetime

# class PostOut(BaseModel):
#     id: int
#     caption: str
#     image_url: str
#     created_at: datetime
#     author_id: int
#     author_username: str
#     like_count: int
#     liked_by_me: bool
#     comments: List[CommentOut]

# # --------------------------- Utils --------------------------- #

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# def verify_password(password: str, hashed: str) -> bool:
#     return pwd_context.verify(password, hashed)

# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> User:
#     credentials_error = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_error
#     except jwt.PyJWTError:
#         raise credentials_error

#     user = db.query(User).filter(User.username == username).first()
#     if user is None:
#         raise credentials_error
#     return user

# # --------------------------- App --------------------------- #
# app = FastAPI(title="Mini Instagram Clone")
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Create tables
# Base.metadata.create_all(bind=engine)

# # --------------------------- Routes --------------------------- #
# @app.post("/register", response_model=UserOut, status_code=201)
# def register(payload: UserCreate, db: Session = Depends(get_db)):
#     if db.query(User).filter(User.username == payload.username).first():
#         raise HTTPException(status_code=400, detail="Username already taken")
#     user = User(username=payload.username, password_hash=hash_password(payload.password))
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user

# @app.post("/login", response_model=Token)
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = db.query(User).filter(User.username == form_data.username).first()
#     if not user or not verify_password(form_data.password, user.password_hash):
#         raise HTTPException(status_code=400, detail="Incorrect username or password")
#     token = create_access_token({"sub": user.username})
#     return {"access_token": token, "token_type": "bearer"}

# @app.post("/posts", response_model=PostOut, status_code=201)
# def create_post(payload: PostCreate, current: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     post = Post(caption=payload.caption or "", image_url=str(payload.image_url), user_id=current.id)
#     db.add(post)
#     db.commit()
#     db.refresh(post)
#     return _post_to_out(post, current, db)

# @app.get("/feed", response_model=List[PostOut])
# def get_feed(skip: int = 0, limit: int = 20, current: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     posts = db.query(Post).order_by(Post.created_at.desc()).offset(skip).limit(limit).all()
#     return [_post_to_out(p, current, db) for p in posts]

# @app.post("/posts/{post_id}/like", response_model=dict)
# def like_post(post_id: int, current: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#     existing = db.query(Like).filter(Like.post_id == post_id, Like.user_id == current.id).first()
#     if existing:
#         db.delete(existing)
#         db.commit()
#         return {"status": "unliked"}
#     like = Like(post_id=post_id, user_id=current.id)
#     db.add(like)
#     db.commit()
#     return {"status": "liked"}

# @app.post("/posts/{post_id}/comment", response_model=CommentOut, status_code=201)
# def comment_post(post_id: int, payload: CommentCreate, current: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found")
#     c = Comment(post_id=post_id, user_id=current.id, text=payload.text)
#     db.add(c)
#     db.commit()
#     db.refresh(c)
#     return CommentOut(id=c.id, text=c.text, user_id=current.id, username=current.username, created_at=c.created_at)

# @app.delete("/posts/{post_id}", response_model=dict)
# def delete_post(post_id: int, current: User = Depends(get_current_user), db: Session = Depends(get_db)):
#     post = db.query(Post).filter(Post.id == post_id, Post.user_id == current.id).first()
#     if not post:
#         raise HTTPException(status_code=404, detail="Post not found or not yours")
#     db.delete(post)
#     db.commit()
#     return {"status": "deleted"}

# # --------------------------- Helpers --------------------------- #

# def _post_to_out(p: Post, current: User, db: Session) -> PostOut:
#     like_count = db.query(Like).filter(Like.post_id == p.id).count()
#     liked_by_me = db.query(Like).filter(Like.post_id == p.id, Like.user_id == current.id).first() is not None
#     comments = (
#         db.query(Comment).filter(Comment.post_id == p.id).order_by(Comment.created_at.asc()).all()
#     )
#     comments_out = [
#         CommentOut(id=c.id, text=c.text, user_id=c.user_id, username=c.user.username, created_at=c.created_at)
#         for c in comments
#     ]
#     return PostOut(
#         id=p.id,
#         caption=p.caption,
#         image_url=p.image_url,
#         created_at=p.created_at,
#         author_id=p.user_id,
#         author_username=p.author.username,
#         like_count=like_count,
#         liked_by_me=liked_by_me,
#         comments=comments_out,
#     )

# # --------------------------- Seed (optional) --------------------------- #
# @app.post("/seed", response_model=dict)
# def seed(db: Session = Depends(get_db)):
#     if db.query(User).count() > 0:
#         return {"ok": True, "note": "Already seeded"}
#     u1 = User(username="teja", password_hash=hash_password("password123"))
#     u2 = User(username="kaja", password_hash=hash_password("password123"))
#     db.add_all([u1, u2])
#     db.commit()
#     p1 = Post(caption="Hello from Teja", image_url="https://picsum.photos/seed/teja/600/400", user_id=u1.id)
#     p2 = Post(caption="Hi from Kaja", image_url="https://picsum.photos/seed/kaja/600/400", user_id=u2.id)
#     db.add_all([p1, p2])
#     db.commit()
#     return {"ok": True}

# # Root
# @app.get("/")
# def root():
#     return {"message": "Mini Instagram Clone API is running. See /docs"}
