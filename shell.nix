{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python310
    pkgs.poetry
    pkgs.zlib
    pkgs.glib
    pkgs.gcc
    pkgs.grim # screenshot taking
    pkgs.libnotify # notify-send
    pkgs.stdenv.cc.cc
  ];

  shellHook = ''
    echo 'You are now in the >>> Haram Blocker \ for Linux development environment.'
    
    
    # Set Poetry to use Python 3.10
    poetry env use python3.10

    # Activate the Poetry virtual environment
    poetry shell

    # Set environment variables for grim to access the user's display
    export WAYLAND_DISPLAY=/run/user/1000/wayland-1
    export XDG_RUNTIME_DIR=/run/user/1000

    echo 'Environment variables for Wayland display set.'
  '';
}
