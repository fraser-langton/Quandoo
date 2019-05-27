class ErrorResponse(Exception):

    def __init__(self, status_code, data):
        self.statusCode = status_code
        self.errorType = data["errorType"]
        self.errorMessage = data["errorMessage"]

    def __str__(self):
        return "{} {}: {}".format(self.statusCode, self.errorType, self.errorMessage)
