# sudo pacman -S --needed $PACKAGE
# paru -S --needed $PACKAGE
# flatpak install $NAME $PACKAGE
PACKAGES = {
    "base":    {
        "pacman": [
            "base-devel", "git", "curl", "unzip", "unrar",
            "less", "man-db", "man-pages", "nmap", "tcpdump",
            "lsof", "tmux", "zellij", "vim", "neovim", 
            "rustup", "python", "uv", "ghostty", "tree",
            "bat", "tokei", "fastfetch", "firefox", "flatpak",
            "code", "pv"
        ]
    },
    "shell":   {
        "pacman": [
            "zsh", "zsh-completions", "zsh-autosuggestions", "zsh-syntax-highlighting"
        ]
    },
    "containers": {
        "pacman": [
            "podman", "podman-compose", "podman-docker", "podman-desktop"
        ]
    },
    "virt":    {
        "pacman": [
            "qemu-desktop", "virt-manager", "dnsmasq", "dmidecode"
        ]
    },
    "external":     {
        "aur": [
            "brave-bin", "k3s-bin"
        ],
        "flatpak": [
            "com.mattjakeman.ExtensionManager"
        ]
    }
}
