# import pymongo as pm
from pymongo import MongoClient
from bson import ObjectId
client  = MongoClient("mongodb+srv://youtube:youtube@youtube.jdd8wbf.mongodb.net/")
# I've deleted This user 
# contact deshmaneyogesh2002@gmail.com
# update The role of This User form reader to can able to write

db = client["ytmanager"]
video_collection = db["videos"]
 
# print(video_collection)


def list_videos():
    for video in video_collection.find():
        print(f"id : {video['_id']} , name :{video['name']}, time : {video['time']}")


def add_video(name ,time):
    video_collection.insert_one({"name":name,"time":time})



def update_videos(id,n_name,n_time):
    video_collection.update_one(
        {'_id':ObjectId (id)},
        {"$set":{"name":n_name,"time":n_time}}
    )


def delete_video(id):
    video_collection.delete_one({"_id":ObjectId(id)})



def main():
    while True:
        print("""Youtube Manager App""")
        print("1. List All Videos ")
        print("2. Add New Videos ")
        print("3. Update Videos ")
        print("4. Delete Videos ")
        print("5. EXIT")
        choice = input("Enter your Choice ")
        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter Video Name :")
                time = input("Enter Video Time :")
                add_video(name, time)
            case "3":
                id  = input("Enter video ID :")
                update_name = input("Enter the updated Video Name :")
                update_time = input("Enter the updated Video Time :")

                update_videos(id,update_name,update_time)
            case "4" :
                id  = input("Enter video ID :")
                delete_video(id)
            case "5": 
                exit()
            case "_":
                print("Enter Valid Choice")



if __name__ =="__main__":
    main()