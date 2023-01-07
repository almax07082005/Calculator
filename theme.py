import winreg


def theme_is_light():
    t = winreg.OpenKey(winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER), r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize')
    for i in range(1024):
        try:
            temp = winreg.EnumValue(t, i)
            if temp[0] == 'AppsuseLightTheme' and temp[1]:
                return True
        except:
            return False
