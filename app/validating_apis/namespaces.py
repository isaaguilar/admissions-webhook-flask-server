from flask import jsonify, request, Response
from app import app


@app.route("/api/v1/validate/namespace/labels", methods=["POST"])
def namespace_labels():
    """
    :return: (http) response
    """
    allowed = True
    result = ""
    data = request.json  # K8s spec sent in url body by admission controller
    try:
        metadata = data["request"]["object"]["metadata"]
        if not metadata.get("labels"):
            allowed = False
            result = "'environment' label is required"
        else:
            if not metadata["labels"].get("environment"):
                allowed = False
                result = "'environment' label is required"
    except Exception as e:
        allowed = False
        result = str(e)

    return jsonify({
        "response": {
            "allowed": allowed,
            "status": {
                "reason": result
            }
        }
    })