from flask import jsonify, request, Response
from app import app
from app.validating_apis import pods


@app.route("/api/v1/validate/podtemplate/pod-readiness", methods=["POST"])
def podtemplate_pod_readiness():
    """
    :return: (http) response
    """
    allowed = True
    result = ""
    data = request.json  # K8s spec sent in url body by admission controller
    try:
        obj = data["request"]["object"]
        containers = obj["spec"]["template"]["spec"]["containers"]
        if not pods.validate_pod_readiness(containers):
            allowed = False
            result = "Pod spec requires a readiness probe"
    except Exception as e:
        allowed = False
        result = str(e)

    response = {"response": {"allowed": allowed, "status": {"reason": result}}}

    with open("app.log", "a") as f:
        import json
        f.write(json.dumps(obj))
        f.write(json.dumps(response))

    return jsonify(response)

