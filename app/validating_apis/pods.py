from flask import jsonify, request, Response
from app import app


@app.route("/api/v1/validate/pod/readiness", methods=["POST"])
def pod_readiness():
    """
    :return: (http) response
    """
    allowed = True
    result = ""
    data = request.json  # K8s spec sent in url body by admission controller
    try:
        container_specs = data["request"]["object"]["spec"]["containers"]
        if not validate_pod_readiness(container_specs):
            allowed = False
            result = "Pod spec requires a readiness probe"
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

def validate_pod_readiness(container_specs):
    for spec in container_specs:
        if spec.get("readinessProbe") is None:
            return False
    return True
        