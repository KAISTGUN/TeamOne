REGEX_USERNAME = '^[A-Za-z0-9]{,20}$' # TODO: should be changed based on MySQL
#REGEX_PASSWORD = '' # TODO: should be changed based on MySQL
REGEX_EMAIL = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
REGEX_PHONE = '^\d{11}$'
REGEX_AMOUNT = '^[0-9]*$' 
LEN_PASSWORD = 20 # TODO: should be changed based on MySQL
LEN_EMAIL = 45
LEN_MSG = 100

CLEAR_TERMINAL = b"\x1b[2J\x1b[H"

COR_LOGO = b"\033[1;36;40m"
COR_BASE = b"\033[0;33;40m"
COR_ERRMSG = b"\033[1;37;41m"
COR_SUCCESS = b"\033[0;30;42m"
COR_DEFAULT = b"\033[0m"
COR_RESULT = b"\033[1;37;45m"

ERRMSG_OPTION = COR_ERRMSG+ b" Invalid input.\n" + COR_BASE

#ERRMSG_USER_LEN = (COR_ERRMSG + " Username should be shorter than " +
#                    str(LEN_USERNAME) + ".\n" + COR_BASE)
ERRMSG_USER_NULL = COR_ERRMSG + b" Please input the username.\n" + COR_BASE
ERRMSG_USER_INVAL = COR_ERRMSG + b" Invalid username.\n" + COR_BASE

ERRMSG_PW_LEN = (COR_ERRMSG + b" Password should be shorter than " + 
                    bytes(str(LEN_PASSWORD).encode()) + b".\n" + COR_BASE)
ERRMSG_PW_NULL = COR_ERRMSG +  b" Please input the password.\n" + COR_BASE
ERRMSG_PW_WRONG = COR_ERRMSG +  b" Incorrect password.\n" + COR_BASE

ERRMSG_RECV_NULL = COR_ERRMSG + b" Please input the receiver.\n" + COR_BASE
ERRMSG_RECV_INVAL = COR_ERRMSG + b" Invalid receiver.\n" + COR_BASE

ERRMSG_WON_NULL = COR_ERRMSG + b" Please input amount to transfer.\n" + COR_BASE
ERRMSG_WON_INVAL = COR_ERRMSG + b" Invalid amount.\n" + COR_BASE
ERRMSG_WON_LIMIT = COR_ERRMSG + b" Transfer amount cannot exceed balance.\n" + COR_BASE

ERRMSG_EMAIL_NULL = COR_ERRMSG +  b" Please input the email.\n" + COR_BASE
ERRMSG_EMAIL_INVAL = COR_ERRMSG + b" Invalid email.\n" + COR_BASE
ERRMSG_EMAIL_LEN = (COR_ERRMSG + b" Email should be shorter than " + 
                    bytes(str(LEN_EMAIL).encode()) + b".\n" + COR_BASE)

ERRMSG_PHONE_NULL = COR_ERRMSG +  b" Please input the phone number.\n" + COR_BASE
ERRMSG_PHONE_INVAL = COR_ERRMSG + b" Invalid phone number.\n" + COR_BASE

ERRMSG_MSG_NULL = COR_ERRMSG +  b" Please input the transfer message.\n" + COR_BASE
ERRMSG_MSG_LEN = (COR_ERRMSG + b" Transfer message should be shorter than " + 
                    bytes(str(LEN_MSG).encode()) + b".\n" + COR_BASE)
