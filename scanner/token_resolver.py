# James Chomchan Gojit, ID:015785846 - Token Resolver
# This file is used to define the function required to convert lexemes into tokens that the parser
# will use.
def get_token_id(index):
    """
    token_ids = [
        "grave", "lbracket", "rbracket", "lbrace", "rbrace", "lsquig", "rsquig", "at", "ampersand", "hash",
        "bang", "tilde", "squote", "dquote", "dollar", "colon", "semicolon", "period", "comma", "plus",
        "minus", "slash", "backslash", "star", "equal", "carat", "lparen", "rparen", "ddash", "dplus",
        "plusminus", "minusplus", "greatereq", "lesseq", "noteq", "spaceshp", "eqeq", "coloneq", "dless",
        "dgreater", "slasheq", "dbang", "dcolon", "identifier", "integer", "currency", "library", "fixed",
        "scinotation", "file", "string", "comment", "whspace"
    ]
    """

    token_ids = [
        "`", "<", ">", "[", "]", "{", "}", "@", "&", "#",
        "!", "~", "'", "\"", "$", ":", ";", ".", ",", "+",
        "-", "/", "\\", "*", "=", "^", "(", ")", "--", "++",
        "+-", "-+", ">=", "<=", "!=", "<>", "==", ":=", "<<",
        ">>", "/=", "!!", "::", "id", "int", "currency", "library", "real",
        "sci", "file", "string", "comment", "whspace", "!accept"
    ]

    return token_ids[index]
