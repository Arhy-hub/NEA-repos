import bcrypt

def hash_content(content):
    salt = bcrypt.gensalt()
    hashed_content = bcrypt.hashpw(content.encode('utf-8'), salt)
    verify_hash(content,hashed_content)
    return hashed_content

def verify_hash(content, hashed_content):
    return bcrypt.checkpw(content.encode('utf-8'), hashed_content)