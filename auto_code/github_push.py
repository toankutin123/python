import os

def push_github():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.abspath(os.path.join(current_dir, ".."))

        os.chdir(root_dir)

        print("📦 Đang add file...")
        os.system("git add .")

        print("📝 Commit...")
        os.system('git commit -m "auto add bai tap"')

        print("🔄 Pull code mới nhất...")
        os.system("git pull --rebase origin main")

        print("🚀 Push lên GitHub...")
        os.system("git push origin main")

        print("✅ Đã push lên GitHub!")

    except Exception as e:
        print("❌ Lỗi:", e)