{ pkgs ? import <nixpkgs> {} }:

let
  rustEnv = pkgs.mkShell {
    buildInputs = [
      pkgs.rustc
      pkgs.cargo
      pkgs.makeWrapper
      pkgs.scdoc
    ];
  };
  
  pythonEnv = pkgs.mkShell {
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
  };
in

pkgs.mkShell {
  buildInputs = rustEnv.buildInputs ++ pythonEnv.buildInputs;

  LD_LIBRARY_PATH = pythonEnv.LD_LIBRARY_PATH;

  shellHook = ''
    echo 'You are now in the >>> Haram Blocker \ for Linux development environment.'

    # Activate the Poetry virtual environment
    poetry shell

    # Set environment variables for grim to access the user's display
    export WAYLAND_DISPLAY=/run/user/1000/wayland-1
    export XDG_RUNTIME_DIR=/run/user/1000

    echo 'Environment variables for Wayland display set.'
  '';
}
