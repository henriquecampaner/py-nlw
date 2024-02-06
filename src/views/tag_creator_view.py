from src.controller.tag_creator_controller import CreateTagController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:
    """
    Responsible for interacting with HTTP
    """

    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        tag_creator_controller = CreateTagController()

        body = http_request.body
        product_code = body.get("product_code")

        if product_code is None:
            return HttpResponse(
                status_code=400, body={"error": "Product code is required"}
            )

        formatted_response = tag_creator_controller.create(product_code)

        return HttpResponse(status_code=200, body=formatted_response)
