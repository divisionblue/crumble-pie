# --- Install the needed packages for a regenradar.
packages = [
    'binutils',
    'build-essential',
    'etckeeper',
    'git',
    'htop',
    'lynx-cur',
    'ntp',
    'python-dev',
    'python-imaging',
    'python-numpy',
    'python-scipy',
    'python-setuptools',
    'rdiff-backup',
    'unzip',
    'vim',
    ]

packages.each do |pkg|
  package pkg
end
