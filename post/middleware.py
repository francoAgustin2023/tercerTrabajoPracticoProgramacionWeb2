
class RequestLogMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"REQUEST URL: {request.path} - Metodo: {request.method} - Usuario: {request.user}")
        response = self.get_response(request)
        print(f"RESPONSE: {response}")
        return response
        
    