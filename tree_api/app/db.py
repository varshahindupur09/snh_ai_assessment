from sqlmodel import create_engine, Session

engine = create_engine("sqlite:///tree.db", echo=False)

def get_session():
    with Session(engine) as session:
        yield session
