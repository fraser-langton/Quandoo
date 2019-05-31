class ErrorResponse(Exception):

    def __init__(self, status_code, data, request):
        self.statusCode = status_code
        self.errorType = data["errorType"]
        self.errorMessage = data["errorMessage"]
        self.request = request

    def __str__(self):
        return "{} {}: {}".format(self.statusCode, self.errorType, self.errorMessage)
