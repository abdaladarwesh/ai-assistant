from plyer import *
def noti(text : str):
    notification.notify(
        title="Nova",
        message=f"{text}",
        app_name="Nova",
        app_icon="gg.ico",  # Optional
        timeout=1
    )
if __name__ == "__main__":
    noti("hello wrold")
