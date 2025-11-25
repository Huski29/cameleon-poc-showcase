import os
import sys

db_path = "cameleon.db"

if os.path.exists(db_path):
    try:
        os.remove(db_path)
        print(f"Deleted old database: {db_path}")
    except Exception as e:
        print(f"Could not delete {db_path}: {e}")
        print("Please close any applications using the database and try again.")
        sys.exit(1)

from app.database import engine, Base
from app import models

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Database recreated with new schema!")
print("\nNow run: python seed.py")

