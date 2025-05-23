# 💚 Monster Boost - Roblox Performance Enhancer 💚

[![PowerShell](https://img.shields.io/badge/PowerShell-Enabled-blue?logo=powershell)](https://docs.microsoft.com/powershell/)  
[![Windows](https://img.shields.io/badge/Platform-Windows-lightgrey?logo=windows)](https://www.microsoft.com/windows)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## What is Monster Boost?

**Monster Boost** is a PowerShell-based performance enhancer tailored specifically for Roblox players. It applies a suite of system tweaks to maximize FPS, reduce latency, clean RAM, and optimize system resources — all with a single click!

The package contains two essential files:  

- `MonsterBoost.ps1` — The core PowerShell script applying tweaks and launching Roblox.  
- `RunMonsterBoost.bat` — A convenient batch launcher that runs the PowerShell script with elevated Administrator privileges.

---

## How to Use

1. **Keep `RunMonsterBoost.bat` and `MonsterBoost.ps1` in the *same folder*.**  
   Do not separate or move one without the other.

2. **Run `RunMonsterBoost.bat` by double-clicking it.**  
   This batch file:
   - Automatically runs the PowerShell script as Administrator.  
   - Displays a console window showing progress and messages.  
   - Keeps the window open until you press any key.

3. **Administrator permissions are required.**  
   The script needs Admin rights to apply system tweaks successfully. If you don't run the batch file as Admin, it will prompt or fail to apply some changes.

---

## Why this Setup?

- **PowerShell scripts (`.ps1`) cannot reliably be run by double-clicking in Windows** due to security policies and execution restrictions.  
- The batch file launcher **handles launching the script with the correct execution policy and Administrator privileges** automatically.  
- This method works **regardless of your Windows username or folder location**, making it portable and easy to use.

---

## Additional Notes

- Feel free to move the folder anywhere on your PC, but keep the `.bat` and `.ps1` files together.  
- For easier access, create a shortcut to `RunMonsterBoost.bat` on your desktop or Start Menu.  
- Always launch the boost using the batch file to ensure proper permissions and settings.

---

## Troubleshooting

- **Script fails to launch Roblox or apply tweaks?**  
  Ensure you are running as Administrator.

- **Execution policy errors?**  
  The batch file temporarily bypasses PowerShell’s execution policy, so always run the `.bat` launcher.

- **Roblox already running?**  
  Close any running Roblox instances before launching Monster Boost for best results.

---

## Future Improvements

- GUI-based launcher for easier tweak selection and status feedback  
- Portable EXE wrapper with system tray integration  
- Custom profiles for different gaming scenarios  

---

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it as you wish!

---

## Enjoy your boosted Roblox experience! 💚⚡

---

*Made with ❤️ by [YourName]*

