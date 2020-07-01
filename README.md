# Android Debloater

### Clean your bloated device without root!

## Requirement

- **ADB**
- Python3
- A bloated android device
- A functional brain

## Debloating

1. Clone this repo:
   ```bash
   git clone https://github.com/Surendrajat/android-debloater && cd android-debloater
   ```
2. Connect device with `adb` and test with:
   ```bash
   adb decives
   ```
3. Run 
   ```bash
   adb shell pm list packages > pkg.list
   ```
5. Open **pkg.list** file and add a hyphen(-) to the bloat apps.
   
   For eg:
   Change
   `package:com.bloat.bs`
   to
   `-package:com.bloat.bs`
6. Save **pkg.list** and run:
   ```bash
   python debloater.py
   ```

## Troubleshooting

Meh! It's simple. Figure out yourself.