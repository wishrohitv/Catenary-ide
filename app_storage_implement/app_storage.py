from kivy import platform

__all__ = ("storage_path",)

if platform == "win":
    storage_path = "ide-workspace"
else:
    from android.storage import app_storage_path
    from android import mActivity

    context = mActivity.getApplicationContext()
    result = context.getExternalFilesDir("")  # don't forget the argument
    if result:
        storage_path = str(result.toString())
    else:
        storage_path = app_storage_path()  # NOT SECURE
