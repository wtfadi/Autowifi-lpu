```markdown
# LPU WiFi Auto-Login

**Automated WiFi connection and login system for LPU (Lovely Professional University) campus network.** 

Continuously monitors WiFi connection, auto-connects to valid LPU networks (excludes jioNet@LPU), and handles captive portal login.

## Features

- ✅ **Auto-detects** valid LPU WiFi networks
- ✅ **Auto-connects** to available LPU SSIDs
- ✅ **Selenium-based** captive portal login
- ✅ **Continuous monitoring** (15s intervals)
- ✅ **Internet connectivity check**
- ✅ **Headless browser** (auto-closes after login)
- ✅ **Graceful error handling**
- ✅ **Windows netsh integration**

## Prerequisites

### Windows Requirements
- **Microsoft Edge** browser
- **Edge WebDriver** (auto-managed by Selenium 4+)
- Administrator privileges for WiFi commands

### Python Dependencies
```bash
pip install selenium requests
```

## Quick Setup

1. **Clone repository**
```bash
git clone https://github.com/yourusername/LPU-WiFi-Auto-Login
cd LPU-WiFi-Auto-Login
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure credentials** (edit `autologin.py`)
```python
USERNAME = "your_lpu_id"  # Your LPU student ID
PASSWORD = "your_password"
```

4. **Run as Administrator**
```bash
python autologin.py
```

## Configuration

**Edit these variables in `autologin.py`:**
```python
USERNAME = "12509995"  # Your LPU student ID
PASSWORD = "your_password"
```

**Optional environment variables:**
```bash
set LPU_USERNAME=your_id
set LPU_PASSWORD=your_pass
python autologin.py
```

## How It Works

```
1. 🔍 Scan for LPU WiFi networks (excludes jioNet@LPU)
2. 🔌 Auto-connect to valid SSID
3. 🌐 Wait for internet connectivity
4. 🔍 Check if captive portal login required
5. 🤖 Selenium login → Auto-close browser
6. 🔄 Repeat every 15 seconds
```

## Usage

### Run (Admin Required)
```bash
# As Administrator (PowerShell/Command Prompt)
python autologin.py
```

### Example Output
```
🚀 FINAL AUTO WIFI LOGIN SYSTEM STARTED

📡 Found valid WiFi: LPU-STUDENT-WIFI
🔌 Connecting to LPU-STUDENT-WIFI...
🌐 Waiting for internet...
🟢 Internet ready
🔴 Login required → starting login...
🔑 Filling credentials...
🚀 Logging in...
🟢 LOGIN SUCCESS → closing browser
🟢 Already logged in

[Repeats every 15s...]
```

## Supported Networks

✅ **Valid LPU Networks** (auto-detected):
- `LPU-STUDENT-WIFI`
- `LPU-FACULTY-WIFI`
- Any SSID containing "LPU" **except** `jioNet@LPU*`

❌ **Excluded**:
- `jioNet@LPU-*` (unreliable networks)

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `Access denied` | Run as **Administrator** |
| `Edge WebDriver not found` | Update Edge browser |
| `No LPU WiFi found` | Check WiFi adapter / airplane mode |
| `Login failed` | Verify `USERNAME`/`PASSWORD` |
| `Selenium errors` | `pip install --upgrade selenium` |

## Advanced Usage

### Custom Interval
```python
time.sleep(30)  # Change 15s → 30s interval
```

### Debug Mode
Add `print()` statements in functions for detailed logging.

### Multiple Credentials
Create `credentials.json`:
```json
{
  "primary": {"username": "12509995", "password": ""},
  "backup": {"username": "backup_id", "password": ""}
}
```

## WiFi Commands Reference

**Manual equivalents** (for testing):
```bash
# List networks
netsh wlan show networks

# List interfaces
netsh wlan show interfaces

# Connect
netsh wlan connect name="LPU-STUDENT-WIFI"
```

## Security Notes

- ✅ Credentials stored locally only
- ✅ Browser auto-closes after login
- ✅ No network transmission of credentials
- ✅ Windows netsh uses secure system APIs

## License

MIT License - see [LICENSE](LICENSE) for details.

---

**⭐ Star if helpful!**  
**🐛 Issues? [Open issue](https://github.com/yourusername/LPU-WiFi-Auto-Login/issues)**

---

```bash
# 🚀 One-liner setup (Admin required)
git clone <repo> && cd LPU-WiFi-Auto-Login && pip install -r requirements.txt && python autologin.py
```

**Made for LPU students ✨**
```
