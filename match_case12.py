def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
           return "internal server Error"
        case _:
            return"unknown status"
print(http_status(5006))


    