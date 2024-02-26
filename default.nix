{ pkgs ? import
    (fetchTarball {
      name = "jpetrucciani-2024-02-25";
      url = "https://github.com/jpetrucciani/nix/archive/59ed571fce26b2b3e13f3db6cb0d1b3bcccf80a9.tar.gz";
      sha256 = "0zxx5rhnj6sskbf532dp56w9lsq1m31yr1sl6g95hn5wsgxb6ms0";
    })
    { }
}:
let
  name = "StockMeme";

  python = (pkgs.poetry2nix.mkPoetryEnv {
    projectDir = ./.;
    python = pkgs.python311;
    overrides = pkgs.poetry2nix.overrides.withDefaults (final: prev: { });
    preferWheels = true;
  }).overrideAttrs (old: { buildInputs = with pkgs; [ libcxx ]; });

  tools = with pkgs; {
    cli = [
      coreutils
      nixpkgs-fmt
    ];
    python = [
      ruff
      poetry
    ];
    scripts = pkgs.lib.attrsets.attrValues scripts;
  };

  scripts = with pkgs; { };
  paths = pkgs.lib.flatten [ (builtins.attrValues tools) ];
  env = python.env.overrideAttrs (_: {
    buildInputs = paths;
  });
in
(env.overrideAttrs (_: {
  inherit name;
  NIXUP = "0.0.6";
})) // { inherit scripts; }
