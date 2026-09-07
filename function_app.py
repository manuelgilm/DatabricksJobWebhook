import json
import logging

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

logger = logging.getLogger(__name__)


@app.function_name(name="databricks_job_webhook")
@app.route(route="webhook", methods=["POST"])
def databricks_job_webhook(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_body().decode("utf-8")
    except Exception:
        body = ""

    if body:
        try:
            logger.info("Webhook payload:\n%s", json.dumps(json.loads(body), indent=2))
        except ValueError:
            logger.info("Webhook payload (raw body):\n%s", body)
    else:
        logger.info("Webhook payload: (empty body)")

    return func.HttpResponse(
        body=json.dumps({"status": "ok"}),
        status_code=200,
        mimetype="application/json",
    )
