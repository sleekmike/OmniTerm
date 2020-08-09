# OmniTerm

# Features
-  HUB of popular terminal extentions/add-ons and utilities.
- Ability to change the Desktop Wallpaper & the Terminal background
- Supports iTerm2, ConEmu, Terminology, Windows Terminal and Tilix terminal emulators
- Supports Windows, MacOS, GNOME, Openbox (with feh), i3wm (with feh) and sway for desktops

# Installation

Install Python 3.7 or higher:
- [For Mac](https://www.python.org/downloads/mac-osx/)
- For Windows: [desktop](https://www.python.org/downloads/windows/) or [Microsoft Store](https://www.microsoft.com/p/python-38/9mssztt1n39l)
- [For Ubuntu](https://askubuntu.com/a/865569)
- [For Arch Linux](https://www.archlinux.org/packages/extra/x86_64/python/)
- Not all compatible distros are named here, but a quick Google search should give you instructions for your distribution of choice.

Get a compatible terminal emulator:
- [iTerm2](https://iterm2.com/)
- [ConEmu](https://conemu.github.io/) or derivative (such as [Cmder](http://cmder.net/))
- [Terminology](https://www.enlightenment.org/about-terminology)
- [Tilix](https://gnunn1.github.io/tilix-web/)
- [Windows Terminal](https://www.microsoft.com/p/windows-terminal-preview/9n0dx20hk701)

You can then proceed with one of the following methods for installation:

Clone and Download this repo and run pyt


## pip

Linux users: Your distro might include `pip` in a different package than Python, make sure to have that installed.

Run `pip3 install git+https://github.com/LazoCoder/Pokemon-Terminal.git`.

If you want a system-wide install, run the command as superuser or administrator.

If you want a per-user install, append the `--user` flag.

You might want to add the following directories to your `PATH` on a per-user install, to be able to call `pokemon` and `ichooseyou` everywhere:
 - Linux and macOS: `~/.local/bin`
 - Windows: (replace `X` by your Python minor version, for example, 8 for Python 3.8)
   - `%AppData%\Python\Python3X\Scripts` for a desktop installation of Python;
   - `%LocalAppData%\Packages\PythonSoftwareFoundation.Python.3.X_qbz5n2kfra8p0\LocalCache\local-packages\Python3X\Scripts` for a Microsoft Store installation of Python (note that there's two `X` here).

When the command completes, it's installed and ready to go!




# Usage

After successfully installing this repository, you can call any of the following terminal add-ons/extensions or utilities by calling the name on your terminal.

# Tips, tricks and common issues

## iTerm2 settings

I highly suggest making the font colors black and the terminal window transparent. Some of the images have both light and dark colours and so it can be difficult to see the text sometimes. Transparency resolves this issue. Since *Pokemon-Terminal* only changes the background, the transparency must be done manually:

1. Navigate to iTerm2 > Preferences > Profiles > Window
2. Set the transparency to about half way.
3. Hit the "blur" checkbox.
4. Set the blur to maximum.
5. Optionally you can set the blending to maximum to adjust the colors to look like the samples provided.

![](https://i.imgur.com/xSZAGhL.png)

The result should look like this:

![](https://i.imgur.com/82DAT97.jpg)

## ConEmu settings

1. From the menu under the symbol at left of title bar, navigate to Settings > Main > Background
2. Set Darkening to maximum (255).
3. Set Placement to Stretch.
4. Click Save Settings.
5. Optionally you apply transparency under Features > Transparency.

## Windows Terminal settings

You can, like in iTerm2, enable transparency. Simply press the down arrow in the tab bar and click settings. Once the JSON file opens, add the following settings under the `defaults` section:

```json
"backgroundImageOpacity": 0.5,
"useAcrylic": true,
"acrylicOpacity": 0.0
```

The result should look like this:

![](https://i.imgur.com/DZbiQHf.png)

## Solutions for Common Issues

* If you experience a line at the top of the terminal after changing the Pokemon, you can remove it by typing in the `clear` command or opening a new terminal.
![](https://i.imgur.com/5HMu1jD.png)

* If you are using Tilix and the terminal background is not changing, try adjusting the transparency in your profile settings.
* If you are experiencing issues with Terminology and are running on Ubuntu, make sure that you have installed the latest version:
   ```bash
   $ sudo add-apt-repository ppa:niko2040/e19
   $ sudo apt-get update
   $ sudo apt install terminology
   ```

## Saving

### iTerm2
To save a background you will need to setup a startup command in the profile:
1. Navigate to iTerm2 > Preferences > General
2. Locate the field where it says *Send text at start* under *Command*.
3. In that field type `pokemon -n [pokemon name]`. You can see an example in the image down below.
   - Alternatively you can also type `pokemon` for a random theme each time you open up a new terminal.
4. You can leave out `; clear` if you don't care about the line showing up at the top of the terminal.

![](https://i.imgur.com/2d4qa9j.png)

### ConEmu
After setting your desired pokemon, from the menu under the symbol at left of title bar, navigate to Settings > Main > Background and click Save Settings.

### Terminology
Terminology already saves it automatically, just untick "temporary" in the settings after setting your desired Pokemon:
![](http://i.imgur.com/BTqYXKa.png)

# Notes & Credits

- Platforms:
  - Thanks to [@samosaara](https://github.com/samosaara) for the Linux (GNOME and Terminology) port.
  - Thanks to [@jimmyorourke](https://github.com/jimmyorourke) for the Windows (ConEMU and wallpaper) port.
  - Thanks to [@sylveon](https://github.com/sylveon) for the Windows slideshow functionality and maintaining the AUR package.
- Terminal & wallpaper support:
  - Thanks to [@MattMattV](https://github.com/MattMattV) for adding Tilix support.
  - Thanks to [@regenbogencode](https://github.com/regenbogencode) for sway support.
  - Thanks to [@kyle-seongwoo-jun](https://github.com/kyle-seongwoo-jun) for Windows Terminal support.
- Thanks to [@DrMartinLutherXing](https://github.com/DrMartinLutherXing) for some bug fixes.
- Thanks to [@joanbono](https://github.com/joanbono) for the easy installation script in the readme.
- Thanks to [@BnMcG](https://github.com/BnMcG) for the region specific randomize function.
- Thanks to [@therealklanni](https://github.com/therealklanni) for adding the project to npm.
- Thanks to [@connordinho](https://github.com/connordinho) for enhancing the slideshow functionality.
- Thanks to [@cclauss](https://github.com/cclauss) for simplifying the code in the database class and the main class, as well as general code quality fixes.
- Thanks to [@Fiskie](https://github.com/Fiskie) for implementing the adapter design pattern, piping commands and more.
- Thanks to [@marcobiedermann](https://github.com/marcobiedermann) for better image compression.
- Thanks to [@kamil157](https://github.com/kamil157) and [@dosman711](https://github.com/dosman711) for the randomized slideshow function.
- Thanks to [@Squirrels](https://github.com/Squirrels) for adding Pokemon from the Unova and Kalos regions.
- Thanks to [@caedus75](https://github.com/caedus75) for pip and reorganizing the files & folders.
