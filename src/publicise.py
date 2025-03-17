import os, shutil

static = "./static"
public = "./public"


def handle_files(src, dst):
    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        if os.path.isfile(item_path):
            print(f"{os.path.join(dst, item)}")
            shutil.copy(item_path, dst)
        elif os.path.isdir(item_path):
            folder_path = os.path.join(dst, item)
            print(f"{folder_path}")
            os.mkdir(folder_path)
            handle_files(item_path, folder_path)


def publicise():
    print("-----COPYING STATIC TO PUBLIC-----")
    print("CHECKING\n./public exists... " + str(os.path.exists("./public")))
    if not os.path.exists("./public"):
        print("CREATING\n./public...")
        os.mkdir("./public")
    else:
        print("DELETING\n./public")
        shutil.rmtree("./public/")
        print("CREATING\n./public")
        os.mkdir("./public")

    handle_files(static, public)


if __name__ == "__main__":
    publicise()
