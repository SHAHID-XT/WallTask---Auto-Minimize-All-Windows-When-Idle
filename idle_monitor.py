import time
import ctypes
import win32api
import win32con

class LASTINPUTINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.c_uint),
        ("dwTime", ctypes.c_uint),
    ]


class IdleMonitor:
    is_log_enable = False
    def __init__(self, idle_limit_seconds=300):
        self.idle_limit = idle_limit_seconds
        if not self.is_log_enable:
            def print(*args, **kwargs):
                pass

    def get_idle_time(self):
        """Return system idle time in seconds."""
        last_input = LASTINPUTINFO()
        last_input.cbSize = ctypes.sizeof(last_input)
        ctypes.windll.user32.GetLastInputInfo(ctypes.byref(last_input))

        millis = ctypes.windll.kernel32.GetTickCount() - last_input.dwTime
        return millis / 1000.0

    def minimize_all_windows(self):
        """Minimize all open windows using Shell.Application."""
        try:
            shell = ctypes.windll.shell32
            shell.ShellExecuteW(
                None,
                "open",
                "powershell.exe",
                " -command \"(New-Object -ComObject Shell.Application).MinimizeAll()\"",
                None,
                0  # run hidden
            )
        except Exception as e:
            print(f"Error minimizing windows: {e}")

    def start(self):
        print(f"IdleMonitor started, limit = {self.idle_limit} seconds")

        while True:
            idle_time = self.get_idle_time()

            if idle_time > self.idle_limit:
                print("Idle limit reached → Minimizing all windows...")
                self.minimize_all_windows()
                time.sleep(10)  # Wait so it doesn't minimize repeatedly

            time.sleep(1)


if __name__ == "__main__":
    monitor = IdleMonitor(idle_limit_seconds=300)  # 5 minutes
    monitor.start()
