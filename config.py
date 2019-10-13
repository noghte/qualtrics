DATA_CENTER = "terry"
SURVEY_ID = "SV_6ViRhA5W64pm3kh"
TOKEN_FILENAME = "token.txt"

def read_token_from_file():
    token = ""
    with open(TOKEN_FILENAME) as f:
        token = f.readline()
    return token
