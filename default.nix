{
  pkgs ? import (fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/23.11.tar.gz";
    sha256 = "sha256:1ndiv385w1qyb3b18vw13991fzb9wg4cl21wglk89grsfsnra41k";
  }) {}
}:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311Packages.moviepy
    pkgs.python311Packages.pandas
    pkgs.python311Packages.setuptools
  ];
}
