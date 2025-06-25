status_code = 203

match status_code:
    case 200 | 201 | 202:
        print("Success")
    case 400 | 401 | 403:
        print("Client error")
    case 500 | 501 | 502:
        print("Server error")
    case _:
        print("Unknown status")