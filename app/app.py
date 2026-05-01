from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["devnotes"]
collection = db["notes"]

@app.route("/")
def home():
    return {"message": "DevNotes API running"}

@app.route("/notes", methods=["POST"])
def create_note():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"id": str(result.inserted_id)})

@app.route("/notes", methods=["GET"])
def get_notes():
    notes = []
    for note in collection.find():
        note["_id"] = str(note["_id"])
        notes.append(note)
    return jsonify(notes)

@app.route("/notes/<id>", methods=["DELETE"])
def delete_note(id):
    from bson import ObjectId
    collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Deleted"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
