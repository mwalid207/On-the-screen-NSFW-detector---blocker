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
  LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
  shellHook = ''
    echo 'You are now in the >>> Haram Blocker \ for Linux development environment.'


    source "$VENV_DIR/bin/activate"
    
    # Set environment variables for grim to access the user's display
    export WAYLAND_DISPLAY=/run/user/1000/wayland-1
    export XDG_RUNTIME_DIR=/run/user/1000

    echo 'Environment variables for Wayland display set.'
  '';
}
