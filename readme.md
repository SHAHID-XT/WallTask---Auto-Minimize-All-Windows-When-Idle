# **WallTask — Auto-Minimize All Windows When Idle**

This is a tiny personal project I built because I wanted one simple thing:
whenever my PC is idle, minimize every window so the wallpaper is always visible.
No gimmicks, no UI, just clean background magic.

The script quietly watches for idle time, and when it hits the limit, it minimizes everything — giving you a clear desktop view like a live wallpaper frame.
---

## **What This Script Does**

* Runs silently using **pythonw.exe** (no console popup)
* Checks system idle time
* When idle > limit → **minimizes every window**
* Waits a bit, then continues monitoring
* Designed to run fully hidden from startup

---

## **Default Paths Used**

### **Python (pythonw.exe)**

These are the common default install paths:

```
C:\Users\<username>\AppData\Local\Programs\Python\Python313\pythonw.exe
C:\Users\<username>\AppData\Local\Programs\Python\Python312\pythonw.exe
C:\Users\<username>\AppData\Local\Programs\Python\Python311\pythonw.exe
C:\Users\<username>\AppData\Local\Programs\Python\Python39\pythonw.exe
```

If you're using this repo "as is," the XML expects:

```
C:\Users\admin\AppData\Local\Programs\Python\Python313\pythonw.exe
```

### **Script Path**

The default script location used in the project:

```
C:\idle_monitor\idle_monitor.py
```

You can change it — just make sure you update the Task Scheduler XML.

---

## **How to Run Manually**

If you want to test it:

```
"C:\Users\admin\AppData\Local\Programs\Python\Python313\pythonw.exe" C:\idle_monitor\idle_monitor.py
```

No window will show. It runs silently in the background.

---

## **Automatically Run at Startup**

This repo includes a ready-to-import Task Scheduler file:

```
WallTask.xml
```

### **To import the task:**

1. Open **Task Scheduler**
2. Click **Import Task**
3. Select **WallTask.xml**
4. Save it
5. Done — it will now run hidden at boot

The XML is already configured with:

* Highest privileges
* Hidden execution
* Boot trigger
* `pythonw.exe` launcher
* Full script path
* No console window

---

## **Included XML (WallTask.xml)**

```xml
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.3" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Author>DESKTOP-O7K4OSO\Admin</Author>
    <URI>\WallTask</URI>
  </RegistrationInfo>
  <Triggers>
    <BootTrigger>
      <Enabled>true</Enabled>
    </BootTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>S-1-5-21-4170502357-3273478604-883288445-1000</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
    <AllowHardTerminate>true</AllowHardTerminate>
    <StartWhenAvailable>false</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>true</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>true</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT72H</ExecutionTimeLimit>
    <Priority>7</Priority>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>C:\Users\admin\AppData\Local\Programs\Python\Python313\pythonw.exe</Command>
      <Arguments>C:\idle_monitor\idle_monitor.py</Arguments>
    </Exec>
  </Actions>
</Task>
```

---

## **Why I Built This**

Because I wanted:

* A clean desktop when idle
* A way to show my wallpaper without closing my apps
* A background tool that behaves and stays out of the way

Tiny idea → tiny script → surprisingly useful.

---

# Note
> **Important:** Before importing `WallTask.xml`, update the paths and IDs to match your machine — replace the `pythonw.exe` path, the script path (`C:\idle_monitor\idle_monitor.py`), and the `Author` / `UserId` / hostname entries with your username/host values (e.g. `C:\Users\<yourname>\AppData\Local\Programs\Python\Python313\pythonw.exe`, `C:\idle_monitor\idle_monitor.py`, `DESKTOP-XXXX\<youruser>`).
