import bcrypt


def hashPassword(password: str):
    hashied = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt(rounds=12))
    return hashied.decode("utf-8")

def checkPassword(password: str, hashiedPassword: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashiedPassword.encode("utf-8"))
    

