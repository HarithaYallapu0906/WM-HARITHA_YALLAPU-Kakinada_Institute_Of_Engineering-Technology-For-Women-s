from flask import Flask, request, jsonify

app = Flask(__name__)

# temporary storage (can be replaced with DB)
bin_data = {}

@app.route("/update", methods=["POST"])
def update_bin():
    data = request.json
    bin_id = data.get("bin_id")
    level = data.get("level")

    if level < 0 or level > 100:
        return jsonify({"status": "Invalid reading"}), 400

    status = "Empty"
    if level >= 75:
        status = "Full"
    elif level >= 30:
        status = "Partially Filled"

    bin_data[bin_id] = {
        "level": level,
        "status": status
    }

    return jsonify({"message": "Data updated", "bin": bin_data[bin_id]})

@app.route("/bins", methods=["GET"])
def get_bins():
    return jsonify(bin_data)

if __name__ == "__main__":
    app.run(debug=True)
