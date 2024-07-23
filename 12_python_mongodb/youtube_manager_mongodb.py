from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://CHAI:CHAI@cluster0.lxl3fsq.mongodb.net/", tlsAllowInvalidCertificates=True)

print(client)
db = client["ytmanager"]
video_collection = db["videos"]


def list_videos(videos):
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one({"_id": ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})


def delete_video(video_id):
    video_collection.update_one({"_id": video_id})

def main():
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name:\n ")
                time = input("Enter the video time:\n ")
                add_video(name, time)
            case '3':
                video_id = input("Enter the video ID to update:\n ")
                name = input("Enter the video name:\n ")
                time = input("Enter the video time:\n ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter the video ID to update:\n ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()